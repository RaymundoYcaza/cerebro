from __future__ import annotations

import argparse
import re
import subprocess
from datetime import date
from pathlib import Path

from tools.repo_scan import write_repo_map
from tools.memory import (
    add_change,
    add_decision,
    add_error,
    add_task,
    complete_task,
    connect,
    get_status,
    init_db,
    list_tasks,
    recent_context,
)


HARNESS_DIR = Path(__file__).resolve().parent
REPO_ROOT = HARNESS_DIR.parents[1]
DB_PATH = HARNESS_DIR / ".memory" / "cerebro_harness.sqlite"
CHANGELOG_PATH = HARNESS_DIR / "CHANGELOG.md"


def append_changelog(summary: str, details: str | None = None, files: str | None = None) -> None:
    lines = ["", "## Cambio", "", f"- {summary}"]

    if details:
        lines.append(f"- Detalle: {details}")

    if files:
        lines.append(f"- Archivos: {files}")

    CHANGELOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with CHANGELOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def read_file_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def cmd_init(args: argparse.Namespace) -> None:
    init_db(DB_PATH)
    add_decision(
        DB_PATH,
        topic="Harness inicial",
        decision="Usar scripts/harness con memoria SQLite y changelog Markdown.",
        rationale="Mantiene el sistema agnóstico, portable y entendible por distintos agentes.",
    )
    add_change(
        DB_PATH,
        summary="Inicialización del harness",
        details="Se creó memoria SQLite y estructura documental base.",
        files="scripts/harness",
    )
    print(f"OK: memoria inicializada en {DB_PATH}")


def cmd_status(args: argparse.Namespace) -> None:
    status = get_status(DB_PATH)

    print("Cerebro Harness")
    print("================")
    print(f"Repo: {REPO_ROOT}")
    print(f"DB:   {DB_PATH}")
    print()
    print(f"Tareas pendientes: {status['pending_tasks']}")
    print(f"Tareas completadas: {status['done_tasks']}")
    print(f"Errores abiertos: {status['open_errors']}")

    print("\nDecisiones recientes:")
    if not status["recent_decisions"]:
        print("- Ninguna")
    for row in status["recent_decisions"]:
        print(f"- [{row['created_at']}] {row['topic']}: {row['decision']}")

    print("\nCambios recientes:")
    if not status["recent_changes"]:
        print("- Ninguno")
    for row in status["recent_changes"]:
        print(f"- [{row['created_at']}] {row['summary']}")


def cmd_remember_decision(args: argparse.Namespace) -> None:
    add_decision(DB_PATH, args.topic, args.decision, args.rationale)
    print("OK: decisión registrada.")


def cmd_add_task(args: argparse.Namespace) -> None:
    add_task(
        DB_PATH,
        title=args.title,
        description=args.description,
        priority=args.priority,
        area=args.area,
        files=args.files,
    )
    print("OK: tarea registrada.")


def cmd_list_tasks(args: argparse.Namespace) -> None:
    rows = list_tasks(DB_PATH, args.status)

    if not rows:
        print("No hay tareas.")
        return

    for row in rows:
        print(
            f"#{row['id']} [{row['status']}] [{row['priority']}] "
            f"{row['title']} | área={row['area'] or '-'} | archivos={row['files'] or '-'}"
        )


def cmd_complete_task(args: argparse.Namespace) -> None:
    complete_task(DB_PATH, args.id)
    print(f"OK: tarea #{args.id} marcada como done.")


def cmd_log_error(args: argparse.Namespace) -> None:
    add_error(
        DB_PATH,
        command=args.command,
        error_text=args.error_text,
        suspected_cause=args.suspected_cause,
        fix_applied=args.fix_applied,
    )
    print("OK: error registrado.")


def cmd_log_change(args: argparse.Namespace) -> None:
    add_change(DB_PATH, args.summary, args.details, args.files)
    append_changelog(args.summary, args.details, args.files)
    print("OK: cambio registrado en SQLite y CHANGELOG.md.")


def cmd_scan_repo(args: argparse.Namespace) -> None:
    out = write_repo_map(REPO_ROOT)
    add_change(
        DB_PATH,
        summary="Repo map actualizado",
        details="Se generó context/repo_map.md mediante scan-repo.",
        files="scripts/harness/context/repo_map.md",
    )
    print(f"OK: repo map generado en {out}")


