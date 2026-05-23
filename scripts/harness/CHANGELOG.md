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

## Cambio

- Fase 3B core obsidian
- Detalle: Se creo core/obsidian.py y se migraron helpers duplicados de wikilink, nombres seguros y rutas unicas en flujos reflexivos y renderers.
- Archivos: scripts/cerebro_notes/core/obsidian.py scripts/cerebro_notes/run_reflective_interactive.py scripts/cerebro_notes/run_reflective_from_note.py scripts/cerebro_notes/reflective/markdown.py scripts/cerebro_notes/reflective/final_markdown.py scripts/cerebro_notes/technical/markdown.py

## Cambio

- Fase 3C: core/search.py implementado
- Detalle: Se extrajo fuzzy search reusable desde run_reflective_from_note.py.
- Archivos: scripts/cerebro_notes/core/search.py scripts/cerebro_notes/run_reflective_from_note.py

## Cambio

- Fase 3D: smoke tests implementados
- Detalle: Se agregaron smoke tests mínimos para frontmatter, obsidian, search y reflective dry-run.
- Archivos: scripts/cerebro_notes/tests/smoke scripts/harness/harness.py

## Cambio

- Fase 4A: Git Safety Tools
- Detalle: Se agregaron comandos seguros de Git para status, validacion de ramas, creacion de ramas, resumen de diff y commit asistido con fallback.
- Archivos: scripts/harness/git_tools.py scripts/harness/config.yaml scripts/harness/rules/git_rules.md scripts/harness/harness.py

## Cambio

- Fase 4B: Specs Workflow y documentación humana
- Detalle: Se agregaron estructura de specs, comandos specs/new-spec/docs/check-docs y documentación humana obligatoria del harness y git_tools.
- Archivos: specs scripts/harness/docs scripts/harness/harness.py scripts/harness/README.md scripts/harness/rules/agent_protocol.md

## Cambio

- Commit creado con git_tools
- Detalle: feat: Implementa fase 4B con documentacion de git tools
- Archivos: scripts/harness/.memory/cerebro_harness.sqlite scripts/harness/CHANGELOG.md scripts/harness/README.md scripts/harness/config.yaml scripts/harness/context/repo_map.md scripts/harness/docs/git_tools.md scripts/harness/docs/harness_usage.md scripts/harness/docs/index.md scripts/harness/git_tools.py scripts/harness/harness.py scripts/harness/rules/agent_protocol.md scripts/harness/rules/git_rules.md specs/README.md specs/templates/spec.template.md specs/templates/task.template.md

## Cambio

- Commit creado con git_tools
- Detalle: refactor: Elimina archivos sqlite del seguimiento
- Archivos: .gitignore scripts/harness/.memory/cerebro_harness.sqlite scripts/harness/CHANGELOG.md

## Cambio

- Corrige generación de commits con Ollama
- Detalle: git_tools commit ahora acepta texto plano, usa fallback manual y valida Conventional Commits.
- Archivos: scripts/harness/git_tools.py scripts/harness/docs/git_tools.md

## Cambio

- Corrige fallback HTTP de git_tools commit
- Detalle: git_tools commit ya no depende de requests; usa urllib estándar si requests no está disponible y mantiene generación de commit con Ollama.
- Archivos: scripts/harness/git_tools.py scripts/harness/docs/git_tools.md

## Cambio

- Commit creado con git_tools
- Detalle: feat(harness): update git tools and configuration
- Archivos: scripts/harness/CHANGELOG.md scripts/harness/context/repo_map.md scripts/harness/docs/git_tools.md scripts/harness/git_tools.py

## Cambio

- Fase 4C: documentación automática implementada
- Detalle: Se agregaron docs/check-docs, templates y validación automática de documentación.
- Archivos: scripts/harness/docs scripts/harness/harness.py

## Cambio

- Commit creado con git_tools
- Detalle: docs(harness): expandir documentación técnica y flujos de trabajo
- Archivos: scripts/harness/CHANGELOG.md scripts/harness/config.yaml scripts/harness/context/repo_map.md scripts/harness/docs/git_tools.md scripts/harness/docs/harness_usage.md scripts/harness/docs/index.md scripts/harness/docs/reflective_workflow.md scripts/harness/docs/repo_structure.md scripts/harness/docs/technical_workflow.md scripts/harness/docs/templates/architecture_doc.template.md scripts/harness/docs/templates/tool_doc.template.md scripts/harness/docs/templates/workflow_doc.template.md scripts/harness/harness.py scripts/harness/rules/agent_protocol.md specs/README.md

## Cambio

- Specs futuras creadas
- Detalle: Se crearon specs para fases 4D, 4E, 4F, 5 y 6, junto con tareas en harness.
- Archivos: specs/backlog specs/templates specs/README.md

## Cambio

- Commit creado con git_tools
- Detalle: docs(specs): update project roadmap and backlog specifications
- Archivos: prompt-base_corto.md scripts/harness/CHANGELOG.md scripts/harness/context/repo_map.md specs/README.md specs/backlog/20260523_phase-4d-transactions-rollback.md specs/backlog/20260523_phase-4e-structural-validators.md specs/backlog/20260523_phase-4f-git-harness-integration.md specs/backlog/20260523_phase-5-safe-reflective-batch.md specs/backlog/20260523_phase-6-optional-semantic-search.md specs/templates/spec.template.md specs/templates/task.template.md

## Cambio

- Add transactional utilities and integrate into run_reflective_from_note

## Cambio

- Commit creado con git_tools
- Detalle: feat(cerebro_notes): implement transaction core and reflective note execution
- Archivos: scripts/cerebro_notes/core/README.md scripts/cerebro_notes/core/transactions.py scripts/cerebro_notes/run_reflective_from_note.py scripts/cerebro_notes/tests/smoke/test_transactions.py scripts/harness/CHANGELOG.md scripts/harness/context/repo_map.md specs/README.md specs/backlog/20260523141512_discard-working-tree-git-tools.md
