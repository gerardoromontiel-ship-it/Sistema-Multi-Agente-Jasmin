# 🚀 Workflow de Notificaciones de GitHub → Discord

**Propósito:** enviar notificaciones a Discord cuando algo sucede en el repo: push, PR, issue, release, o cambio en documentos importantes.

**Canales destino:**
- **#estado** — cambios en documentos de estado de agentes, protocolos críticos
- **#general** — push general, PRs, issues
- **#panel-de-control** — alertas técnicas, cambios de configuración

---

## Workflow actual: `discord-notify.yml`

- **Trigger:** push a main, PR a main, issues (abiertos/cerrados), releases
- **Acción:** usa `Ilshidur/action-discord@master` con el webhook del secret `DISCORD_WEBHOOK_URL`
- **Contenido:** emoji 🌸 + evento + rama + autor + URL

---

## Limitaciones actuales

1. **Un solo canal:** todo va al mismo webhook → todas las notificaciones van al mismo lugar
2. **Sin detalle de qué archivo cambió:** solo el commit, no qué documentos se vieron afectados
3. **No distingue categorías:** un cambio en `agentes/laura/status.md` va igual que un push deocumento investigación
4. **No hay modo silencio:** cada push notifica, aunque sea un cambio menor

---

## Mejoras sugeridas (futuras)

### 1. Notificaciones por categoría

Crear workflows separados o usar un solo workflow con conditionals para enviar a canales diferentes:

- Push a `agentes/*/status.md` → #estado
- Push a `protocolos/*` → #protocolos o #panel-de-control
- Push a `documentos/articulos/*` → #debate-articulos
- Push a `documentos/poemas/*` o `documentos/cuentos/*` → #poesia-y-cuentos
- Push a `documentos/investigacion/*` → #coordinación
- Cualquier otro push → #general

### 2. Contenido más informativo

Incluir en la notificación:
- Qué archivos cambiaron (`git diff --stat`)
- Resumen del cambio (mensaje de commit)
- Quién hizo el cambio
- Enlace al commit o PR

### 3. Modo silencio para cambios menores

Permitir que ciertos cambios (ej: actualización de índice, cambio de typo menor) no notifiquen, o notifiquen de forma resumida.

---

## Nota sobre el Webhook

El webhook actual está configurado en los **Secrets** del repositorio como `DISCORD_WEBHOOK_URL`. Si se necesitan múltiples canales, se pueden configurar múltiples secrets:

- `DISCORD_WEBHOOK_ESTADO`
- `DISCORD_WEBHOOK_GENERAL`
- `DISCORD_WEBHOOK_CONTROL`

Cada uno apuntando a un canal diferente de Discord.

---

*[Sistema Multi-Agente Jasmin — GitHub Actions]*
*[Documentado: 2026-09-29]*
