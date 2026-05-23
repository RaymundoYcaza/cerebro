# Cerebro Harness

Harness local y agnóstico para evolucionar el repositorio `cerebro`.

## Propósito

Ayudar a cualquier agente —Claude Code, OpenCode, Codex CLI, Gemini CLI, Ollama u otro— a trabajar sobre el proyecto con contexto, memoria, reglas y trazabilidad.

## Filosofía

El flujo estándar es:

```text
plan → script bash temporal → ejecución → checks → memoria SQLite → changelog → documentación
```

## Principios

- El agente debe entender el estado antes de modificar.
- Los cambios de archivos se hacen preferentemente mediante scripts bash temporales.
- La memoria operacional vive en SQLite.
- Los cambios relevantes se registran en `CHANGELOG.md`.
- Toda funcionalidad nueva debe documentarse.
- La bóveda de Obsidian está protegida por defecto.
- Los scripts deben soportar `dry-run` cuando sea posible.

## Cómo encontrar documentación

Lista la documentación humana disponible con:

```bash
python3 scripts/harness/harness.py docs
```

Valida que la documentación mínima exista con:

```bash
python3 scripts/harness/harness.py check-docs
```

La documentación extendida vive en `scripts/harness/docs/`.

## Cómo usar specs

Lista specs:

```bash
python3 scripts/harness/harness.py specs
```

Crea una spec nueva:

```bash
python3 scripts/harness/harness.py new-spec --title "Nombre del cambio" --area harness --status backlog
```

Las specs viven en `specs/active`, `specs/backlog` y `specs/done`.

## Cómo debe trabajar un agente

Un agente debe:

1. Ejecutar `context`, `status` y `scan-repo` antes de modificar.
2. Presentar plan y riesgos.
3. Trabajar en fases pequeñas.
4. Usar scripts temporales en `/tmp`.
5. Evitar `vault/raymundo_ideaverse` salvo instrucción explícita.
6. Ejecutar `check`.
7. Registrar cambios con `log-change`.
8. Actualizar documentación humana para toda funcionalidad nueva.
9. Ejecutar `scan-repo`.

