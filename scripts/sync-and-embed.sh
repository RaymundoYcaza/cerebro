# /home/jabes/cerebro/scripts/sync-and-embed.sh
#!/bin/bash
set -e

REPO_DIR="/home/jabes/cerebro"
LOG_FILE="/home/jabes/cerebro/sync.log"

cd "$REPO_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Pulling..." >>"$LOG_FILE"
git pull --ff-only >>"$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Embedding..." >>"$LOG_FILE"
"$REPO_DIR/qmd.sh" embed >>"$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Done." >>"$LOG_FILE"
