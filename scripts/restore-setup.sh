#!/bin/bash
# restore-setup.sh — Restaura toda la config cerebro tras un formateo
set -euo pipefail

CEREBRO_DIR="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro"
QMD_CACHE="$HOME/.cache/qmd"
QMD_CONFIG="$HOME/.config/qmd"
OPENCODE_CONFIG="$HOME/.config/opencode"
SYSTEMD_USER_DIR="$HOME/.config/systemd/user"

echo "==> [1/8] Creando directorios de cache y config..."
mkdir -p "$QMD_CACHE" "$QMD_CONFIG" "$OPENCODE_CONFIG" "$SYSTEMD_USER_DIR"

echo "==> [2/8] Aplicando symlink index -> portable..."
if [ -f "$QMD_CACHE/index.sqlite" ] && [ ! -L "$QMD_CACHE/index.sqlite" ]; then
  mv "$QMD_CACHE/index.sqlite" "$QMD_CACHE/index.sqlite.bak"
fi
ln -sf "$QMD_CACHE/portable.sqlite" "$QMD_CACHE/index.sqlite"

echo "==> [3/8] Copiando portable.sqlite al cache de usuario..."
if [ ! -f "$QMD_CACHE/portable.sqlite" ]; then
  cp "$CEREBRO_DIR/qmd/.cache/qmd/portable.sqlite" "$QMD_CACHE/portable.sqlite"
  echo "    portable.sqlite copiado."
else
  echo "    portable.sqlite ya existe, omitiendo."
fi

echo "==> [4/8] Enlazando portable.yml al config de usuario..."
if [ ! -L "$QMD_CONFIG/portable.yml" ]; then
  ln -sf "$CEREBRO_DIR/qmd/.config/qmd/portable.yml" "$QMD_CONFIG/portable.yml"
  echo "    portable.yml enlazado."
else
  echo "    portable.yml ya existe, omitiendo."
fi

echo "==> [5/8] Verificando permisos del wrapper qmd-mcp..."
chmod +x "$CEREBRO_DIR/qmd/bin/qmd-mcp"

echo "==> [6/8] Instalando units systemd user..."
cp "$CEREBRO_DIR/scripts/qmd-embed.service" "$SYSTEMD_USER_DIR/"
cp "$CEREBRO_DIR/scripts/qmd-embed.timer" "$SYSTEMD_USER_DIR/"

echo "==> [7/8] Recargando y habilitando timer..."
systemctl --user daemon-reload
systemctl --user enable --now qmd-embed.timer

echo "==> [8/8] Verificando timer y setup..."
echo ""
echo "==> Verificación final:"

sqlite3 "$QMD_CACHE/portable.sqlite" "SELECT COUNT(*) FROM documents WHERE active = 1;" |
  xargs -I{} echo "    Documentos indexados: {}"

echo "    index.sqlite -> $(readlink -f "$QMD_CACHE/index.sqlite")"

systemctl --user status qmd-embed.timer --no-pager || true
systemctl --user list-timers --all | grep qmd-embed || true

if loginctl show-user "$USER" | grep -q 'Linger=yes'; then
  echo "    Linger: habilitado"
else
  echo "    Linger: NO habilitado"
  echo "    Recomendado: sudo loginctl enable-linger $USER"
fi

echo ""
echo "✓ Setup restaurado. Reinicia opencode para que tome efecto."
