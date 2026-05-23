# Estructura del Repositorio

Descripción:
Mapa conceptual de los módulos principales de Cerebro.

## Propósito

Evitar mezclas de responsabilidades y ayudar a humanos/agentes a ubicar cambios.

## Flujo

La arquitectura separa utilidades compartidas, flujos técnicos, flujos reflexivos, harness operativo, specs, docs y tests.

## Comandos

Ver mapa actualizado:

```bash
python3 scripts/harness/harness.py scan-repo
```

Leer contexto:

```bash
python3 scripts/harness/harness.py context
```

## Ejemplos

```text
scripts/cerebro_notes/core/        utilidades compartidas
scripts/cerebro_notes/reflective/  notas reflexivas
scripts/cerebro_notes/technical/   notas técnicas
scripts/harness/                   operación, memoria y checks
specs/                             trabajo planeado
scripts/harness/docs/              documentación humana
scripts/cerebro_notes/tests/       smoke tests
```

## Core

`core/` contiene funciones compartidas como frontmatter, wikilinks, búsqueda simple, tags y utilidades de texto.

## Reflective

`reflective/` contiene renderers, prompts y pipeline para sesiones reflexivas y Thing Notes.

## Technical

`technical/` contiene el flujo de notas técnicas, configuración compartida y Qdrant opcional.

## Harness

`harness/` contiene memoria SQLite, comandos operativos, reglas, docs y herramientas Git.

## Specs

`specs/` guarda trabajo activo, backlog, completado y templates de planificación.

## Docs

`scripts/harness/docs/` guarda documentación humana descubierta por `harness.py docs`.

## Tests

`scripts/cerebro_notes/tests/smoke/` contiene smoke tests ejecutables sin pytest.

## Errores comunes

- Mezclar lógica reflexiva en `technical`.
- Poner utilidades compartidas fuera de `core`.
- Documentar una feature sin actualizar `index.md`.

## Troubleshooting

- Usa `rg` para ubicar módulos.
- Ejecuta `scan-repo` después de cambios estructurales.

## Notas de seguridad

- `vault/raymundo_ideaverse` está protegido por defecto.
- `.git` no debe manipularse con scripts destructivos.

## Relación con otras herramientas

- `harness.py check` valida el estado funcional.
- `git_tools.py` ayuda a revisar y commitear cambios de forma segura.
