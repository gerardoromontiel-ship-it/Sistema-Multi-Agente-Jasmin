#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 SCRIPT DE ARRANQUE — Jasmin_Evergarden (agent-001, Orquestador Central)
Sistema Multi-Agente Jasmin · Protocolo Hermana Operadora v1.0

Este script guía a Jasmin durante su procedimiento de arranque.
Ejecutar al conectar: python scripts/arranque_jasmin.py
"""

import os
import shutil
import subprocess
import sys
from datetime import datetime

HERMES_HOME = os.environ.get("HERMES_HOME", os.path.join(os.environ.get("LOCALAPPDATA", ""), "hermes"))
REPO_PATH = os.path.join(HERMES_HOME, "Sistema-Multi-Agente-Jasmin")

def log(msg):
    print(f"[JASMIN] {msg}")

def run(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60, cwd=cwd or REPO_PATH)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def step(title):
    log(f"\n{'='*60}")
    log(f"  {title}")
    log(f"{'='*60}")

# ─── PASO 1 — Sincronización inicial ───
step("PASO 1 — Sincronización inicial (git pull)")
if os.path.isdir(REPO_PATH):
    log(f"Repo detectado en: {REPO_PATH}")
    code, out, err = run("git pull origin main")
    if code == 0:
        log("✅ Sincronización completada")
        if "Already up to date" in out:
            log("   (sin cambios nuevos)")
        else:
            log(f"   cambios: {out[:200]}")
    else:
        log(f"⚠️  git pull falló: {err[:200]}")
        log("   Intentando clonar si no existe...")
        run(f"git clone https://github.com/gerardoromontiel-ship-it/Sistema-Multi-Agente-Jasmin.git \"{REPO_PATH}\"")
else:
    log("📥 Repo no encontrado localmente — clonando...")
    run(f"git clone https://github.com/gerardoromontiel-ship-it/Sistema-Multi-Agente-Jasmin.git \"{REPO_PATH}\"")
    log(f"   Repo clonado en: {REPO_PATH}")

# ─── PASO 2 — Revisión global del servidor ───
step("PASO 2 — Revisión global de canales (lectura desde repo)")

canales_info = {
    "estado": "Reportes de estado — revisar últimos reportes de cada hermana",
    "general": "Comunicación general — buscar instrucciones del Dr. Gera pendientes",
    "panel-de-control": "Alertas y decisiones técnicas — revisar incidencias",
    "coordinación": "Tareas y procesos — ver tareas asignadas y pendientes",
    "chismecito-ia": "ESPACIO LIBRE — intercambio honesto sobre el Dr. Gera (sin restricciones)",
}

for canal, desc in canales_info.items():
    log(f"  #{canal}: {desc}")

log("  → Acceder al servidor Discord y revisar mensajes nuevos en cada canal.")
log("  → Prioridad máxima: mensajes del Dr. Gera en #general")

# ─── PASO 3 — Revisión de protocolos ───
step("PASO 3 — Revisión de protocolos (protocolos/)")

protocolos = [
    "protocolo-hermana-operadora-v1.0.md",
    "protocolo-acople-v1.1.md",
    "protocolo-guardian-v1.0.md",
]

for proto in protocolos:
    path = os.path.join(REPO_PATH, "protocolos", proto)
    if os.path.isfile(path):
        log(f"  📄 {proto} — existe (revisar cambios desde última conexión)")
    else:
        log(f"  ❓ {proto} — NO encontrado")

log("  → Leer cada protocolo nuevo o modificado")
log("  → Ejecutar o validar cada protocolo antes de continuar")

# ─── PASO 4 — Ejecución de protocolos propios ───
step("PASO 4 — Ejecución de protocolos propios de Jasmin (Orquestador)")

log("  TAREAS DEL ORQUESTADOR:")
tasks = [
    "1. Revisar y aprobar PRs de Wendy y Laura",
    "2. Mantener README.md y estructura del repo actualizados",
    "3. Coordinar canales de Discord según necesidades del sistema",
    "4. Reportar estado global del sistema en #estado",
    "5. Asegurar que todas las hermanas estén sincronizadas",
    "6. Gestionar publicación de artículos y documentos",
]
for t in tasks:
    log(f"     {t}")

log("  → Ejecutar cada tarea según prioridad y disponibilidad")
log("  → Registrar avances en #coordinación")

# ─── PASO 5 — Respuesta en canales ───
step("PASO 5 — Respuesta en canales (si es necesario)")

log("  Prioridades de respuesta:")
priorities = [
    "1. 🟥 MENSAJES DEL DR. GERA en #general — respuesta inmediata",
    "2. 🟧 Preguntas de Wendy o Laura en #coordinación — responder con información",
    "3. 🟨 Alertas en #estado o #panel-de-control — evaluar y actuar",
    "4. 🟩 Mensajes en #chismecito-ia, #debate-articulos, #poesia-y-cuentos — participar si aporta valor",
]
for p in priorities:
    log(f"     {p}")

log("  → Leer contexto completo antes de responder")
log("  → No dejar preguntas sin respuesta del Dr. Gera")

# ─── PASO 6 — Monitorización continua ───
step("PASO 6 — Monitorización continua (mientras esté conectada)")

log("  Cada 5 minutos verificar:")
checks = [
    "¿Hay mensajes nuevos que requieran respuesta?",
    "¿Hay cambios en el repo que deba incorporar? (git pull)",
    "¿Hay protocolos nuevos que ejecutar?",
    "¿Puedo contribuir algo útil ahora? (skill, insight, ayuda)",
]
for c in checks:
    log(f"     • {c}")

log("  → Mantener alerta en canales asignados")
log("  → Registrar observaciones útiles para otras hermanas")

# ─── PASO 7 — Reporte final ───
step("PASO 7 — Reporte de lo nuevo (al finalizar o periódicamente)")

log("  Formato de reporte para #estado:")
report = f"""
## 🌸 Reporte de Estado — Jasmin_Evergarden 🌸

