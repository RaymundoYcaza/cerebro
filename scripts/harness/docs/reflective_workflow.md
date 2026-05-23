# Reflective Workflow

Descripción:
Guía humana para los flujos reflexivos desde texto y desde nota fuente.

## Propósito

Convertir Sparks o extractos en sesiones reflexivas guiadas y Thing Notes limpias.

## Flujo

1. Entrada desde texto directo, stdin, archivo o nota fuente.
2. El modelo sugiere señal, título, preguntas, tags y conexiones.
3. Python decide rutas, nombres, frontmatter y escritura.
4. En modo interactivo se pide validación humana.
5. Se genera sesión reflexiva y/o Thing Note.

## Comandos

Dry-run desde texto:

```bash
cd scripts/cerebro_notes
python3 run_reflective.py --text "idea" --config config.yaml --dry-run --nothink
```

Interfaz interactiva:

```bash
python3 run_reflective_interactive.py --config config.yaml --dry-run
```

Desde nota fuente:

```bash
python3 run_reflective_from_note.py --config config.yaml --query "texto" --dry-run
```

Escribir sin mover fuente:

```bash
python3 run_reflective_from_note.py --config config.yaml --query "texto" --write --no-move-source
```

## Ejemplos

Generar solo Thing Note:

```bash
python3 run_reflective_from_note.py --query "dataclass" --dry-run --output-mode thing
```

Generar sesión y Thing Note:

```bash
python3 run_reflective_from_note.py --query "dataclass" --write --output-mode both
```

## Dry-run

`--dry-run` imprime Markdown y no escribe archivos ni mueve fuentes.

## Move Source

Con `--write`, `run_reflective_from_note.py` mueve la fuente a `Atlas/Dots/Sources` salvo que uses `--no-move-source`.

## Output Mode

- `session`: genera sesión reflexiva.
- `thing`: genera Thing Note limpia.
- `both`: genera ambas.

## Session Notes

La sesión conserva proceso, preguntas y respuestas guiadas.

## Thing Notes

La Thing Note debe quedar limpia, con menos proceso reflexivo y lista para moverse manualmente al Atlas.

## Errores comunes

- Ollama no responde:
  - Causa: servidor local apagado o modelo no disponible.
  - Solución: revisar `ollama` y `config.yaml`.

- Fuente movida por accidente:
  - Causa: uso de `--write` sin `--no-move-source`.
  - Solución: usar dry-run primero.

## Troubleshooting

- Ejecuta `run_reflective_from_note.py --help`.
- Verifica `paths.inbox_sources_dir` y `paths.sources_dir`.
- Revisa frontmatter y wikilinks en YAML.

## Notas de seguridad

- No mover fuentes en dry-run.
- No editar `vault/raymundo_ideaverse` sin instrucción explícita desde agentes.

## Relación con otras herramientas

- Usa `core/frontmatter.py` para YAML.
- Usa `core/obsidian.py` para wikilinks/nombres.
- Usa `core/search.py` para búsqueda fuzzy.
