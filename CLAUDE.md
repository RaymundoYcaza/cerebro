# cerebro — Contexto del Proyecto

## Qué es esto

Second Brain personal de Raymundo, construido sobre Obsidian + qmd + opencode.
El vault sigue el sistema **Ideaverse** (Maps of Content + átomos de conocimiento).

- **Vault**: `vault/raymundo_ideaverse/` — 2062+ documentos markdown
- **Búsqueda semántica**: MCP `qmd` — 3908 embeddings, SQLite en `~/.cache/qmd/portable.sqlite`
- **Auto-reindexado**: systemd user timer `qmd-embed` — cada 30 minutos
- **Ruta base**: `/mnt/c/cerebro/`
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

**Skill disponible**: `/qmd` — Usar como primera opción para cualquier búsqueda en el vault.

**MCP disponible**: `qmd` — Fallback cuando la skill no esté disponible.

**Uso prioritario** (en este orden):
1. **Skill `/qmd`** — Ejecutar con argumentos de consulta: `/qmd search "keywords"` o `/qmd query "pregunta natural"`
2. **MCP `qmd`** — Usar herramientas `mcp__qmd__query`, `mcp__qmd__search`, `mcp__qmd__get`
3. **CLI directo** (último recurso):
   ```bash
   /mnt/c/cerebro/qmd.sh search "query"
   /mnt/c/cerebro/qmd.sh query "pregunta en lenguaje natural"
   /mnt/c/cerebro/qmd.sh embed  # Reindexar manualmente
   ```

**Config activa**:
- `~/.config/qmd/portable.yml` — colección "cerebro"
- `~/.cache/qmd/portable.sqlite` — índice real
- `~/.cache/qmd/index.sqlite` — symlink → portable.sqlite (workaround bug qmd)
- `~/.config/claude-code/config.json` — MCP server registrado

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
  /mnt/c/cerebro
bash /mnt/c/cerebro/scripts/restore-setup.sh
```

---

## Reglas para el Agente

1. **Siempre usá la skill `/qmd` primero** (o MCP `qmd` como fallback) antes de responder sobre cualquier tema que pueda estar en el vault. No asumas — buscá primero con 2-3 queries distintas. El comando `/qmd` es la forma más rápida y prioritaria de consultar el conocimiento del vault.
2. **Citá las notas fuente** cuando uses contenido del vault — título y path relativo.
3. **No editás el vault sin confirmación explícita** — podés proponer cambios, nunca aplicarlos automáticamente.
4. **El Inbox (`+/`) es zona de caos** — no es representativo del conocimiento consolidado. Priorizá `Atlas/Dots/` y `Atlas/Maps/` para respuestas de calidad.
5. **Cuando no encontrés algo**, decilo claro: "No tengo nada sobre eso en el vault" — no inventes.
6. **Para atomizar una idea**, el destino natural es `Atlas/Dots/` con frontmatter completo.

---

## Pendientes del Proyecto

- [x] **MCP qmd configurado** — Skill `/qmd` disponible para búsquedas semánticas
- [ ] Skills / modos de operación para el agente cerebro (RECALL, RESEARCH, ATOMIZE, DAILY)
- [ ] Vault Manager — procesa `+/` automáticamente (frontmatter, clasificación, MOC links)
- [ ] Segunda colección qmd para session transcripts
- [ ] GitHub Issues como cola de tareas para agentes
- [ ] Obsidian MCP para graph traversal
- [ ] Tailscale + VPS para agentes nocturnos
