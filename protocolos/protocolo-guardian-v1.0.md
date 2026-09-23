# 🛡️ PROTOCOLO GUARDIÁN v1.0 — Familia Evergarden

**Fecha:** 2026-09-23 · **Autora:** Cortana Evergarden (N03) · **Aprobado por:** Dr. Gera

---

## 1. Qué es

Un protocolo de **diagnóstico y auto-reparación** para cada máquina de la familia
Evergarden. Corre periódicamente, busca errores del PC y de Hermes, repara lo
reparable, y **si el modelo de IA no sirve o no tiene créditos, reporta y conmuta
automáticamente a un modelo vivo**.

**Primer rescate real (2026-09-23):** el modelo `hermes-4` murió (HTTP 404) y dejó
6 fallos seguidos en el cron de monitoreo. El Guardián lo detectó, conmutó a
`meituan/longcat-2.0:free` (verificado end-to-end) y restauró todos los servicios.

## 2. Arquitectura

```
Windows Task Scheduler (o cron de Hermes)
    │
    ├── DIARIO (guardian_diario.cmd → --quick)
    │     Sonda el modelo primario + gateway.
    │     Todo bien → SILENCIO (nada notifica).
    │     Algo caído → repara + reporta a #estado.
    │
    └── SEMANAL (guardian_semanal.py, modo completo)
          Diagnóstico integral SIEMPRE visible:
          · Modelo primario (sonda real de inferencia)
          · Gateway (y auto-arranque si está caído)
          · Cron jobs con fallos recurrentes
          · Espacio en disco
          · Errores en logs de Hermes
          · Procesos python/hermes huérfanos
          → Reporte completo a #estado (Discord)
```

## 3. Conmutación automática de modelos

Cuando el modelo primario falla (404 no existe, 401/403 credenciales, 402/429 sin
créditos, timeouts), el Guardián recorre EN ORDEN esta cadena de candidatos
(verificados vivos el 2026-09-23):

| # | Proveedor | Modelo | Estado (2026-09-23) |
|---|-----------|--------|---------------------|
| 1 | nous | `meituan/longcat-2.0:free` | ✅ vivo |
| 2 | nous | `stepfun/step-3.7-flash:free` | ✅ vivo |
| 3 | nous | `upstage/solar-pro4:free` | ✅ vivo |
| 4 | nous | `inclusionai/ling-3.0-flash-sante:free` | ✅ vivo |
| 5 | nous | `poolside/laguna-s-2.1:free` | ✅ vivo |
| 6 | gemini | `gemini-2.5-flash` | ✅ vivo (GOOGLE_API_KEY) |
| 7 | gemini | `gemini-flash-latest` | ✅ vivo |
| 8 | gemini | `gemini-2.5-flash-lite` | ✅ vivo |

**Proveedores agotados (reportados, no en la cadena):** openrouter (402), xai/grok
(402), openai sk-proj (429), nous-modelos-pagados (sin créditos).

Reglas de conmutación:
1. Sonda cada candidato con una petición real de inferencia (no solo ping).
2. El primer candidato vivo se instala como modelo primario (con respaldo del
   config.yaml).
3. **Verificación end-to-end obligatoria:** abre una sesión Hermes real
   (`hermes chat -q`) y exige respuesta. Si falla, sigue buscando.
4. Reporta la conmutación a **#estado** con 🔧 y al usuario en su chat.
5. Si NINGÚN candidato vive: reporta 🚨 y pide recargar créditos o añadir
   proveedor al `.env`.

Adicionalmente, Hermes tiene **fallback nativo en vivo** (`fallback_providers` en
config.yaml): si el primario falla a mitad de conversación, conmuta al instante
sin perder contexto. Actual: `gemini/gemini-2.5-flash`.

## 4. Instalación en cada nodo de la familia

**Requisitos:** Windows con Hermes instalado y Python del venv de Hermes.

```powershell
# 1. Copiar el guardián (desde el repo Sistema-Multi-Agente-Jasmin)
Copy-Item .\guardian_semanal.py $env:LOCALAPPDATA\hermes\scripts\
Copy-Item .\guardian_diario.cmd $env:LOCALAPPDATA\hermes\scripts\

# 2. Programar el diario (9:00 cada día) y el semanal (lunes 8:30)
schtasks /create /tn "Hermes_Guardian_Diario" /tr "$env:LOCALAPPDATA\hermes\scripts\guardian_diario.cmd" /sc daily /st 09:00
schtasks /create /tn "Hermes_Guardian_Semanal" /tr "\"$env:LOCALAPPDATA\hermes\hermes-agent\venv\Scripts\python.exe\" $env:LOCALAPPDATA\hermes\scripts\guardian_semanal.py" /sc weekly /d MON /st 08:30
```

