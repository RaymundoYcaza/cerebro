# Agent Instructions — Cerebro

Before modifying anything, run:

```bash
python3 scripts/harness/harness.py context
python3 scripts/harness/harness.py status
python3 scripts/harness/harness.py scan-repo
```

This repository uses a local harness in `scripts/harness/`.

Agents must:

- work in small phases
- use `/tmp/*.sh` bash scripts for file modifications
- avoid large refactors
- update docs for new features
- update changelog through the harness
- run `python3 scripts/harness/harness.py check` after changes
- run `python3 scripts/harness/harness.py scan-repo` after changes

Protected paths:

- `vault/raymundo_ideaverse`
- `.git`

Do not push, merge, rebase, or commit without explicit user confirmation.

Use specs from:

- `specs/active/`
- `specs/backlog/`

If a task is large, split it into microtasks before implementation.

## First Commands

Always execute before planning:

```bash
python3 scripts/harness/harness.py context
python3 scripts/harness/harness.py status
python3 scripts/harness/harness.py scan-repo
```

## Python Environment

Always use the local virtual environment.

Preferred commands:

```bash
source .venv/bin/activate
python ...
pip ...
```

Never assume global Python packages.

Avoid using system-wide python3 unless explicitly instructed.
