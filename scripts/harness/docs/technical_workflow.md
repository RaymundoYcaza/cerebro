# Technical Workflow

Descripción:
Guía humana para generar notas técnicas estructuradas.

## Propósito

Transformar contenido técnico crudo en notas Markdown para Obsidian, con frontmatter controlado por Python.

## Flujo

1. Leer texto técnico desde archivo, stdin o argumento.
2. Compactar contenido para prompt.
3. Pedir extracción estructurada al modelo local.
4. Normalizar tags y frontmatter.
5. Renderizar nota técnica.
6. Opcionalmente escribir e indexar.

## Comandos

Dry-run:

```bash
cd scripts/cerebro_notes
python3 run_technical.py --text "nota técnica" --config config.yaml --dry-run
```

Desde archivo:

```bash
python3 run_technical.py --input nota.txt --config config.yaml --write
```

Ayuda:

```bash
python3 run_technical.py --help
```

## Ejemplos

Procesar un comando:

```bash
python3 run_technical.py --text "docker compose up falla por puerto ocupado" --dry-run
```

## Búsqueda fuzzy

`run_technical.py` incluye búsqueda simple para ubicar notas fuente técnicas cuando corresponde. La extracción reusable para Markdown vive en `core/search.py`.

## Source Notes

Las notas fuente preservan trazabilidad mediante hashes, source paths y frontmatter controlado.

## Generación técnica

El modelo sugiere resumen, problema, contexto, solución, pasos, comandos, errores y vacíos. Python valida estructura final.

## Errores comunes

- JSON inválido del modelo:
  - Causa: respuesta con texto extra.
  - Solución: revisar fallback de extracción en `technical/llm.py`.

- Tags fuera de política:
  - Causa: sugerencias libres del modelo.
  - Solución: revisar `core/tags.py`.

## Troubleshooting

- Ejecuta `run_technical.py --help`.
- Revisa `scripts/cerebro_notes/config.yaml`.
- Ejecuta `python3 scripts/harness/harness.py check`.

## Notas de seguridad

- Usar dry-run antes de write.
- Python decide rutas, nombres, frontmatter y escritura.

## Relación con otras herramientas

- `core/frontmatter.py` serializa YAML.
- `technical/markdown.py` renderiza notas técnicas.
- `technical/pipeline.py` coordina extracción y escritura.
