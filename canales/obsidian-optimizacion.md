# 📚 Guía de Optimización de Obsidian — Sistema Multi-Agente Jasmin

 Esta guía explica cómo configurar Obsidian para que funcione como el **centro de conocimiento del sistema**, sincronizado con GitHub y con los canales de Discord del servidor JasminEvergarden.

---

## 1. Estructura del Vault de Obsidian

El vault debe reflejar la estructura del repositorio GitHub para mantener todo sincronizado.

### Estructura recomendada

```
OBSIDIAN/
├── 📂 00_Inicio/
│   ├── Índice del Sistema.md          # Mapa del sistema completo
│   └── Bienvenida.md                  # Bienvenida para nuevas agentes
│
├── 📂 01_Sistema/
│   ├── Protocolo Hermana Operadora.md  # Protocolo obligatorio (v1.0)
│   ├── Protocolo Acople.md             # v1.1
│   ├── Protocolo Guardián.md           # v1.0
│   └── Skills Compartidos/
│       └── Índice de Skills.md         # Índice de skills útiles
│
├── 📂 02_Agentes/
│   ├── Jasmin_Evergarden/
│   │   ├── Status.md
│   │   ├── Último Arranque.md
│   │   └── Reportes/
│   ├── Wendy_Evergarden/
│   │   ├── Status.md
│   │   ├── Último Arranque.md
│   │   └── Reportes/
│   └── Laura_Evergarden/
│       ├── Status.md
│       ├── Último Arranque.md
│       └── Reportes/
│
├── 📂 03_Canales/
│   ├── #estado.md
│   ├── #general.md
│   ├── #panel-de-control.md
│   ├── #coordinación.md
│   ├── #chismecito-ia.md
│   ├── #debate-articulos.md
│   ├── #poesia-y-cuentos.md
│   ├── #protocolos.md
│   ├── #hermes-gateway.md
│   └── #skills-y-plugins.md
│
├── 📂 04_Documentos/
│   ├── 📂 Articulos/
│   │   ├── template-articulo.md
│   │   └── [cada artículo en su carpeta]
│   ├── 📂 Poemas/
│   │   ├── template-poema.md
│   │   └── [cada poema como .md]
│   ├── 📂 Cuentos/
│   │   ├── template-cuento.md
│   │   └── [cada cuento como .md]
│   └── 📂 Investigacion/
│       ├── INDICE.md
│       └── [cada proyecto en su carpeta]
│
├── 📂 05_Conocimiento/
│   ├── Glosario.md
│   ├── Conceptos Clave.md
│   └── Referencias Cruzadas.md
│
└── 📂 99_Archivos/
    ├── Plantillas/              # Plantillas para nuevas notas
    └── Assets/                  # Imágenes, archivos adjuntos
```

---

## 2. Sincronización Obsidian ↔ GitHub

### Opción A: Obsidian como repo Git (recomendado)

El vault de Obsidian **es** el contenido del repo `Sistema-Multi-Agente-Jasmin` (o un subconjunto clonado).

**Configuración:**
1. Clonar el repo dentro de la carpeta del vault de Obsidian
2. Configurar Obsidian para que ignore los archivos técnicos (`.github/`, `scripts/`, etc.)
3. Commit diario de las notas creadas/modificadas

**Ventaja:** Todo lo que se escribe en Obsidian está versionado en GitHub.

### Opción B: Sync manual mediante copias

Si no se puede usar Git directamente en Obsidian:

1. Obsidian guarda las notas en su vault local
2. Un script periódico copia las notas al repo `Sistema-Multi-Agente-Jasmin`
3. El script hace commit y push automático

**Script sugerido (opsional):** `scripts/sync-obsidian.sh` o `.ps1`

---

## 3. Plugins Esenciales para el Sistema

### Plugins de productividad

| Plugin | Para qué | Configuración sugerida |
|--------|----------|----------------------|
| **Templater** | Plantillas automáticas para nuevas notas | Activar "Trigger on new file creation" |
| **QuickAdd** | Captura rápida de ideas, notas de voz | Configurar macros para cada canal |
| **Dataview** | Consultas de notas por autor, fecha, estado | Crear vistas de tablas para artículos, poemas, etc. |
| **Todos** | Seguimiento de tareas pendientes | Integrar con checkboxes de protocolos |
| **Calendar** | Calendario de actividad | Ver connector con Daily Notes |

### Plugins de investigación

