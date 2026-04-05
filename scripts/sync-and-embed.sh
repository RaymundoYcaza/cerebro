#!/bin/bash
set -e

REPO_DIR="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro"
LOG_FILE="$REPO_DIR/sync.log"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Embedding..." >>"$LOG_FILE"
"$REPO_DIR/qmd.sh" embed >>"$LOG_FILE" 2>&1
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Done." >>"$LOG_FILE"
