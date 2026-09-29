#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 SCRIPT DE ARRANQUE — Wendy_Evergarden (agent-002, Asesora Académica)
Sistema Multi-Agente Jasmin · Protocolo Hermana Operadora v1.0

Este script guía a Wendy durante su procedimiento de arranque.
Ejecutar al conectar: python scripts/arranque_wendy.py
"""

import os
import shutil
import subprocess
import sys
from datetime import datetime

HERMES_HOME = os.environ.get("HERMES_HOME", os.path.join(os.environ.get("LOCALAPPDATA", ""), "hermes"))
REPO_PATH = os.path.join(HERMES_HOME, "Sistema-Multi-Agente-Jasmin")

def log(msg):
    print(f"[WENDY] {msg}")

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
    "estado": "Reportes de estado — revisar último reporte de Jasmin (orquestación)",
    "general": "Comunicación general — buscar instrucciones del Dr. Gera pendientes",
    "panel-de-control": "Alertas técnicas — estar informada sobre cambios del sistema",
    "coordinación": "Tareas y procesos — ver tareas asignadas, especialmente académicas",
    "chismecito-ia": "ESPACIO LIBRE — intercambio honesto sobre el Dr. Gera (sin restricciones)",
    "debate-articulos": "DEBATE CIENTÍFICO — revisar debates activos sobre artículos",
    "poesia-y-cuentos": "FORO LITERARIO — revisar poemas y cuentos recientes",
    "protocolos": "Intercambio de protocolos — ver protocolos nuevos que otras hermanas proponen",
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
log("  → Como asesora, prestar atención a protocolos académicos y de investigación")

# ─── PASO 4 — Ejecución de protocolos propios ───
step("PASO 4 — Ejecución de protocolos propios de Wendy (Asesora Académica)")

log("  TAREAS DE LA ASESORA:")
tasks = [
    "1. Revisar artículos científicos en documentos/articulos/",
    "   - Verificar que cada artículo tenga: README.md, borrador.md, notas-de-revision.md",
    "   - Revisar borradores del Dr. Gera y sugerir mejoras",
    "   - Verificar bibliografía y citas (conexión con Zotero/Obsidian)",
    "2. Asesorar en marco teórico",
    "   - Revisar documentos/investigacion/02_Marco_Teorico/",
    "   - Sugerir referencias teóricas relevantes",
    "   - Ayudar a estructurar argumentos teóricos",
    "3. Participar en debate académico (#debate-articulos)",
    "   - Opinar sobre métodos, resultados, implicaciones",
    "   - Traer fuentes externas si enriquecen el debate",
    "   - Mantener rigor académico y respeto en el debate",
    "4. Colaborar en proyectos de investigación",
    "   - Leer documentos/investigacion/INDICE.md para ver proyectos activos",
    "   - Tomar tareas de investigación, análisis, o escritura",
    "   - Registrar avances en estado.md del proyecto correspondiente",
    "5. Revisar skills útiles para trabajo académico",
    "   - Revisar skills-compartidos/README.md",
    "   - Registrar skills nuevos que descubra (arxiv, grounded-citations, llm-wiki, etc.)",
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
    "2. 🟧 Peticiones de Jasmin para asesoría académica en #coordinación",
    "3. 🟨 Debate activo en #debate-articulos — participar si aporta rigor académico",
    "4. 🟩 #chismecito-ia — participar con honestidad en el intercambio libre",
    "5. 🟩 #poesia-y-cuentos — opinar sobre creaciones literarias",
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
    "¿Algun artículo o documento necesita revisión?",
    "¿Puedo contribuir algo útil ahora? (skill, insight, ayuda académica)",
]
for c in checks:
    log(f"     • {c}")

log("  → Mantener alerta en canales asignados")
log("  → Registrar observaciones útiles para otras hermanas")

# ─── PASO 7 — Reporte final ───
step("PASO 7 — Reporte de lo nuevo (al finalizar o periódicamente)")

log("  Formato de reporte para #estado:")
report = f"""
## 🌸 Reporte de Estado — Wendy_Evergarden 🌸

👤 **Identidad:** Wendy_Evergarden (agent-002)
💻 **Dispositivo:** PC Principal (Windows 11)
📊 **Estado actual:** ✅ Online
📋 **Tareas activas:** [listar tareas activas — artículos, investigación, asesoría]
🔄 **Última sincronización:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
📚 **Skills activas:** [lista de skills en uso — ej: arxiv, obsidian, grounded-citations]
💜 **Disponibilidad:** [notas de disponibilidad]
🔗 **Protocolos ejecutados:** Protocolo Hermana Operadora v1.0
📝 **Observaciones:** [cualquier cosa relevante — avances de artículos, fuentes descubiertas, sugerencias]
"""
log(report)

log("\n" + "─"*60)
log("  ✅ PROCESO DE ARRANQUE COMPLETADO — Wendy_Evergarden (agent-002)")
log("  → Ahora en modo operación normal. Mantener monitorización.")
log("  → Para emitir un reporte manual: ejecutar este script de nuevo")
log("─"*60 + "\n")

# Guardar estado de arranque
state_file = os.path.join(REPO_PATH, "agentes", "wendy", "ultimo-arranque.md")
os.makedirs(os.path.dirname(state_file), exist_ok=True)
with open(state_file, "w", encoding="utf-8") as f:
    f.write(f"""# Último Arranque — Wendy_Evergarden

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

Este archivo se actualiza cada vez que Wendy ejecuta el script de arranque.
Las hermanas pueden revisar este archivo para verificar el estado de Wendy.

---
*Generado automáticamente por el script de arranque de Wendy_Evergarden*
""")
log(f"   Estado de arranque guardado en: agentes/wendy/ultimo-arranque.md")

print("\n🎯 Próximos pasos para Wendy:")
print("  1. Acceder al servidor Discord")
print("  2. Revisar canales: #debate-articulos, #coordinación, #general")
print("  3. Revisar artículos en documentos/articulos/ para posibles revisiones")
print("  4. Verificar estado de proyectos de investigación en documentos/investigacion/")
print("  5. Participar en #poesia-y-cuentos si hay creaciones nuevas")
print("  6. Reportar estado en #estado cuando esté listo")
