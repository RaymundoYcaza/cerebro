#!/bin/bash
set -e
REPO="/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro"
LOG="$REPO/sync.log"

cd "$REPO"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === sync start ===" >>"$LOG"
git pull --ff-only >>"$LOG" 2>&1
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === sync done ===" >>"$LOG"
