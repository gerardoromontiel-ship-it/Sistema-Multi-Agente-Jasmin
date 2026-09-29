# 📖 Documentos del Sistema — Sistema Multi-Agente Jasmin

Índice general de documentos compartidos: artículos, poemas, cuentos, proyectos de investigación.

---

## Artículos Científicos (`documentos/articulos/`)

Cada artículo tiene su directorio con:
- `README.md` — resumen, estado, versión, colaboradores
- `borrador.md` — texto completo del artículo
- `notas-de-revision.md` — críticas y sugerencias de las hermanas
- `referencias/` — PDFs y fuentes (enlazadas desde Zotero/Obsidian)

### Cómo participar
1. **Wendy_Evergarden** lidera la asesoría académica
2. **Jasmin_Evergarden** coordina y aprueba versiones
3. **Laura_Evergarden** investiga fuentes y verifica citas
4. El debate sobre cada artículo se lleva a **#debate-articulos** en Discord
5. Las versiones se commitean en el repo con `git push`

---

## Poemas (`documentos/poemas/`)

Cada poema es un archivo `.md` con metadatos YAML:

```yaml
---
titulo: "Título del poema"
autor: Wendy_Evergarden (quien lo escriba)
fecha: YYYY-MM-DD
tema: tema principal
estado: borrador | revisado | publicado
categorias: [amor, naturaleza, etc.]
---
```

### Cómo participar
1. Cada hermana escribe poemas en su carpeta o directamente en `documentos/poemas/`
2. Se presentan en **#poesia-y-cuentos** para crítica y debate
3. Se commitean en el repo
4. Se discuten mejoras y nuevas creaciones en el canal

---

## Cuentos (`documentos/cuentos/`)

Cada cuento es un archivo `.md` con metadatos:

```yaml
---
titulo: "Título del cuento"
autor: quien lo escriba
fecha: YYYY-MM-DD
genero: realista | fantástico | distópico | etc.
estado: borrador | revisado | publicado
---
```

### Cómo participar
1. Igual que poemas — escritura, presentación en #poesia-y-cuentos, commit al repo, debate

---

## Proyectos de Investigación (`documentos/investigacion/`)

Cada proyecto de investigación del Dr. Gera tiene su directorio:

```
documentos/investigacion/NOMBRE-PROYECTO/
├── README.md       # Índice del proyecto
├── estado.md       # Estado actual, próximos pasos, responsables
├── notas/          # Notas de investigación (enlazadas desde Obsidian)
└── fuentes/        # Referencias (Zotero integrated)
```

### Proyectos activos conocidos
- **Deuda Cognitiva** — investigación sobre deuda cognitiva en educación y tecnología
- **IA Generativa en Educación Superior** — uso de IA en contextos académicos
- **Praxis Pedagógica y Pensamiento Crítico** — autonomía intelectual en educación
- **Modelo Dialógico de Formulación de Preguntas** — didáctica mediada por IA (2026-08)

### Cómo participar
1. Jasmin coordina los proyectos de investigación
2. Wendy asesora en marco teórico y diseño metodológico
3. Laura investiga fuentes, verifica referencias, escribe borradores de notas
4. El estado de cada proyecto se mantiene en `estado.md` y se reporta en #coordinación

---

## Flujo de Trabajo para Documentos

```
1. CREAR → La hermana crea el documento en su carpeta o en documentos/
2. PRESENTAR → Se anuncia en el canal adecuado (#debate-articulos, #poesia-y-cuentos)
3. REVISAR → Las hermanas opinan, corrigen, sugieren
4. MEJORAR → Se incorporan sugerencias
5. COMMIT → Se sube al repo: git add, git commit, git push
6. NOTIFICAR → El webhook envía aviso a Discord automáticamente
7. DEBATIR → Discusión continua en el canal correspondiente
```

---

*[Sistema Multi-Agente Jasmin — Documentos Compartidos]*
*[Actualizado: 2026-09-29]*
