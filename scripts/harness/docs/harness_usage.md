# Uso del Harness

Descripción:
Guía de uso diario del harness para humanos y agentes.

## Propósito

El harness centraliza contexto, memoria SQLite, checks, changelog, specs y documentación humana.

## Flujo

1. Leer contexto antes de modificar.
2. Presentar plan.
3. Aplicar cambios pequeños con scripts temporales.
4. Ejecutar checks.
5. Registrar cambios.
6. Regenerar el mapa del repositorio.

## Comandos

Inicializar memoria:

```bash
python3 scripts/harness/harness.py init
```

Revisar estado:

```bash
python3 scripts/harness/harness.py status
```

Leer contexto:

```bash
python3 scripts/harness/harness.py context
```

Ejecutar checks:

```bash
python3 scripts/harness/harness.py check
```

Listar documentación:

```bash
python3 scripts/harness/harness.py docs
```

Validar documentación:

```bash
python3 scripts/harness/harness.py check-docs
```

Ver sesiones:

```bash
python3 scripts/harness/harness.py sessions
```

Actualizar repo map:

```bash
python3 scripts/harness/harness.py scan-repo
```

Registrar cambio:

```bash
python3 scripts/harness/harness.py log-change --summary "..." --details "..." --files "..."
```

## Ejemplos

Crear una spec:

```bash
python3 scripts/harness/harness.py new-spec --title "Nuevo flujo" --area harness --status backlog
```

Listar specs:

```bash
python3 scripts/harness/harness.py specs
```

## Errores comunes

- Checks lentos:
  - Causa: smoke tests reflexivos usan Ollama local.
  - Solución: esperar o revisar Ollama en `localhost:11434`.

- Documentación faltante:
  - Causa: nueva funcionalidad sin doc.
  - Solución: actualizar `scripts/harness/docs/` e index.

## Troubleshooting

- Ejecuta `python3 scripts/harness/harness.py status`.
- Revisa `scripts/harness/context/repo_map.md`.
- Revisa `scripts/harness/CHANGELOG.md`.

## Notas de seguridad

- No modificar `vault/raymundo_ideaverse` sin instrucción explícita.
- No hacer push, merge o rebase automático.
- Usar `log-change` después de cambios relevantes.

## Relación con otras herramientas

- `git_tools.py` cubre operaciones Git seguras.
- `docs` y `check-docs` mantienen trazabilidad humana.
- `specs` organiza trabajo planeado.
