#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

export XDG_CACHE_HOME="$DIR/qmd/.cache"

echo "Running from:"
echo "$DIR/qmd/bin/qmd"

"$DIR/qmd/bin/qmd" \
  --index portable \
  "$@"
