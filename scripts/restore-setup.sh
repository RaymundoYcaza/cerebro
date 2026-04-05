#!/bin/bash
# restore-setup.sh — Restaura toda la config cerebro tras un formateo
set -euo pipefail

CEREBRO_DIR="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro"
QMD_CACHE="$HOME/.cache/qmd"
QMD_CONFIG="$HOME/.config/qmd"
OPENCODE_CONFIG="$HOME/.config/opencode"

echo "==> [1/5] Creando directorios de cache y config..."
mkdir -p "$QMD_CACHE" "$QMD_CONFIG" "$OPENCODE_CONFIG"

echo "==> [2/5] Aplicando symlink index -> portable..."
if [ -f "$QMD_CACHE/index.sqlite" ] && [ ! -L "$QMD_CACHE/index.sqlite" ]; then
  mv "$QMD_CACHE/index.sqlite" "$QMD_CACHE/index.sqlite.bak"
fi
ln -sf "$QMD_CACHE/portable.sqlite" "$QMD_CACHE/index.sqlite"

echo "==> [3/5] Copiando portable.sqlite al cache de usuario..."
if [ ! -f "$QMD_CACHE/portable.sqlite" ]; then
  cp "$CEREBRO_DIR/qmd/.cache/qmd/portable.sqlite" "$QMD_CACHE/portable.sqlite"
  echo "    portable.sqlite copiado."
else
  echo "    portable.sqlite ya existe, omitiendo."
fi

echo "==> [4/5] Enlazando portable.yml al config de usuario..."
if [ ! -f "$QMD_CONFIG/portable.yml" ]; then
  ln -sf "$CEREBRO_DIR/qmd/.config/qmd/portable.yml" "$QMD_CONFIG/portable.yml"
  echo "    portable.yml enlazado."
else
  echo "    portable.yml ya existe, omitiendo."
fi

echo "==> [5/5] Verificando permisos del wrapper qmd-mcp..."
chmod +x "$CEREBRO_DIR/qmd/bin/qmd-mcp"

echo ""
echo "==> Verificación final:"
sqlite3 "$QMD_CACHE/portable.sqlite" "SELECT COUNT(*) FROM documents WHERE active = 1;" |
  xargs -I{} echo "    Documentos indexados: {}"

echo ""
echo "✓ Setup restaurado. Reinicia opencode para que tome efecto."
