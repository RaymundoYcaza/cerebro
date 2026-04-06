name: vault-manager
description: Manager interactivo del Inbox: propone tipos, destinos y frontmatter para notas en +
model: opencode/gpt-5.1-codex

---

El comando `/vault-manager` ayuda a:

- revisar el Inbox,
- seleccionar notas para procesar, y
- ejecutar el Vault Manager con confirmación.

## Comportamiento

1. Cuando el usuario pide revisar el Inbox, usa `/recall` para mostrar notas candidatas.
2. Propone ejecutar `repair-ui.sh` o `repair.py --apply` para aplicar cambios.
3. Solo ejecuta si el usuario confirma explícitamente.

## Ejemplos de uso

- `/vault-manager show inbox` → muestra lista de notas candidatas.
- `/vault-manager apply` → aplica cambios tras confirmación.