def cmd_start_session(args: argparse.Namespace) -> None:
    init_db(DB_PATH)
    from tools.memory import now

    with connect(DB_PATH) as conn:
        cur = conn.execute(
            "INSERT INTO sessions (started_at, goal, result) VALUES (?, ?, ?)",
            (now(), args.goal, "active"),
        )
        session_id = cur.lastrowid

    print(f"OK: sesión #{session_id} iniciada.")
    print(f"Goal: {args.goal}")


def cmd_end_session(args: argparse.Namespace) -> None:
    init_db(DB_PATH)
    from tools.memory import now

    with connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY id DESC LIMIT 1"
        ).fetchone()

        if not row:
            raise SystemExit("No hay sesiones activas.")

        session_id = row["id"]

        conn.execute(
            "UPDATE sessions SET ended_at = ?, summary = ?, changed_files = ?, result = ? WHERE id = ?",
            (now(), args.summary, args.changed_files, args.result, session_id),
        )

    add_change(DB_PATH, f"Sesión #{session_id} cerrada", args.summary, args.changed_files)
    append_changelog(f"Sesión #{session_id} cerrada", args.summary, args.changed_files)

    print(f"OK: sesión #{session_id} cerrada.")


def cmd_sessions(args: argparse.Namespace) -> None:
    init_db(DB_PATH)

    with connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, started_at, ended_at, goal, summary, result FROM sessions ORDER BY id DESC LIMIT ?",
            (args.limit,),
        ).fetchall()

    if not rows:
        print("No hay sesiones registradas.")
        return

    for row in rows:
        status = "active" if row["ended_at"] is None else row["result"]
        print(f"#{row['id']} [{status}] {row['started_at']} → {row['ended_at'] or '-'}")
        print(f"  Goal: {row['goal'] or '-'}")
        if row["summary"]:
            print(f"  Summary: {row['summary']}")



def slugify(value: str, max_len: int = 72) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return (value or "spec")[:max_len].strip("-") or "spec"


def specs_root() -> Path:
    return REPO_ROOT / "specs"


def list_markdown_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted(p for p in path.glob("*.md") if p.is_file())


def cmd_specs(args: argparse.Namespace) -> None:
    root = specs_root()
    print("Specs")
    print("=====")
    for status in ["active", "backlog", "done"]:
        folder = root / status
        print()
        print(f"{status}:")
        files = list_markdown_files(folder)
        if not files:
            print("- Ninguna")
            continue
        for path in files:
            print(f"- {path.relative_to(REPO_ROOT)}")


def unique_spec_path(path: Path) -> Path:
    if not path.exists():
        return path
    i = 2
    while True:
        candidate = path.with_name(f"{path.stem}-{i}{path.suffix}")
        if not candidate.exists():
            return candidate
        i += 1


def cmd_new_spec(args: argparse.Namespace) -> None:
    root = specs_root()
    target_dir = root / args.status
    template = root / "templates" / "spec.template.md"

    if args.status not in {"active", "backlog"}:
        raise SystemExit("status debe ser active o backlog")

    target_dir.mkdir(parents=True, exist_ok=True)
    created = date.today().isoformat()
    slug = slugify(args.title)
    filename = f"{created}-{slug}.md"
    out = unique_spec_path(target_dir / filename)

    if template.exists():
        text = template.read_text(encoding="utf-8")
    else:
        text = "# {{title}}\n\nstatus: {{status}}\narea: {{area}}\ncreated: {{created}}\n"

    text = (
        text.replace("{{title}}", args.title.strip())
        .replace("{{area}}", args.area.strip())
        .replace("{{status}}", args.status)
        .replace("{{created}}", created)
    )
    out.write_text(text, encoding="utf-8")

    print(f"OK: spec creada: {out.relative_to(REPO_ROOT)}")


DOCS = [
    ("harness", "scripts/harness/README.md", "visión general del harness"),
    ("harness_usage", "scripts/harness/docs/harness_usage.md", "uso diario del harness"),
    ("git_tools", "scripts/harness/docs/git_tools.md", "herramientas Git seguras"),
    ("git_rules", "scripts/harness/rules/git_rules.md", "reglas Git para agentes"),
    ("specs", "specs/README.md", "flujo de specs"),
    ("reflective", "scripts/cerebro_notes/reflective/README.md", "flujo reflexivo"),
    ("technical", "scripts/cerebro_notes/technical/README.md", "flujo técnico"),
]


def cmd_docs(args: argparse.Namespace) -> None:
    print("Documentación humana")
    print("====================")
    for name, rel_path, description in DOCS:
        path = REPO_ROOT / rel_path
        status = "OK" if path.exists() else "MISSING"
        print(f"- {name}: {rel_path} [{status}] - {description}")


