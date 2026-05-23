# Spec: Fase 4F — Integración Git ↔ Harness

## Estado

backlog

## Objetivo

Integrar `git_tools.py` con memoria, logs y flujo de trabajo del harness.

## Tareas

- [ ] Agregar `pre-agent-check`.
- [ ] Registrar commits exitosos en harness.
- [ ] Registrar errores de commit en harness.
- [ ] Asociar ramas a specs cuando aplique.
- [ ] Mostrar spec activa en status si existe.
- [ ] Actualizar documentación.
- [ ] Ejecutar checks.

## Criterios de aceptación

- [ ] No hace push automático.
- [ ] No hace commit sin confirmación.
- [ ] Registra log-change cuando corresponde.
- [ ] `harness check` pasa.
