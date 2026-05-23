# Specs

Descripción:
Specs registra trabajo planeado o en curso sin depender de un agente específico.

## Propósito

Mantener trazabilidad de trabajo antes, durante y después de una implementación.

## Flujo

1. Crear una spec en `backlog` o `active`.
2. Ejecutar el trabajo por fases pequeñas.
3. Mover la spec a `done` cuando el cambio esté cerrado.

## Comandos

Crear una spec:

```bash
python3 scripts/harness/harness.py new-spec --title "Nombre del cambio" --area harness --status backlog
```

Listar specs:

```bash
python3 scripts/harness/harness.py specs
```

## Ejemplos

Crear una spec activa:

```bash
python3 scripts/harness/harness.py new-spec --title "Documentación automática" --area harness --status active
```

## Carpetas

- `active/`: specs en ejecución o listas para ejecutar.
- `backlog/`: specs propuestas o pendientes.
- `done/`: specs cerradas.
- `templates/`: plantillas base para specs y tareas.

## Errores comunes

- Spec sin área:
  - Causa: falta contexto operativo.
  - Solución: usar `--area`.

## Troubleshooting

- Ejecuta `python3 scripts/harness/harness.py specs`.
- Revisa nombres de archivos en `specs/active`, `specs/backlog` y `specs/done`.

## Notas de seguridad

- No usar specs como autorización para modificar el vault protegido.
- No automatizar ejecución de specs sin revisión humana.

## Relación con otras herramientas

- `harness.py docs` descubre documentación.
- `harness.py check-docs` valida documentación.
- `git_tools.py` ayuda a cerrar cambios con commits seguros.
