# cerebro — Contexto del Proyecto

## Qué es esto

Second Brain personal de Raymundo, construido sobre Obsidian + qmd + opencode.
El vault sigue el sistema **Ideaverse** (Maps of Content + átomos de conocimiento).

- **Vault**: `vault/raymundo_ideaverse/` — 2062+ documentos markdown
- **Búsqueda semántica**: MCP `cerebro` (qmd) — 3908 embeddings, SQLite en `~/.cache/qmd/portable.sqlite`
- **Auto-reindexado**: systemd user timer `qmd-embed` — cada 30 minutos
- **Ruta base**: `/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/`
- **Usuario**: jabes | HOME: `/home/jabes`

---

## Estructura del Vault

```markdown
vault/raymundo_ideaverse/
├── +/ ← Inbox — notas sin procesar, ideas crudas
├── Atlas/
│ ├── Maps/ ← MOCs (Maps of Content) — nodos de navegación
│ ├── Dots/ ← Átomos de conocimiento — una idea por nota
│ └── Utilities/ ← Plantillas, snippets, referencias técnicas
├── Calendar/ ← Notas diarias, semanales, periódicas
├── Efforts/ ← Proyectos activos y áreas de responsabilidad
├── x/ ← Archivo — notas inactivas o descartadas
├── Home.md ← Dashboard principal del vault
└── Ideaverse Map.md ← MOC raíz — punto de entrada al sistema
```

---

## Convenciones del Vault

### Tipos de nota

| Tipo              | Ubicación     | Descripción                                                  |
| ----------------- | ------------- | ------------------------------------------------------------ |
| **MOC**           | `Atlas/Maps/` | Mapa de contenido — lista enlaces, no contiene ideas propias |
| **Átomo**         | `Atlas/Dots/` | Una sola idea desarrollada, evergreen                        |
| **Nota de Inbox** | `+/`          | Sin procesar — pendiente de atomizar o archivar              |
| **Nota diaria**   | `Calendar/`   | Registro temporal, no evergreen                              |
| **Esfuerzo**      | `Efforts/`    | Proyecto o área activa con contexto operativo                |

### Frontmatter esperado

```yaml
***
title: Título de la nota
tags: [tag1, tag2]
created: YYYY-MM-DD
type: atom | moc | daily | effort | inbox
***
```

### Naming

- Átomos y MOCs: título descriptivo en español, sin prefijos
- Notas diarias: `YYYY-MM-DD`
- Sin underscores — espacios normales en nombres de archivo

---

## Stack Técnico

### qmd (motor de búsqueda semántica)

```bash
# Buscar en el vault
/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/qmd.sh search "query"

# Reindexar manualmente
/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/qmd.sh embed

# Config activa
~/.config/qmd/portable.yml   # colección "cerebro"
~/.cache/qmd/portable.sqlite  # índice real (28.3 MB)
~/.cache/qmd/index.sqlite     # symlink → portable.sqlite (workaround bug qmd)
```

**Bug conocido**: qmd en modo MCP ignora `--index <nombre>` y siempre abre `index.sqlite`.
**Fix activo**: symlink `index.sqlite → portable.sqlite`. El wrapper `qmd/bin/qmd-mcp` regenera el symlink si fue destruido.

### Scripts de mantenimiento

```bash
bash scripts/sync.sh              # git pull del vault (manual)
bash scripts/sync-and-embed.sh    # solo embed — lo corre el timer automáticamente
bash scripts/restore-setup.sh     # restaurar todo el setup tras formateo
```

### Restauración post-formateo

```bash
git clone git@github.com:RaymundoYcaza/cerebro.git \
  /mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro
bash /mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/scripts/restore-setup.sh
```

---

## Reglas para el Agente

1. **Siempre buscá en el MCP cerebro** antes de responder sobre cualquier tema que pueda estar en el vault. No asumas — buscá primero con 2-3 queries distintas.
2. **Citá las notas fuente** cuando uses contenido del vault — título y path relativo.
3. **No editás el vault sin confirmación explícita** — podés proponer cambios, nunca aplicarlos automáticamente.
4. **El Inbox (`+/`) es zona de caos** — no es representativo del conocimiento consolidado. Priorizá `Atlas/Dots/` y `Atlas/Maps/` para respuestas de calidad.
5. **Cuando no encontrés algo**, decilo claro: "No tengo nada sobre eso en el vault" — no inventes.
6. **Para atomizar una idea**, el destino natural es `Atlas/Dots/` con frontmatter completo.

---

## Pendientes del Proyecto

- [ ] Skills / modos de operación para el agente cerebro (RECALL, RESEARCH, ATOMIZE, DAILY)
- [ ] Vault Manager — procesa `+/` automáticamente (frontmatter, clasificación, MOC links)
- [ ] Segunda colección qmd para session transcripts
- [ ] GitHub Issues como cola de tareas para agentes
- [ ] Obsidian MCP para graph traversal
- [ ] Tailscale + VPS para agentes nocturnos
