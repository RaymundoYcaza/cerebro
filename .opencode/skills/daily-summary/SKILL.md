---
name: daily-summary
description: Use this skill to produce a concise daily summary from the vault, work logs, and session notes.
---

# Daily Summary

## Purpose

Produce a concise daily summary from the vault, work logs, and session notes.

## When to use

Use this skill when the user asks to:

- Summarize the day.
- List completed work and pending tasks.
- Review notes created today.
- Create a daily report for the vault.

## Operating rules

- Prefer calendar notes and recent session transcripts.
- Separate completed items, blockers, and next actions.
- Keep it short and actionable.
- Do not invent progress.
- If there is little data, say so explicitly.

## Workflow

1. Collect notes from the current day.
2. Identify completed work.
3. Identify open tasks and blockers.
4. Extract important decisions.
5. Produce a short summary with next steps.

## Output format

- What happened today
- Completed
- Pending
- Blockers
- Next actions

## Example

What happened today:

- Fixed qmd MCP symlink.
- Installed systemd timer for reindexing.

Pending:

- Add OpenCode commands for recall and atomize.