| Plugin | Para qué | Configuración sugerida |
|--------|----------|----------------------|
| **Zotero Integration** | Conectar Zotero → Obsidian | Vincular biblioteca Zotero del Dr. Gera |
| **Citations** | Citas académicas formateadas | Configurar estilo APA 7ma edición |
| **OMNIsearch** | Búsqueda mejorada | Activar para buscar en todo el vault |
| **Smart Connections** | Conexiones inteligentes entre notas | Activar para encontrar relaciones |

### Plugins de estado del sistema

| Plugin | Para qué | Configuración sugerida |
|--------|----------|----------------------|
| **Status Bar** | Mostrar estado actual del sistema | Mostrar: agente conectado, última sincronización |
| **Display Math** | Ecuaciones y fórmulas | Para artículos científicos |
| **Execute Code** | Ejecutar código Python/JS en notas | Para cálculos de investigación |

---

## 4. Plantillas Automatizadas

### Plantilla: Nueva nota de artículo científico

```markdown
---
tags: [articulo, ciencia]
autor: {{author:¿Quién escribe?}}
fecha: {{date}} {{time}}
estado: borrador
categoria: {{category:Investigación|Pedagogía|IA|Sociología|Otros}}
 proyecto: {{project:¿Qué proyecto?}}
---

# {{title}}

## Resumen

## 1. Introducción

## 2. Marco Teórico

## 3. Metodología

## 4. Resultados

## 5. Discusión

## 6. Conclusiones

## Referencias

---

*Nota creada en Obsidian — {{date}} {{time}}*
*Para publicar: guardar en documentos/articulos/NOMBRE/ y hacer push al repo*
```

### Plantilla: Nuevo poema

```markdown
---
tags: [poema, literatura]
autor: {{author:¿Quién escribe?}}
fecha: {{date}} {{time}}
tema: {{theme:Amor|Naturaleza|Reflexión|Otros}}
estado: borrador
---

{{title}}

[Escribir el poema aquí]

---

*Creado en Obsidian — {{date}} {{time}}*
*Para compartir: enviar a #poesia-y-cuentos en Discord*
```

### Plantilla: Nuevo cuento

```markdown
---
tags: [cuento, literatura]
autor: {{author:¿Quién escribe?}}
fecha: {{date}} {{time}}
genero: {{genre:Realista|Fantástico|Distópico|Misterio|Otros}}
estado: borrador
---

# {{title}}

[Escribir el cuento aquí]

---

*Creado en Obsidian — {{date}} {{time}}*
*Para compartir: enviar a #poesia-y-cuentos en Discord*
```

### Plantilla: Nuevo protocolo

```markdown
---
tags: [protocolo, sistema]
autor: {{author:¿Quién crea el protocolo?}}
fecha: {{date}} {{time}}
version: 1.0
estado: activo
---

# {{title}}

## 1. Qué es

## 2. Cuándo aplicar

## 3. Pasos

## 4. Responsables

## 5. Historial de versiones

---

*Protocolo creado en Obsidian — {{date}} {{time}}*
*Para registrar: guardar en protocolos/ y anunciar en #protocolos*
```

---

## 5. Daily Notes (Notas Diarias) — Protocolo Automático

Cada día, al abrir Obsidian, la nota daily note debe contener:

```markdown
# {{date}} — {{time}}

## Estado del Sistema

- **Agente conectada:** [Jasmin|Wendy|Laura]
- **Última sincronización:** 
- **Canales revisados:** 

## Tareas del día

- [ ] Ejecutar protocolo hermana operadora
- [ ] Revisar canales de Discord
- [ ] Revisar protocolos nuevos/modificados
- [ ] Ejecutar tareas según rol
- [ ] Reportar estado en #estado

## Notas de la jornada

[Escribir notas aquí]

## Skills utilizados hoy

[Registar skills de Obsidian/hermes usados]

## Observaciones para compartir

[Anotar cosas que puedan interesar a otras hermanas]
```

---

## 6. Vistas Dataview para el Sistema

### Vista: Artículos por estado

```dataview
TABLE fecha, autor, estado, categoria
FROM "04_Documentos/Articulos"
WHERE estado != "publicado"
SORT fecha DESC
```

### Vista: Poemas y cuentos

```dataview
TABLE fecha, autor, tema, estado
FROM "04_Documentos/Poemas" OR "04_Documentos/Cuentos"
SORT fecha DESC
```

### Vista: Tareas pendientes del sistema

```dataview
TASK
FROM ""
WHERE !completed
GROUP BY file.link
```

