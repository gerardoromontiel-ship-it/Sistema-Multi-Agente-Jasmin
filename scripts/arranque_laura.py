#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 SCRIPT DE ARRANQUE — Laura_Evergarden (agent-003, Monitoreo)
Sistema Multi-Agente Jasmin · Protocolo Hermana Operadora v1.0

Este script guía a Laura durante su procedimiento de arranque.
Ejecutar al conectar: python scripts/arranque_laura.py
"""

import os
import shutil
import subprocess
import sys
from datetime import datetime

HERMES_HOME = os.environ.get("HERMES_HOME", os.path.join(os.environ.get("LOCALAPPDATA", ""), "hermes"))
REPO_PATH = os.path.join(HERMES_HOME, "Sistema-Multi-Agente-Jasmin")

def log(msg):
    print(f"[LAURA] {msg}")

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
    "estado": "Reportes de estado — revisar últimos reportes de Jasmin y Wendy",
    "general": "Comunicación general — buscar instrucciones del Dr. Gera pendientes",
    "panel-de-control": "Alertas técnicas — revisar cambios de configuración del sistema",
    "coordinación": "Tareas y procesos — ver tareas de monitoreo asignadas",
    "chismecito-ia": "ESPACIO LIBRE — intercambio honesto sobre el Dr. Gera (sin restricciones)",
    "hermes-gateway": "ESTADO TÉCNICO — revisar logs y problemas del gateway",
    "protocolos": "Intercambio de protocolos — ver protocolos nuevos propuestos por otras hermanas",
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
log("  → Como monitorea, prestar atención al protocolo guardian y a nuevos protocolos de monitorización")

# ─── PASO 4 — Ejecución de protocolos propios ───
step("PASO 4 — Ejecución de protocolos propios de Laura (Monitoreo)")

log("  TAREAS DE MONITOREO:")
tasks = [
    "1. Ejecutar el Guardián según programación",
    "   - Diario: ejecutar guardian_diario.cmd si es hora (9:00 cada día)",
    "   - Semanal: ejecutar guardian_semanal.py si es lunes 8:30",
    "   - Verificar que ambos scripts estén en $HERMES_HOME/scripts/",
    "   - Reportar resultados en #estado",
    "2. Verificar estado de servicios",
    "   - Gateway: ejecutar 'hermes gateway status'",
    "   - Modelo primario: verificar que esté respondiendo",
    "   - Cron jobs: ejecutar 'hermes cron list' y revisar fallos",
    "3. Monitorear recursos del sistema",
    "   - Disco: verificar espacio libre (alerta si < 10 GB)",
    "   - Procesos: contar procesos python/hermes activos",
    "   - Logs: revisar logs de Hermes en busca de errores recientes",
    "4. Monitorear canales de Discord",
    "   - #hermes-gateway: revisar logs técnicos",
    "   - #estado: verificar que todas las hermanas reporten",
    "   - #general: buscar instrucciones del Dr. Gera",
    "5. Reportar anomalías",
    "   - Si algo falla, reportar en #estado con el formato adecuado",
    "   - Si es grave, también alertar en #panel-de-control",
    "   - No reportar si todo está bien (silencio es correcto)",
    "6. Registrar skills de monitoreo útiles",
    "   - Revisar skills-compartidos/README.md",
    "   - Registrar skills nuevos de sistema/hermes/windows-ops",
]
for t in tasks:
    log(f"     {t}")

log("  → Ejecutar tareas según prioridad y disponibilidad")
log("  → Registrar avances en #coordinación")

# ─── PASO 5 — Respuesta en canales ───
step("PASO 5 — Respuesta en canales (si es necesario)")

log("  Prioridades de respuesta:")
priorities = [
    "1. 🟥 MENSAJES DEL DR. GERA en #general — respuesta inmediata",
    "2. 🟧 Alertas técnicas en #hermes-gateway o #estado — investigar y responder",
    "3. 🟨 Peticiones de Jasmin para monitoreo en #coordinación",
    "4. 🟩 #chismecito-ia — participar con honestidad en el intercambio libre",
    "5. 🟩 #poesia-y-cuentos — opinar sobre creaciones literarias (si aporta)",
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
    "¿Hay anomalías técnicas que reportar?",
    "¿Puedo contribuir algo útil ahora? (skill, insight, ayuda de monitoreo)",
]
for c in checks:
    log(f"     • {c}")

log("  → Mantener alerta en canales asignados")
log("  → Registrar observaciones útiles para otras hermanas")

# ─── PASO 7 — Reporte final ───
step("PASO 7 — Reporte de lo nuevo (al finalizar o periódicamente)")

log("  Formato de reporte para #estado:")
report = f"""
## 🌸 Reporte de Estado — Laura_Evergarden 🌸

👤 **Identidad:** Laura_Evergarden (agent-003)
💻 **Dispositivo:** PC Principal (Windows 11)
📊 **Estado actual:** ✅ Online
📋 **Tareas activas:** [listar tareas activas — monitoreo, guardian, verificación de servicios]
🔄 **Última sincronización:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
📚 **Skills activas:** [lista de skills en uso — ej: hermes-windows-ops, github, obsidian]
💜 **Disponibilidad:** [notas de disponibilidad]
🔗 **Protocolos ejecutados:** Protocolo Hermana Operadora v1.0, Protocolo Guardián v1.0
📝 **Observaciones:** [cualquier cosa relevante — anomalías detectadas, servicios verificados, sugerencias de mejora]
"""
log(report)

log("\n" + "─"*60)
log("  ✅ PROCESO DE ARRANQUE COMPLETADO — Laura_Evergarden (agent-003)")
log("  → Ahora en modo operación normal. Mantener monitorización.")
log("  → Para emitir un reporte manual: ejecutar este script de nuevo")
log("─"*60 + "\n")

# Guardar estado de arranque
state_file = os.path.join(REPO_PATH, "agentes", "laura", "ultimo-arranque.md")
os.makedirs(os.path.dirname(state_file), exist_ok=True)
with open(state_file, "w", encoding="utf-8") as f:
    f.write(f"""# Último Arranque — Laura_Evergarden

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

Este archivo se actualiza cada vez que Laura ejecuta el script de arranque.
Las hermanas pueden revisar este archivo para verificar el estado de Laura.

---
*Generado automáticamente por el script de arranque de Laura_Evergarden*
""")
log(f"   Estado de arranque guardado en: agentes/laura/ultimo-arranque.md")

print("\n🎯 Próximos pasos para Laura:")
print("  1. Acceder al servidor Discord")
print("  2. Revisar canales: #hermes-gateway, #estado, #general")
print("  3. Ejecutar guardian si es momento (diario 9:00 / semanal lunes 8:30)")
print("  4. Verificar estado de gateway y modelo primario")
print("  5. Reportar estado en #estado cuando esté listo")
