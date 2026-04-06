#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro"
PYTHON_BIN="${PYTHON_BIN:-python3}"
REPAIR_PY="$REPO_DIR/scripts/vault_manager/repair.py"

cd "$REPO_DIR"

if ! command -v gum >/dev/null 2>&1; then
  echo "Error: gum no está instalado."
  echo "Instálalo con:"
  echo "  brew install gum"
  echo "o"
  echo "  sudo snap install gum"
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "Error: jq no está instalado."
  exit 1
fi

TMP_JSON="$(mktemp)"
TMP_LINES="$(mktemp)"

cleanup() {
  rm -f "$TMP_JSON" "$TMP_LINES"
}
trap cleanup EXIT

echo "Obteniendo propuestas del Inbox..."
"$PYTHON_BIN" "$REPAIR_PY" --dry-run --format json >"$TMP_JSON"

COUNT="$(jq 'length' "$TMP_JSON")"
if [ "$COUNT" -eq 0 ]; then
  echo "No hay notas para reparar en Inbox."
  exit 0
fi

jq -r '
  .[]
  | [
      .relative_path,
      (if (.action_summary|length) > 0 then (.action_summary|join(",")) else "none" end)
    ]
  | @tsv
' "$TMP_JSON" >"$TMP_LINES"

CHOICES="$(
  cat "$TMP_LINES" |
    gum filter --placeholder "Busca por path o acción faltante..." --no-limit
)"

if [ -z "${CHOICES:-}" ]; then
  echo "No seleccionaste nada."
  exit 0
fi

echo
echo "Resumen de selección:"
printf '%s\n' "$CHOICES" | while IFS=$'\t' read -r rel actions; do
  echo "  - $rel"
  echo "    faltan: $actions"
done

echo
if ! gum confirm "¿Aplicar cambios a los archivos seleccionados?"; then
  echo "Cancelado."
  exit 0
fi

echo
printf '%s\n' "$CHOICES" | while IFS=$'\t' read -r rel actions; do
  echo "Aplicando: $rel"
  "$PYTHON_BIN" "$REPAIR_PY" --apply --yes "$rel"
done

echo
echo "Listo."