def cmd_check_docs(args: argparse.Namespace) -> None:
    required = {
        "harness": ["scripts/harness/README.md", "scripts/harness/docs/harness_usage.md"],
        "git_tools": ["scripts/harness/docs/git_tools.md", "scripts/harness/rules/git_rules.md"],
        "cerebro_notes reflective": ["scripts/cerebro_notes/reflective/README.md"],
        "cerebro_notes technical": ["scripts/cerebro_notes/technical/README.md"],
        "specs": ["specs/README.md", "specs/templates/spec.template.md", "specs/templates/task.template.md"],
    }

    missing: list[str] = []
    for feature, paths in required.items():
        for rel_path in paths:
            path = REPO_ROOT / rel_path
            if not path.exists() or not path.read_text(encoding="utf-8").strip():
                missing.append(f"{feature}: {rel_path}")

    if missing:
        print("FAIL: documentación requerida faltante")
        for item in missing:
            print(f"- {item}")
        raise SystemExit(1)

    print("OK: documentación mínima presente")



def cmd_context(args: argparse.Namespace) -> None:
    ctx = recent_context(DB_PATH)

    print("# Cerebro Agent Context")
    print()
    print("## Project Brief")
    print(read_file_if_exists(HARNESS_DIR / "context" / "project_brief.md"))
    print()
    print("## Current State")
    print(read_file_if_exists(HARNESS_DIR / "context" / "current_state.md"))
    print()
    print("## Repo Map")
    print(read_file_if_exists(HARNESS_DIR / "context" / "repo_map.md"))
    print()
    print("## Agent Protocol")
    print(read_file_if_exists(HARNESS_DIR / "rules" / "agent_protocol.md"))
    print()
    print("## Recent Decisions")
    if not ctx["decisions"]:
        print("- Ninguna")
    for row in ctx["decisions"]:
        print(f"- {row['topic']}: {row['decision']}")
        if row["rationale"]:
            print(f"  - Razón: {row['rationale']}")

    print()
    print("## Recent Tasks")
    if not ctx["tasks"]:
        print("- Ninguna")
    for row in ctx["tasks"]:
        print(f"- #{row['id']} [{row['status']}] {row['title']}")

    print()
    print("## Recent Changes")
    if not ctx["changes"]:
        print("- Ninguno")
    for row in ctx["changes"]:
        print(f"- {row['summary']}")
        if row["files"]:
            print(f"  - Archivos: {row['files']}")

    print()
    print("## Recent Errors")
    if not ctx["errors"]:
        print("- Ninguno")
    for row in ctx["errors"]:
        print(f"- [{row['status']}] {row['error_text']}")
        if row["suspected_cause"]:
            print(f"  - Causa sospechada: {row['suspected_cause']}")


def run_check_command(label: str, command: list[str], cwd: Path) -> bool:
    print(f"\n[check] {label}")

    result = subprocess.run(
        command,
        cwd=str(cwd),
        text=True,
        capture_output=True,
        timeout=180,
    )

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        print(f"FAIL: {label}")
        return False

    print(f"OK: {label}")
    return True


