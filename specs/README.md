# Specs

Specs registra trabajo planeado o en curso sin depender de un agente específico.

## Carpetas

- `active/`: specs en ejecución o listas para ejecutar.
- `backlog/`: specs propuestas o pendientes.
- `done/`: specs cerradas.
- `templates/`: plantillas base para specs y tareas.

## Flujo recomendado

Crear una spec:

```bash
python3 scripts/harness/harness.py new-spec --title "Nombre del cambio" --area harness --status backlog
```

Listar specs:

```bash
python3 scripts/harness/harness.py specs
```

Mover una spec entre carpetas debe hacerse manualmente y de forma explícita. El harness no hace planificación automática.
