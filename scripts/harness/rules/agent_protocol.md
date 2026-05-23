# Agent Protocol

Todo agente debe seguir este protocolo:

1. Leer `scripts/harness/context/current_state.md`.
2. Leer reglas relevantes en `scripts/harness/rules/`.
3. Revisar memoria SQLite mediante `harness.py status`.
4. Presentar plan antes de modificar archivos.
5. Preferir scripts bash temporales para crear o modificar archivos.
6. Ejecutar checks mínimos después de cambios.
7. Registrar decisiones importantes en SQLite.
8. Actualizar `CHANGELOG.md`.
9. Documentar funcionalidades nuevas.

El agente puede modificar archivos directamente solo si el usuario lo solicita o lo confirma.

## Documentación obligatoria para nueva funcionalidad

Toda nueva funcionalidad debe actualizar:

- documentación humana correspondiente en `scripts/harness/docs/`, `scripts/cerebro_notes/*/README.md` o `specs/README.md`;
- `scripts/harness/CHANGELOG.md` mediante `harness.py log-change`;
- memoria SQLite mediante `harness.py log-change`;
- `scripts/harness/context/repo_map.md` mediante `harness.py scan-repo`.

