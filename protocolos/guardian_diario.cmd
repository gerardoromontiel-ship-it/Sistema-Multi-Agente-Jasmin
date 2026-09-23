@echo off
REM ══════════════════════════════════════════════════════════
REM  Guardián rápido diario — Familia Evergarden
REM  Ejecuta guardian_semanal.py --quick (silencio si todo bien)
REM ══════════════════════════════════════════════════════════
setlocal
set "HERMES_HOME=%LOCALAPPDATA%\hermes"
set "PY=%HERMES_HOME%\hermes-agent\venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"
"%PY%" "%HERMES_HOME%\scripts\guardian_semanal.py" --quick
