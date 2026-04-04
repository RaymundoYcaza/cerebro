#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Running from:"
echo "$DIR/qmd/bin/qmd"

"$DIR/qmd/bin/qmd" \
  --index portable \
  "$@"
