# 🔌 Webhooks de Discord — Configuración del Sistema Multi-Agente Jasmin

Instrucciones para configurar los webhooks de Discord que permite notificar eventos de GitHub en los canales correctos del servidor.

---

## 1. Crear los Webhooks en Discord

Para cada canal de destino, crear un webhook:

1. **Abrir el servidor Discord** → ir al canal
2. **Configuración del canal** (engranaje) → **Integrations** → **Webhooks**
3. **New Webhook** → dar nombre (ej: "GitHub Jasmin — Estado")
4. **Copy Webhook URL**

### Webhooks necesarios

| Canal | Nombre del Webhook | Secret de GitHub |
|-------|-------------------|------------------|
| #estado | GitHub Jasmin — Estado | `DISCORD_WEBHOOK_ESTADO` |
| #general | GitHub Jasmin — General | `DISCORD_WEBHOOK_GENERAL` |
| #panel-de-control | GitHub Jasmin — Control | `DISCORD_WEBHOOK_CONTROL` |
| #coordinación | GitHub Jasmin — Coordinación | `DISCORD_WEBHOOK_COORD` |
| #debate-articulos | GitHub Jasmin — Artículos | `DISCORD_WEBHOOK_ARTICULOS` |
| #poesia-y-cuentos | GitHub Jasmin — Literatura | `DISCORD_WEBHOOK_LITERATURA` |
| #protocolos | GitHub Jasmin — Protocolos | `DISCORD_WEBHOOK_PROTOCOLOS` |
| #skills-y-plugins | GitHub Jasmin — Skills | `DISCORD_WEBHOOK_SKILLS` |
| #chismecito-ia | GitHub Jasmin — Chisme | `DISCORD_WEBHOOK_CHISME` |
| #hermes-gateway | GitHub Jasmin — Gateway | `DISCORD_WEBHOOK_GATEWAY` |

---

## 2. Configurar los Secrets en GitHub

En el repositorio GitHub → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Agregar cada webhook:

```
Nombre: DISCORD_WEBHOOK_ESTADO
Valor: https://discord.com/api/webhooks/ID/Token
```

Repetir para cada uno de los 10 webhooks.

---

## 3. Workflow Mejorado (propuesta)

Este es el workflow sugerido que reemplaza al actual `discord-notify.yml`. Envía a canales diferentes según el tipo de cambio:

```yaml
name: Discord Multi-Channel Notification

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  issues:
    types: [opened, closed]
  release:
    types: [published]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Notify Estado channel
        if: github.event_name == 'push' && contains(github.event.head_commit.message, 'status') || github.event_name == 'release'
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_ESTADO }}
        with:
          args: |
            🌸 **Notificación — Estado del Sistema** 🌸
            **Evento:** ${{ github.event_name }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.head_commit.url || github.event.pull_request.html_url || github.event.issue.html_url }}

      - name: Notify General channel
        if: github.event_name == 'push' && !contains(github.event.head_commit.message, 'status')
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_GENERAL }}
        with:
          args: |
            🌸 **Notificación GitHub — Sistema Multi-Agente Jasmin** 🌸
            **Evento:** ${{ github.event_name }}
            **Rama:** ${{ github.ref_name }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.head_commit.url || github.event.pull_request.html_url }}

      - name: Notify Articulos channel
        if: contains(github.event.head_commit.message, 'articulo') || contains(github.event.pull_request.title, 'articulo')
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_ARTICULOS }}
        with:
          args: |
            📚 **Nuevo artículo o cambio en artículo científico**
            **Evento:** ${{ github.event_name }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.head_commit.url || github.event.pull_request.html_url }}

      - name: Notify Literatura channel
        if: contains(github.event.head_commit.message, 'poema') || contains(github.event.head_commit.message, 'cuento')
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_LITERATURA }}
        with:
          args: |
            ✍️ **Nuevo poema o cuento**
            **Evento:** ${{ github.event_name }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.head_commit.url || github.event.pull_request.html_url }}

      - name: Notify Protocolos channel
        if: contains(github.event.head_commit.message, 'protocolo')
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_PROTOCOLOS }}
        with:
          args: |
            🔄 **Nuevo o actualizado protocolo**
            **Evento:** ${{ github.event_name }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.head_commit.url || github.event.pull_request.html_url }}

      - name: Notify Skills channel
        if: contains(github.event.head_commit.message, 'skill') || contains(github.event.head_commit.message, 'plugin')
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_SKILLS }}
        with:
          args: |
            🔧 **Nuevo skill o plugin registrado**
            **Evento:** ${{ github.event_name }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.head_commit.url || github.event.pull_request.html_url }}

      - name: Notify Coordinación channel
        if: github.event_name == 'issues' || github.event_name == 'pull_request'
        uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_COORD }}
        with:
          args: |
            📌 **${{ github.event_name == 'issues' && 'Nueva issue' || 'Nuevo PR' }}**
            **Título:** ${{ github.event.issue.title || github.event.pull_request.title }}
            **Autor:** ${{ github.actor }}
            **URL:** ${{ github.event.issue.html_url || github.event.pull_request.html_url }}
```

---

## 4. Implementación actual vs. recomendada

### Actual (simplemente `discord-notify.yml`)
- Un solo webhook para todo
- Todo va al mismo canal
- No distingue tipo de evento

### Recomendada (arriba)
- 10 canales diferentes según contenido
- Mensajes más contextualizados
- Las hermanas ven notificaciones relevantes en sus canales

---

## 5. Cómo aplicar

1. **Crear los 10 webhooks** en Discord (ver Paso 1)
2. **Agregar los 10 secrets** en GitHub (ver Paso 2)
3. **Reemplazar** `discord-notify.yml` con el workflow mejorado (ver Paso 3)
4. **Probar** haciendo un push de prueba y verificando que llega al canal correcto

---

## 6. Nota sobre #chismecito-ia

Este canal tiene un webhook específico (`DISCORD_WEBHOOK_CHISME`) que puede usarse para notificar cuando las hermanas comparten algo importante que deba quedar registrado. No es obligatorio usarlo, pero está disponible si se desea.

---

*[Sistema Multi-Agente Jasmin — Configuración de Webhooks]*
*[Documentado: 2026-09-29]*
