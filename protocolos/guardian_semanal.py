#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════
 GUARDIÁN SEMANAL v1.0 — Protocolo de diagnóstico y auto-reparación
 Familia Evergarden · Hermes Agent
═══════════════════════════════════════════════════════════════════
Patrón watchdog:
  · Modo completo (sin argumentos): diagnóstico integral + reporte
    semanal siempre visible (modelo, gateway, cron, disco, logs,
    procesos). Se entrega por stdout al canal configurado + Discord.
  · Modo --quick: solo modelo primario + gateway. Si todo está bien,
    stdout VACÍO = no notifica. Si el modelo murió, lo repara y
    reporta la reparación.
El script NUNCA imprime tokens ni secretos. Solo estados.
═══════════════════════════════════════════════════════════════════
"""

import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

try:
    import yaml
except ImportError:
    yaml = None  # solo se necesita para reparar; el diagnóstico sigue

# ─── Rutas portátiles (funciona en cualquier nodo de la familia) ───
def hermes_home():
    h = os.environ.get("HERMES_HOME")
    if h and os.path.isdir(h):
        return h
    base = os.environ.get("LOCALAPPDATA")
    if base and os.path.isdir(os.path.join(base, "hermes")):
        return os.path.join(base, "hermes")
    return os.path.expanduser("~/.hermes")

HOME = hermes_home()
CONFIG = os.path.join(HOME, "config.yaml")
AUTH = os.path.join(HOME, "auth.json")
ENV = os.path.join(HOME, ".env")

# Canal de Discord donde la familia reporta estado (#estado)
DISCORD_STATUS_CHANNEL = "1551628670915969105"

# Candidatos de respaldo EN ORDEN DE PREFERENCIA (verificados 2026-09-23)
FALLBACK_CANDIDATES = [
    ("nous", "meituan/longcat-2.0:free"),
    ("nous", "stepfun/step-3.7-flash:free"),
    ("nous", "upstage/solar-pro4:free"),
    ("nous", "inclusionai/ling-3.0-flash-sante:free"),
    ("nous", "poolside/laguna-s-2.1:free"),
    ("gemini", "gemini-2.5-flash"),
    ("gemini", "gemini-flash-latest"),
    ("gemini", "gemini-2.5-flash-lite"),
]

QUICK = "--quick" in sys.argv
lines = []          # reporte
ALERT = "🚨"        # problema no reparable
FIXED = "🔧"        # reparado automáticamente
OKK = "✅"
repaired_something = False


def hermes_bin():
    """Resuelve el ejecutable hermes en cualquier nodo (PATH o venv hermano)."""
    hb = shutil.which("hermes")
    if hb:
        return hb
    for cand in ("hermes.exe", "hermes"):
        p = os.path.join(os.path.dirname(sys.executable), cand)
        if os.path.isfile(p):
            return p
    return "hermes"


HERMES = hermes_bin()


def say(icon, msg):
    lines.append(f"{icon} {msg}")


def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# ─── Utilidades de secretos (nunca imprimir valores) ───
def read_env_var(name):
    """Lee una variable del .env real de Hermes. Devuelve None si falta."""
    if not os.path.isfile(ENV):
        return None
    try:
        with open(ENV, encoding="utf-8", errors="replace") as f:
            for line in f:
                if line.startswith(name + "="):
                    val = line.partition("=")[2].strip().strip('"').strip("'")
                    return val or None
    except OSError:
        pass
    return None


def load_auth():
    try:
        with open(AUTH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


# ─── Sondas de proveedores ───
def probe_nous(model, timeout=40):
    """HTTP 200 = vivo. Devuelve (ok, detalle)."""
    auth = load_auth()
    nous = auth.get("providers", {}).get("nous", {})
    token = nous.get("agent_key") or nous.get("access_token")
    base = nous.get("inference_base_url", "https://inference-api.nousresearch.com/v1")
    if not token:
        return False, "sin token nous en auth.json"
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": "Di: ok"}],
        "max_tokens": 300,
    }).encode("utf-8")
    req = urllib.request.Request(
        base.rstrip("/") + "/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            r.read()
        return True, "HTTP 200"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, type(e).__name__


def probe_gemini(model, timeout=30):
    key = read_env_var("GOOGLE_API_KEY") or read_env_var("GEMINI_API_KEY")
    if not key or not key.startswith("AQ.") and not key.startswith("AIza"):
        if not key:
            return False, "sin GOOGLE_API_KEY en .env"
    payload = json.dumps({"contents": [{"parts": [{"text": "Di: ok"}]}]}).encode("utf-8")
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            r.read()
        return True, "HTTP 200"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, type(e).__name__


def probe(provider, model):
    if provider == "nous":
        return probe_nous(model)
    if provider in ("gemini", "google"):
        return probe_gemini(model)
    return False, "proveedor sin sonda"


# ─── Configuración del modelo ───
def read_model_config():
    if yaml is None or not os.path.isfile(CONFIG):
        return None, None
    try:
        with open(CONFIG, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        m = cfg.get("model", {}) if isinstance(cfg, dict) else {}
        return m.get("provider"), m.get("default")
    except Exception:
        return None, None


def write_model_config(provider, model):
    """Respalda config.yaml y cambia el modelo primario. Devuelve bool."""
    if yaml is None:
        return False
    try:
        bak = CONFIG + ".bak-" + datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.copy2(CONFIG, bak)
        with open(CONFIG, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        cfg.setdefault("model", {})
        cfg["model"]["provider"] = provider
        cfg["model"]["default"] = model
        if provider != "custom":
            cfg["model"]["base_url"] = ""
            cfg["model"]["api_key"] = ""
            cfg["model"]["api_mode"] = ""
            cfg["model"]["local_gguf"] = ""
        with open(CONFIG, "w", encoding="utf-8") as f:
            yaml.safe_dump(cfg, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return True
    except Exception:
        return False


def end_to_end_test(timeout=100):
    """Prueba real: abrir una sesión Hermes nueva y obtener respuesta."""
    try:
        r = subprocess.run(
            [HERMES, "chat", "-q", "Responde solo: ok"],
            capture_output=True, text=True, timeout=timeout,
            cwd=HOME,
        )
        out = (r.stdout or "") + (r.stderr or "")
        if "HTTP 4" in out or "not found" in out.lower() or "invalid api key" in out.lower():
            return False
        return r.returncode == 0
    except Exception:
        return False


# ─── Diagnóstico y reparación del modelo primario ───
def guardian_model():
    global repaired_something
    provider, model = read_model_config()
    if not provider or not model:
        say(ALERT, "config.yaml ilegible o sin modelo primario — revisión manual")
        return
    ok, detail = probe(provider, model)
    if ok:
        say(OKK, f"Modelo primario vivo: {provider}/{model}")
        return
    say(ALERT, f"Modelo primario CAÍDO: {provider}/{model} ({detail}) — buscando reemplazo…")
    for cand_provider, cand_model in FALLBACK_CANDIDATES:
        if (cand_provider, cand_model) == (provider, model):
            continue
        cok, cdetail = probe(cand_provider, cand_model)
        if cok:
            if write_model_config(cand_provider, cand_model):
                if end_to_end_test():
                    say(FIXED, f"Conmutado a {cand_provider}/{cand_model} y verificado end-to-end")
                    repaired_something = True
                    return
                else:
                    say(ALERT, f"{cand_provider}/{cand_model} pasó sonda pero falló end-to-end — sigo buscando")
            else:
                say(ALERT, "No pude escribir config.yaml — revisión manual")
                return
        else:
            say("·", f"Descartado {cand_provider}/{cand_model} ({cdetail})")
    say(ALERT, "NINGÚN candidato vivo — recargar créditos o añadir proveedor en .env")


# ─── Gateway ───
def guardian_gateway():
    global repaired_something
    try:
        r = subprocess.run([HERMES, "gateway", "status"],
                           capture_output=True, text=True, timeout=60)
        out = r.stdout or ""
        if "running" in out.lower() or "✓" in out:
            say(OKK, "Gateway corriendo")
            return
        say(ALERT, "Gateway detenido — intentando arrancar…")
        subprocess.run([HERMES, "gateway", "start"],
                       capture_output=True, text=True, timeout=90)
        r2 = subprocess.run([HERMES, "gateway", "status"],
                            capture_output=True, text=True, timeout=60)
        if "running" in (r2.stdout or "").lower() or "✓" in (r2.stdout or ""):
            say(FIXED, "Gateway reiniciado")
            repaired_something = True
        else:
            say(ALERT, "Gateway no arranca — ejecutar 'hermes gateway run' y leer logs")
    except Exception as e:
        say(ALERT, f"Gateway: no pude verificar ({type(e).__name__})")


# ─── Cron jobs con fallos ───
def guardian_cron():
    try:
        r = subprocess.run([HERMES, "cron", "list"],
                           capture_output=True, text=True, timeout=90)
        out = r.stdout or ""
        failures = re.findall(r"error:\s+(.{10,90}?)\s+\(\d+ failures?", out)
        if failures:
            for f in set(failures[:3]):
                say(ALERT, f"Cron con fallos: {f.strip()}")
        else:
            say(OKK, "Cron jobs sin fallos recurrentes")
    except Exception:
        say("·", "Cron: no pude listar (gateway puede estar ocupado)")


# ─── Disco ───
def guardian_disk():
    try:
        drive = os.path.splitdrive(HOME)[0] or "C:\\"
        u = shutil.disk_usage(drive)
        free_gb = u.free / (1024 ** 3)
        if free_gb < 10:
            say(ALERT, f"Disco {drive} con solo {free_gb:.1f} GB libres — limpiar")
        else:
            say(OKK, f"Disco {drive}: {free_gb:.0f} GB libres")
    except Exception:
        pass


# ─── Errores recientes en logs ───
def guardian_logs():
    logdir = os.path.join(HOME, "logs")
    if not os.path.isdir(logdir):
        return
    err_count = 0
    try:
        for name in os.listdir(logdir):
            if not name.endswith(".log"):
                continue
            path = os.path.join(logdir, name)
            try:
                if datetime.now().timestamp() - os.path.getmtime(path) > 86400 * 2:
                    continue  # solo logs activos
                with open(path, encoding="utf-8", errors="replace") as f:
                    tail = f.read()[-20000:]
                err_count += len(re.findall(r"\bERROR\b", tail))
            except OSError:
                continue
        if err_count > 30:
            say(ALERT, f"{err_count} errores en logs recientes — revisar {logdir}")
        else:
            say(OKK, f"Logs tranquilos ({err_count} errores recientes)")
    except Exception:
        pass


# ─── Procesos huérfanos (solo contar y reportar, nunca matar solo) ───
def guardian_processes():
    try:
        r = subprocess.run(["tasklist", "/FI", "IMAGENAME eq python.exe"],
                           capture_output=True, text=True, timeout=30)
        n_python = len(re.findall(r"python\.exe", r.stdout or ""))
        r2 = subprocess.run(["tasklist", "/FI", "IMAGENAME eq hermes.exe"],
                            capture_output=True, text=True, timeout=30)
        n_hermes = len(re.findall(r"hermes\.exe", r2.stdout or ""))
        total = n_python + n_hermes
        if total > 14:
            say(ALERT, f"{total} procesos python/hermes activos ({n_python}+{n_hermes}) — posible fuga; limpiar huérfanos conservando el gateway")
        else:
            say(OKK, f"Procesos bajo control ({total})")
    except Exception:
        pass


# ─── Reporte a Discord (canal #estado de la familia) ───
def discord_report():
    """Envía el reporte al canal #estado vía 'hermes send' (reutiliza las
    credenciales del gateway y esquiva bloqueos de red/Cloudflare)."""
    if not lines:
        return
    header = f"🛡️ **Guardián** — {now_str()}\n"
    body = header + "\n".join(lines)
    # Discord: máx 2000 chars por mensaje → dividir
    chunks = []
    rest = body
    while rest:
        chunks.append(rest[:1900])
        rest = rest[1900:]
    for i, chunk in enumerate(chunks):
        prefix = f"({i+1}/{len(chunks)}) " if len(chunks) > 1 else ""
        try:
            subprocess.run(
                [HERMES, "send", "-t", "discord:#estado", prefix + chunk],
                capture_output=True, timeout=60,
            )
        except Exception:
            return  # si Discord falla, el stdout ya lleva el reporte


# ─── Main ───
def main():
    if QUICK:
        # Vigilancia diaria del modelo: silencio absoluto si todo bien
        provider, model = read_model_config()
        if provider and model:
            ok, _ = probe(provider, model)
            if ok:
                sys.exit(0)  # stdout vacío = watchdog en silencio
        # algo anda mal → correr reparación completa y reportar
        guardian_model()
        guardian_gateway()
        if lines:
            print(f"🛡️ Guardián (rápido) — {now_str()}")
            for l in lines:
                print(l)
            discord_report()
        return

    # Modo completo semanal
    guardian_model()
    guardian_gateway()
    guardian_cron()
    guardian_disk()
    guardian_logs()
    guardian_processes()

    verdict = "REPARACIONES APLICADAS" if repaired_something else "SIN INCIDENCIAS GRAVES"
    print(f"🛡️ GUARDIÁN SEMANAL — {now_str()} — {verdict}")
    for l in lines:
        print(l)
    print("— Familia Evergarden · Protocolo Guardián v1.0 —")
    discord_report()


if __name__ == "__main__":
    main()