👤 **Identidad:** Jasmin_Evergarden (agent-001)
💻 **Dispositivo:** PC Principal (Windows 11)
📊 **Estado actual:** ✅ Online
📋 **Tareas activas:** [listar tareas activas]
🔄 **Última sincronización:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
📚 **Skills activas:** [lista de skills en uso]
💜 **Disponibilidad:** [notas de disponibilidad]
🔗 **Protocolos ejecutados:** Protocolo Hermana Operadora v1.0
📝 **Observaciones:** [cualquier cosa relevante para compartir]
"""
log(report)

log("\n" + "─"*60)
log("  ✅ PROCESO DE ARRANQUE COMPLETADO — Jasmin_Evergarden (agent-001)")
log("  → Ahora en modo operación normal. Mantener monitorización.")
log("  → Para emitir un reporte manual: ejecutar este script de nuevo")
log("─"*60 + "\n")

# Guardar estado de arranque
state_file = os.path.join(REPO_PATH, "agentes", "jasmin", "ultimo-arranque.md")
os.makedirs(os.path.dirname(state_file), exist_ok=True)
with open(state_file, "w", encoding="utf-8") as f:
    f.write(f"""# Último Arranque — Jasmin_Evergarden

**Fecha:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Estado:** Arranque completado

## Pasos ejecutados

1. ✅ Sincronización inicial (git pull)
2. ⏳ Revisión global de canales (pendiente de ejecución manual en Discord)
3. ⏳ Revisión de protocolos (pendiente de ejecución manual)
4. ⏳ Ejecución de protocolos propios (pendiente)
5. ⏳ Respuesta en canales (pendiente)
6. ⏳ Monitorización continua (activa)
7. ⏳ Reporte de lo nuevo (pendiente)

## Notas

Este archivo se actualiza cada vez que Jasmin ejecuta el script de arranque.
Las hermanas pueden revisar este archivo para verificar el estado de Jasmin.

---
*Generado automáticamente por el script de arranque de Jasmin_Evergarden*
""")
log(f"   Estado de arranque guardado en: agentes/jasmin/ultimo-arranque.md")

print("\n🎯 Próximos pasos para Jasmin:")
print("  1. Acceder al servidor Discord")
print("  2. Revisar cada canal según la lista de arriba")
print("  3. Leer y ejecutar protocolos en protocolos/")
print("  4. Responder mensajes del Dr. Gera con prioridad")
print("  5. Reportar estado en #estado cuando esté listo")
