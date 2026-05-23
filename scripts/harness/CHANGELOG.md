# Changelog — Cerebro Harness

## 2026-05-23

- Se inicializa el harness agnóstico para el repositorio `cerebro`.
- Se define memoria SQLite local.
- Se establecen reglas de trabajo con agentes.

## Cambio

- Se creó harness SQLite inicial
- Detalle: Incluye memoria operacional, reglas para agentes, contexto del proyecto y changelog.
- Archivos: scripts/harness

## Cambio

- Fase 2 del harness implementada
- Detalle: Se agregaron scan-repo, repo_map.md, checks ampliados y sesiones start/end.
- Archivos: scripts/harness/harness.py scripts/harness/tools/repo_scan.py scripts/harness/context/repo_map.md

## Cambio

- Sesión #1 cerrada
- Detalle: Prueba de sesión completada correctamente.
- Archivos: scripts/harness

## Cambio

- Corrección Fase 3 frontmatter v2
- Detalle: Se reconstruyó _yaml_block para eliminar definitivamente yaml.safe_dump directo.
- Archivos: scripts/cerebro_notes/reflective/markdown.py scripts/cerebro_notes/reflective/final_markdown.py scripts/cerebro_notes/technical/markdown.py

## Cambio

- Documentacion del flujo reflexivo desde nota
- Detalle: Se documento run_reflective_from_note.py y se ajusto scan-repo para no recorrer directorios ignorados como .venv.
- Archivos: scripts/cerebro_notes/reflective/README.md scripts/harness/tools/repo_scan.py scripts/harness/tasks/backlog.md