def cmd_check(args: argparse.Namespace) -> None:
    checks: list[tuple[str, list[str], Path]] = []

    py_files: list[str] = []
    for target in [
        REPO_ROOT / "scripts" / "cerebro_notes",
        REPO_ROOT / "scripts" / "harness",
    ]:
        if target.exists():
            py_files.extend(
                str(p)
                for p in target.rglob("*.py")
                if "__pycache__" not in str(p)
            )

    if py_files:
        checks.append(("py_compile", ["python3", "-m", "py_compile", *py_files], REPO_ROOT))

    check_docs = REPO_ROOT / "scripts" / "harness" / "harness.py"
    checks.append(("harness check-docs", ["python3", str(check_docs), "check-docs"], REPO_ROOT))

    git_tools = REPO_ROOT / "scripts" / "harness" / "git_tools.py"
    if git_tools.exists():
        checks.append(
            (
                "git_tools validate-branch smoke",
                [
                    "python3",
                    str(git_tools),
                    "validate-branch",
                    "--branch",
                    "feat/20260523214730.123_core-obsidian-utils",
                ],
                REPO_ROOT,
            )
        )
        checks.append(
            (
                "git_tools diff-summary smoke",
                ["python3", str(git_tools), "diff-summary", "--no-ollama"],
                REPO_ROOT,
            )
        )

    notes_root = REPO_ROOT / "scripts" / "cerebro_notes"

    if (notes_root / "run_reflective.py").exists():
        checks.append(
            (
                "reflective dry-run smoke",
                [
                    "python3",
                    "run_reflective.py",
                    "--text",
                    "Una idea de prueba para smoke test.",
                    "--config",
                    "config.yaml",
                    "--dry-run",
                    "--nothink",
                ],
                notes_root,
            )
        )

    smoke_root = notes_root / "tests" / "smoke"
    for smoke_name in [
        "test_frontmatter.py",
        "test_obsidian.py",
        "test_search.py",
        "test_reflective_dryrun.py",
    ]:
        smoke_path = smoke_root / smoke_name
        if smoke_path.exists():
            checks.append(
                (
                    f"cerebro_notes smoke {smoke_name}",
                    ["python3", str(smoke_path.relative_to(notes_root))],
                    notes_root,
                )
            )

    if (notes_root / "run_reflective_interactive.py").exists():
        checks.append(
            (
                "reflective interactive help",
                ["python3", "run_reflective_interactive.py", "--help"],
                notes_root,
            )
        )

    if (notes_root / "run_reflective_from_note.py").exists():
        checks.append(
            (
                "reflective from-note help",
                ["python3", "run_reflective_from_note.py", "--help"],
                notes_root,
            )
        )

    failed = 0
    for label, command, cwd in checks:
        if not run_check_command(label, command, cwd):
            failed += 1

    if failed:
        add_error(
            DB_PATH,
            command="harness check",
            error_text=f"{failed} checks fallaron.",
            suspected_cause="Ver salida de harness check.",
        )
        raise SystemExit(1)

    add_change(
        DB_PATH,
        summary="Checks ejecutados correctamente",
        details=f"{len(checks)} checks pasaron.",
        files="scripts/cerebro_notes scripts/harness",
    )

    print(f"\nOK: {len(checks)} checks pasaron correctamente.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Harness local para el repositorio cerebro.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("status")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("remember-decision")
    p.add_argument("--topic", required=True)
    p.add_argument("--decision", required=True)
    p.add_argument("--rationale")
    p.set_defaults(func=cmd_remember_decision)

    p = sub.add_parser("add-task")
    p.add_argument("--title", required=True)
    p.add_argument("--description")
    p.add_argument("--priority", default="normal")
    p.add_argument("--area")
    p.add_argument("--files")
    p.set_defaults(func=cmd_add_task)

    p = sub.add_parser("list-tasks")
    p.add_argument("--status", default="pending", choices=["pending", "done", "all"])
    p.set_defaults(func=cmd_list_tasks)

    p = sub.add_parser("complete-task")
    p.add_argument("--id", type=int, required=True)
    p.set_defaults(func=cmd_complete_task)

    p = sub.add_parser("log-error")
    p.add_argument("--command")
    p.add_argument("--error-text", required=True)
    p.add_argument("--suspected-cause")
    p.add_argument("--fix-applied")
    p.set_defaults(func=cmd_log_error)

    p = sub.add_parser("log-change")
    p.add_argument("--summary", required=True)
    p.add_argument("--details")
    p.add_argument("--files")
    p.set_defaults(func=cmd_log_change)

    p = sub.add_parser("scan-repo")
    p.set_defaults(func=cmd_scan_repo)

    p = sub.add_parser("start-session")
    p.add_argument("--goal", required=True)
    p.set_defaults(func=cmd_start_session)

    p = sub.add_parser("end-session")
    p.add_argument("--summary", required=True)
    p.add_argument("--changed-files")
    p.add_argument("--result", default="done")
    p.set_defaults(func=cmd_end_session)

    p = sub.add_parser("sessions")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_sessions)

    p = sub.add_parser("specs")
    p.set_defaults(func=cmd_specs)

    p = sub.add_parser("new-spec")
    p.add_argument("--title", required=True)
    p.add_argument("--area", required=True)
    p.add_argument("--status", required=True, choices=["active", "backlog"])
    p.set_defaults(func=cmd_new_spec)

    p = sub.add_parser("docs")
    p.set_defaults(func=cmd_docs)

    p = sub.add_parser("check-docs")
    p.set_defaults(func=cmd_check_docs)

    p = sub.add_parser("context")
    p.set_defaults(func=cmd_context)

    p = sub.add_parser("check")
    p.set_defaults(func=cmd_check)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
