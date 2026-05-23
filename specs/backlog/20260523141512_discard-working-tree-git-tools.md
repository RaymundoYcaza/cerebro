# Spec — discard-working-tree en git_tools.py

Estado: backlog

## Objetivo

Agregar un comando directo a `scripts/harness/git_tools.py` llamado `discard-working-tree` para descartar cambios actuales del working tree con advertencia fuerte, confirmación exacta y backup automático previo.

## Contexto

El harness contiene herramientas Git operativas en `scripts/harness/git_tools.py`. Esta funcionalidad debe permitir limpiar cambios locales de forma segura, evitando destrucción accidental.

## Alcance

- Agregar comando directo:
  ```bash
  python3 scripts/harness/git_tools.py discard-working-tree
  ```
- Por defecto:
  - descarta cambios tracked
  - no borra archivos untracked
- Con flag:
  ```bash
  python3 scripts/harness/git_tools.py discard-working-tree --include-untracked
  ```
  también elimina untracked.
- Antes de descartar, crear backup automático:
  ```text
  scripts/harness/backups/git/working-tree-YYYYMMDDhhmmss.patch
  ```
- Exigir confirmación exacta:
  ```text
  DESCARTAR CAMBIOS
  ```
- Mostrar advertencia fuerte, `git status` y resumen de diff antes de pedir confirmación.

## Fuera de alcance

- No integrar todavía en `scripts/harness/harness.py`.
- No hacer commit automático.
- No hacer push, merge, rebase ni reset de ramas remotas.
- No modificar `vault/raymundo_ideaverse`.
- No crear recuperación automática desde backup.

## Requisitos EARS

### Ubiquitous

El sistema deberá exponer el comando `discard-working-tree` desde `scripts/harness/git_tools.py`.

El sistema deberá crear un backup `.patch` antes de descartar cambios.

El sistema deberá pedir confirmación exacta antes de ejecutar cualquier acción destructiva.

### Event-driven

Cuando el usuario ejecute `discard-working-tree`, el sistema deberá mostrar advertencia fuerte, `git status` y resumen de cambios antes de continuar.

Cuando el usuario escriba exactamente `DESCARTAR CAMBIOS`, el sistema deberá descartar los cambios tracked.

Cuando el usuario use `--include-untracked`, el sistema deberá eliminar también archivos untracked.

### State-driven

Mientras existan cambios tracked, el sistema deberá incluirlos en el backup patch.

Mientras existan archivos untracked y no se use `--include-untracked`, el sistema deberá conservarlos.

Mientras no existan cambios tracked ni untracked relevantes, el sistema deberá informar que no hay cambios que descartar.

### Unwanted behavior

Si el usuario no escribe exactamente `DESCARTAR CAMBIOS`, el sistema deberá cancelar sin modificar archivos.

Si falla la creación del backup, el sistema deberá cancelar y no descartar cambios.

Si Git devuelve error durante el descarte, el sistema deberá mostrar el error y terminar con código distinto de cero.

### Optional

Donde `--include-untracked` esté habilitada, el sistema deberá eliminar archivos untracked usando una operación Git explícita y segura.

## Archivos esperados

- `scripts/harness/git_tools.py`
- `scripts/harness/docs/git_tools.md`
- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

## Criterios de aceptación

- Existe `python3 scripts/harness/git_tools.py discard-working-tree`
- El comando exige confirmación exacta `DESCARTAR CAMBIOS`
- El comando crea backup automático antes de descartar
- Por defecto descarta tracked y conserva untracked
- `--include-untracked` elimina untracked
- No elimina ignored files
- Muestra advertencia fuerte, `git status` y resumen de diff antes de actuar
- Cancela sin cambios si la confirmación es incorrecta
- Documentación, changelog y repo map actualizados
- Checks del harness ejecutados

## Checks

```bash
python3 scripts/harness/git_tools.py discard-working-tree --help
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py scan-repo
```