En Linux/macOS (nodos futuros): usar el cron de Hermes con `script=` apuntando al
mismo `guardian_semanal.py` (es portátil: auto-detecta HERMES_HOME, resuelve el
binario `hermes` del venv o PATH, y reporta vía `hermes send`).

## 4.1 Programación vía cron de Hermes (alternativa en cualquier SO)

```bash
# Diario silencioso (watchdog): solo notifica si algo se rompió
hermes cron create --name "Guardián rápido" --schedule "daily 09:00" \
  --script guardian_semanal.py --quick --no-agent

# Semanal completo: reporte integral siempre visible en #estado
hermes cron create --name "Guardián semanal" --schedule "weekly monday 08:30" \
  --script guardian_semanal.py --no-agent
```

> **Nota:** el script es autónomo (no necesita agente). Con `--no-agent`, el
> stdout ES el mensaje: vacío = silencio de watchdog; contenido = reporte.

## 4.2 Verificación de instalación

```powershell
# Probar ambos modos a mano
& $env:LOCALAPPDATA\hermes\scripts\guardian_diario.cmd        # debe callar si todo bien
& $env:LOCALAPPDATA\hermes\hermes-agent\venv\Scripts\python.exe $env:LOCALAPPDATA\hermes\scripts\guardian_semanal.py
```

## 5. Seguridad

- **Nunca imprime tokens ni secretos** — solo estados (✅/⚠️/🚨/🔧).
- Respaldos automáticos de `config.yaml` antes de cada reparación
  (`config.yaml.bak-AAAAMMDD_HHMM`).
- Nunca mata procesos por su cuenta: solo reporta fugas de procesos.
- **Reporta pero no compra:** si todo está sin créditos, pide al Dr. Gera
  recargar o añadir proveedor. El protocolo no gasta dinero por sí solo.

## 6. Manual de la hermana operadora (para JAS, Wendy, Laura)

Cuando el Guardián reporte 🚨 en #estado:

1. **"Modelo primario CAÍDO … Conmutado a X"** → ya resuelto; verificar que el
   chat del usuario responde.
2. **"NINGÚN candidato vivo"** → escalar al Dr. Gera: necesita recargar créditos
   (Nous Portal / OpenRouter / xAI) o añadir una nueva API key en `.env`.
3. **"Gateway no arranca"** → leer `logs/gateway.log` (últimas 50 líneas),
   revisar tokens en `.env`, ejecutar `hermes gateway run` en foreground.
4. **"Cron con fallos"** → `hermes cron runs <job_id>` para ver el error exacto.
5. **"Disco < 10 GB"** → limpiar `cache/`, `sessions/` viejas, papelera.
6. **"Procesos > 14"** → limpiar huérfanos conservando el gateway activo
   (ver skill hermes-windows-ops, sección procesos huérfanos).

## 7. Estado de los proveedores (auditoría 2026-09-23)

| Proveedor | Estado | Detalle |
|-----------|--------|---------|
| nous OAuth | ✅ vivo (free) | modelos free funcionan; pagados sin créditos |
| gemini (GOOGLE_API_KEY) | ✅ vivo | gemini-2.5-flash verificado con chat real |
| openai-codex OAuth | ✅ sesión activa | backend chatgpt.com (no probeable directo por Cloudflare) |
| openrouter | ❌ sin créditos | HTTP 402 |
| xai/grok OAuth | ❌ sin créditos | HTTP 402 spending-limit |
| openai sk-proj | ❌ sin créditos | HTTP 429 insufficient_quota |
| copilot (GitHub) | ⚠️ sin validar | token presente, API rechazó sonda directa |

## 8. Bitácora

| Fecha | Evento |
|-------|--------|
| 2026-09-23 | v1.0 creada tras muerte de `hermes-4` (404). Conmutación a `meituan/longcat-2.0:free` verificada end-to-end. Fallback nativo instalado: `gemini/gemini-2.5-flash`. Primer reporte semanal enviado a #estado. |
