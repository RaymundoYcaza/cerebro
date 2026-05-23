# Uso del Harness

El harness coordina contexto, checks, memoria SQLite, changelog, specs y documentación humana.

## Comandos base

Antes de modificar archivos:

```bash
python3 scripts/harness/harness.py context
python3 scripts/harness/harness.py status
python3 scripts/harness/harness.py scan-repo
```

Después de cambios:

```bash
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py log-change --summary "..." --details "..." --files "..."
python3 scripts/harness/harness.py scan-repo
```

## Documentación

Listar documentación humana:

```bash
python3 scripts/harness/harness.py docs
```

Validar documentación mínima:

```bash
python3 scripts/harness/harness.py check-docs
```

## Specs

Listar specs:

```bash
python3 scripts/harness/harness.py specs
```

Crear una spec:

```bash
python3 scripts/harness/harness.py new-spec --title "Nombre del cambio" --area harness --status backlog
```

## Cómo debe trabajar un agente

1. Leer contexto y reglas.
2. Presentar plan antes de modificar.
3. Trabajar en fases pequeñas.
4. Usar scripts temporales en `/tmp`.
5. No tocar `vault/raymundo_ideaverse` sin instrucción explícita.
6. Ejecutar checks.
7. Registrar cambios con `log-change`.
8. Actualizar documentación si agrega funcionalidad.
9. Ejecutar `scan-repo`.
