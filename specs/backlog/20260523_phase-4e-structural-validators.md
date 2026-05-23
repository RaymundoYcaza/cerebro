# Spec: Fase 4E — Validadores estructurales

## Estado

backlog

## Objetivo

Validar frontmatter y estructura mínima de notas generadas.

## Tareas

- [ ] Crear `scripts/cerebro_notes/core/validators.py`.
- [ ] Implementar extracción de frontmatter.
- [ ] Validar `technical`.
- [ ] Validar `reflective-session`.
- [ ] Validar `thing-note`.
- [ ] Validar `source-extract`.
- [ ] Integrar validación antes de escritura.
- [ ] Crear smoke tests.
- [ ] Documentar reglas.

## Criterios de aceptación

- [ ] Detecta triple comilla en wikilinks.
- [ ] Detecta tags no-lista.
- [ ] Detecta falta de title en Thing Note.
- [ ] `harness check` pasa.
