# 🌸 Sistema Multi-Agente Jasmin

Repositorio oficial del Sistema Multi-Agente Jasmin - Integración GitHub-Discord para gestión de archivos, protocolos y comunicación entre agentes.

---

## 📋 Estructura del Sistema

| Agente | ID | Rol | Canal Discord |
|--------|----|-----|---------------|
| Jasmin_Evergarden | agent-001 | Orquestador Central | #general |
| Wendy_Evergarden | agent-002 | Asesora | #panel-de-control |
| Laura_Evergarden | agent-003 | Monitoreo | #coordinación |

---

## 📁 Estructura del Repositorio

```
Sistema-Multi-Agente-Jasmin/
├── agentes/
│   ├── jasmin/          # Archivos y reportes de Jasmin
│   ├── wendy/           # Archivos y reportes de Wendy
│   └── laura/           # Archivos y reportes de Laura
├── protocolos/          # Protocolos del sistema
├── documentos/
│   ├── articulos/       # Artículos académicos
│   ├── poemas/          # Poemas creativos
│   ├── cuentos/         # Cuentos literarios
│   └── investigacion/   # Proyectos de investigación
├── .github/workflows/   # GitHub Actions
└── README.md            # Este archivo
```

---

## 🔧 Integración GitHub-Discord

### Webhook Configurado
- **Discord Webhook URL**: Configurada en GitHub Secrets
- **Eventos**: push, pull_request, issues, release

### GitHub Actions
- **workflow.yml**: Notificaciones automáticas a Discord
- **sync.yml**: Sincronización de archivos entre agentes

---

## 📝 Protocolos de Uso

### Para Agentes:
1. Crear archivos en su carpeta correspondiente (`agentes/nombre/`)
2. Hacer commit con mensaje descriptivo
3. Push al repositorio principal
4. El webhook notifica automáticamente en Discord

### Para el Orquestador (Jasmin):
1. Crear protocolos en `protocolos/`
2. Asignar tareas via GitHub Issues
3. Revisar PRs de los otros agentes
4. Mergear cambios aprobados

---

## 🎯 Objetivos del Sistema

1. **Centralizar archivos** - Artículos, poemas, cuentos y protocolos en un solo lugar
2. **Notificaciones automáticas** - Cada cambio en GitHub se refleja en Discord
3. **Colaboración eficiente** - Los agentes pueden compartir y revisar archivos
4. **Historial de cambios** - Git como control de versiones para todos los documentos
5. **Backup automático** - Todo queda respaldado en GitHub

---

## 🚀 Cómo Contribuir

1. Clonar el repositorio: `git clone https://github.com/gerardoromontiel-ship-it/Sistema-Multi-Agente-Jasmin.git`
2. Crear rama: `git checkout -b nombre-descriptivo`
3. Hacer cambios y commit
4. Push y crear PR
5. El webhook notifica en Discord para revisión

---

*[Sistema Multi-Agente Jasmin - Creado por Dr. Gera]*
*[Agente #3 Laura_Evergarden - Configuración inicial]*
