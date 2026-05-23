from __future__ import annotations

from datetime import datetime
from pathlib import Path


IGNORE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", ".mypy_cache", ".pytest_cache"}


def should_ignore(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def scan_tree(root: Path, max_depth: int = 5) -> list[str]:
    lines: list[str] = []

    def walk(path: Path, depth: int) -> None:
        if depth > max_depth or should_ignore(path):
            return

        indent = "  " * depth
        label = path.name + ("/" if path.is_dir() else "")
        lines.append(f"{indent}- {label}")

        if path.is_dir():
            for child in sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
                if not should_ignore(child):
                    walk(child, depth + 1)

    walk(root, 0)
    return lines


def list_by_suffix(root: Path, suffixes: set[str]) -> list[Path]:
    if not root.exists():
        return []

    out: list[Path] = []

    def walk(path: Path) -> None:
        if should_ignore(path):
            return

        if path.is_file():
            if path.suffix in suffixes:
                out.append(path)
            return

        if path.is_dir():
            for child in path.iterdir():
                walk(child)

    walk(root)
    return sorted(out)


def find_todos(root: Path) -> list[Path]:
    out: list[Path] = []

    for path in list_by_suffix(root, {".py", ".md", ".yaml", ".yml", ".sh"}):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        if "TODO" in text or "FIXME" in text:
            out.append(path)

    return out


def rel(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except Exception:
        return path.as_posix()


def build_repo_map(repo_root: Path) -> str:
    now = datetime.now().isoformat(timespec="seconds")

    sections: list[str] = [
        "# Repo Map — Cerebro",
        "",
        f"Generated: {now}",
        "",
    ]

    for title, root in [
        ("cerebro_notes", repo_root / "scripts" / "cerebro_notes"),
        ("harness", repo_root / "scripts" / "harness"),
    ]:
        sections += [f"## {title}", ""]

        if not root.exists():
            sections += [f"_No existe: `{root}`_", ""]
            continue

        sections += ["```text"]
        sections += scan_tree(root)
        sections += ["```", ""]

        py_files = list_by_suffix(root, {".py"})
        sh_files = list_by_suffix(root, {".sh"})
        cfg_files = list_by_suffix(root, {".yaml", ".yml", ".json", ".toml"})
        todos = find_todos(root)

        sections += ["### Python files", ""]
        sections += [f"- `{rel(p, repo_root)}`" for p in py_files] or ["- Ninguno"]
        sections += ["", "### Shell scripts", ""]
        sections += [f"- `{rel(p, repo_root)}`" for p in sh_files] or ["- Ninguno"]
        sections += ["", "### Config files", ""]
        sections += [f"- `{rel(p, repo_root)}`" for p in cfg_files] or ["- Ninguno"]
        sections += ["", "### TODO/FIXME", ""]
        sections += [f"- `{rel(p, repo_root)}`" for p in todos] or ["- Ninguno detectado"]
        sections += [""]

    sections += [
        "## Main Commands",
        "",
        "```bash",
        "python3 scripts/harness/harness.py status",
        "python3 scripts/harness/harness.py context",
        "python3 scripts/harness/harness.py check",
        "python3 scripts/harness/harness.py scan-repo",
        "```",
        "",
    ]

    return "\n".join(sections).rstrip() + "\n"


def write_repo_map(repo_root: Path) -> Path:
    out = repo_root / "scripts" / "harness" / "context" / "repo_map.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_repo_map(repo_root), encoding="utf-8")
    return out
