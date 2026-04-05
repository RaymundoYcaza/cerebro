#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

export XDG_CACHE_HOME="$DIR/qmd/.cache"
export QMD_CACHE_DIR="$DIR/qmd/.cache"

echo "Running from:"
echo "$DIR/qmd/bin/qmd"

"$DIR/qmd/bin/qmd" \
  --index portable \
  --data-dir "$DIR/qmd/.qmd-data" \
  "$@"