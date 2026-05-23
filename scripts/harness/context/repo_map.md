# Repo Map — Cerebro

Generated: 2026-05-23T11:50:03

## cerebro_notes

```text
- cerebro_notes/
  - core/
    - __init__.py
    - frontmatter.py
    - obsidian.py
    - search.py
    - source_note.py
    - tags.py
    - text_utils.py
  - reflective/
    - __init__.py
    - cli.py
    - final_markdown.py
    - llm.py
    - markdown.py
    - pipeline.py
    - prompts.py
    - README.md
  - technical/
    - examples/
      - docker-compose-fish.txt
    - __init__.py
    - cli.py
    - config.py
    - llm.py
    - markdown.py
    - pipeline.py
    - qdrant_store.py
    - README.md
  - tests/
    - smoke/
      - test_frontmatter.py
      - test_obsidian.py
      - test_reflective_dryrun.py
      - test_search.py
  - bash
  - config.example.yaml
  - config.yaml
  - requirements.txt
  - run_reflective.py
  - run_reflective_from_note.py
  - run_reflective_interactive.py
  - run_technical.py
```

### Python files

- `scripts/cerebro_notes/core/__init__.py`
- `scripts/cerebro_notes/core/frontmatter.py`
- `scripts/cerebro_notes/core/obsidian.py`
- `scripts/cerebro_notes/core/search.py`
- `scripts/cerebro_notes/core/source_note.py`
- `scripts/cerebro_notes/core/tags.py`
- `scripts/cerebro_notes/core/text_utils.py`
- `scripts/cerebro_notes/reflective/__init__.py`
- `scripts/cerebro_notes/reflective/cli.py`
- `scripts/cerebro_notes/reflective/final_markdown.py`
- `scripts/cerebro_notes/reflective/llm.py`
- `scripts/cerebro_notes/reflective/markdown.py`
- `scripts/cerebro_notes/reflective/pipeline.py`
- `scripts/cerebro_notes/reflective/prompts.py`
- `scripts/cerebro_notes/run_reflective.py`
- `scripts/cerebro_notes/run_reflective_from_note.py`
- `scripts/cerebro_notes/run_reflective_interactive.py`
- `scripts/cerebro_notes/run_technical.py`
- `scripts/cerebro_notes/technical/__init__.py`
- `scripts/cerebro_notes/technical/cli.py`
- `scripts/cerebro_notes/technical/config.py`
- `scripts/cerebro_notes/technical/llm.py`
- `scripts/cerebro_notes/technical/markdown.py`
- `scripts/cerebro_notes/technical/pipeline.py`
- `scripts/cerebro_notes/technical/qdrant_store.py`
- `scripts/cerebro_notes/tests/smoke/test_frontmatter.py`
- `scripts/cerebro_notes/tests/smoke/test_obsidian.py`
- `scripts/cerebro_notes/tests/smoke/test_reflective_dryrun.py`
- `scripts/cerebro_notes/tests/smoke/test_search.py`

### Shell scripts

- Ninguno

### Config files

- `scripts/cerebro_notes/config.example.yaml`
- `scripts/cerebro_notes/config.yaml`

### TODO/FIXME

- Ninguno detectado

## harness

```text
- harness/
  - .memory/
    - cerebro_harness.sqlite
  - backups/
    - fix_phase3_frontmatter/
      - reflective_final_markdown.py.bak
      - reflective_markdown.py.bak
      - technical_markdown.py.bak
    - fix_phase3_frontmatter_v2/
      - reflective_final_markdown.py.bak
      - reflective_markdown.py.bak
      - technical_markdown.py.bak
    - phase3_frontmatter/
      - reflective_final_markdown.py.bak
      - reflective_markdown.py.bak
      - technical_markdown.py.bak
  - context/
    - current_state.md
    - glossary.md
    - project_brief.md
    - repo_map.md
  - docs/
    - git_tools.md
    - harness_usage.md
    - index.md
  - prompts/
  - rules/
    - agent_protocol.md
    - cerebro_notes_rules.md
    - file_modification_rules.md
    - git_rules.md
    - obsidian_rules.md
  - tasks/
    - active_task.md
    - backlog.md
    - done.md
  - tools/
    - __init__.py
    - memory.py
    - repo_scan.py
  - CHANGELOG.md
  - config.yaml
  - git_tools.py
  - harness.py
  - README.md
```

### Python files

- `scripts/harness/git_tools.py`
- `scripts/harness/harness.py`
- `scripts/harness/tools/__init__.py`
- `scripts/harness/tools/memory.py`
- `scripts/harness/tools/repo_scan.py`

### Shell scripts

- Ninguno

### Config files

- `scripts/harness/config.yaml`

### TODO/FIXME

- `scripts/harness/context/repo_map.md`
- `scripts/harness/tools/repo_scan.py`

## Main Commands

```bash
python3 scripts/harness/harness.py status
python3 scripts/harness/harness.py context
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py scan-repo
```
