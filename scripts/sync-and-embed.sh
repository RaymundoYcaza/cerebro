# /home/jabes/cerebro/scripts/sync-and-embed.sh
#!/bin/bash
set -e

REPO_DIR="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro"
LOG_FILE="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/sync.log"

cd "$REPO_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Pulling..." >>"$LOG_FILE"
git pull --ff-only >>"$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Embedding..." >>"$LOG_FILE"
"$REPO_DIR/qmd.sh" embed >>"$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Done." >>"$LOG_FILE"
