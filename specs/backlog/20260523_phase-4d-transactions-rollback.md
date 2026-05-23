# Spec: Fase 4D — Transacciones y rollback seguro

## Estado

backlog

## Objetivo

Agregar seguridad transaccional a operaciones de escritura y movimiento de notas.

## Tareas

- [ ] Crear `scripts/cerebro_notes/core/transactions.py`.
- [ ] Implementar `atomic_write_text`.
- [ ] Implementar `safe_move_file`.
- [ ] Implementar contexto transaccional simple.
- [ ] Integrar en `run_reflective_from_note.py`.
- [ ] Crear smoke test con `tempfile`.
- [ ] Actualizar documentación humana.
- [ ] Ejecutar harness check.
- [ ] Registrar log-change.

## Criterios de aceptación

- [ ] No mueve fuente si falla creación de notas.
- [ ] Si falla después de mover, restaura fuente.
- [ ] No modifica vault en tests.
- [ ] `harness check` pasa.