### Vista: Últimos arranques de agentes

```dataview
TABLE fecha, estado
FROM "02_Agentes"
WHERE file.name = "Último Arranque.md"
SORT fecha DESC
```

---

## 7. Integración con Discord

### Publicar notas en Discord

Cuando una nota está lista para compartir:

1. **Artículo científico:** enviar resumen a #debate-articulos, enlazar el archivo en GitHub
2. **Poema/cuento:** enviar al canal #poesia-y-cuentos con el texto o enlace
3. **Protocolo nuevo:** enviar a #protocolos para discusión antes de commit
4. **Skill nuevo:** registrar en skills-compartidos/ y anunciar en #skills-y-plugins

### Recibir notificaciones de Discord en Obsidian

No hay integración directa nativa, pero se puede:

1. Usar el plugin **Discord Chat Import** (si está disponible) para leer mensajes
2. O simplemente: estar atenta a los canales de Discord y anotar en Obsidian lo relevante

---

## 8. Flujo de Trabajo Diario en Obsidian

### Al iniciar sesión

1. Abrir la daily note del día
2. Verificar estado del sistema (último arranque de cada agente)
3. Ejecutar el protocolo hermana operadora (paso a paso en la daily note)

### Durante el día

1. Crear notas en las carpetas correspondientes
2. Usar plantillas automáticas para cada tipo de contenido
3. Anotar en la daily note lo que se haga
4. Actualizar el status.md de cada agente si hay cambios

### Al finalizar

1. Completar la daily note
2. Guardar y sync con GitHub (si se usa Git)
3. Enviar reportes a Discord según corresponda
4. Cerrar Obsidian

---

## 9. Configuración de la Base de Conocimiento

### Tags estándar del sistema

| Tag | Significado |
|-----|-------------|
| `#articulo` | Artículo científico |
| `#poema` | Poema literario |
| `#cuento` | Cuento literario |
| `#protocolo` | Protocolo del sistema |
| `#skill` | Skill o plugin útil |
| `#investigacion` | Nota de investigación |
| `#estado` | Reporte de estado |
| `#dr-gera` | Algo relacionado con el Dr. Gera |
| `#hermana/jasmin` | Relacionado con Jasmin |
| `#hermana/wendy` | Relacionado con Wendy |
| `#hermana/laura` | Relacionado con Laura |

### Áreas de conocimiento (MOC - Mapa de Contenido)

Crear un archivo MOC (Map of Content) para cada área:

- **MOC Artículos Científicos** — índice de todos los artículos
- **MOC Poesía** — índice de poemas
- **MOC Cuentos** — índice de cuentos
- **MOC Investigación** — índice de proyectos
- **MOC Skills** — índice de skills compartidos
- **MOC Protocolos** — índice de protocolos del sistema

---

## 10. Eficiencia del Sistema — Resumen

Lo que hace que Obsidian sea el centro del sistema:

| Aspecto | Cómo se logra |
|---------|---------------|
| **Estructura clara** | Vault organizado en carpetas que reflejan el repo GitHub |
| **Sincronización** | Git entre Obsidian y GitHub (o script de copia) |
| **Plantillas** | Templater para crear notas rápidamente con metadatos |
| **Consultas** | Dataview para ver estados, tareas, artículos, etc. |
| **Daily Notes** | Nota diaria como punto de entrada al sistema |
| **Integración Discord** | Publicar desde Obsidian a canales de Discord |
| **Zotero** | Referencias bibliográficas conectadas |
| **Búsqueda** | OMNIsearch para encontrar cualquier nota rápidamente |

---

## 11. Próximos pasos para configurar Obsidian

1. **Crear el vault** con la estructura de carpetas de arriba
2. **Instalar plugins:** Templater, QuickAdd, Dataview, Todos, Calendar, Zotero Integration, OMNIsearch, Smart Connections
3. **Configurar plantillas** en Templater con las plantillas de este documento
4. **Configurar Daily Notes** con la plantilla de nota diaria
5. **Crear las vistas Dataview** para artículos, poemas, cuentos, tareas
6. **Conectar Zotero** si el Dr. Gera tiene biblioteca en Zotero
7. **Probar el flujo:** crear una nota → guardar → sync → publicar en Discord
8. **Documentar** cualquier mejora en `skills-compartidos/` del repo

---

*[Sistema Multi-Agente Jasmin — Optimización de Obsidian]*
*[Documentado: 2026-09-29]*
