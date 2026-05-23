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
