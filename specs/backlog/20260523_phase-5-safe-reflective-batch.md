# Spec: Fase 5 — Batch reflexivo seguro

## Estado

backlog

## Objetivo

Procesar múltiples notas reflexivas de forma segura, con dry-run por defecto.

## Tareas

- [ ] Crear `run_reflective_batch.py`.
- [ ] Crear `reflective/batch.py`.
- [ ] Usar transacciones.
- [ ] Usar validadores.
- [ ] Implementar reporte batch.
- [ ] Crear smoke tests.
- [ ] Actualizar documentación.

## Criterios de aceptación

- [ ] Dry-run es el default.
- [ ] `write` requiere `--confirm-write`.
- [ ] No mueve fuentes si falla creación de notas.
- [ ] Genera reporte claro.
- [ ] `harness check` pasa.
