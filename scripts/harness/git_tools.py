from __future__ import annotations

import argparse
import re
import subprocess
import time
import sys
import urllib.error
import urllib.request
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - fallback for minimal envs
    yaml = None

try:
    import requests
except Exception:  # pragma: no cover - fallback when requests is unavailable
    requests = None


HARNESS_DIR = Path(__file__).resolve().parent
REPO_ROOT = HARNESS_DIR.parents[1]
HARNESS_CONFIG = HARNESS_DIR / "config.yaml"
CEREBRO_CONFIG = REPO_ROOT / "scripts" / "cerebro_notes" / "config.yaml"
DB_PATH = HARNESS_DIR / ".memory" / "cerebro_harness.sqlite"
CHANGELOG_PATH = HARNESS_DIR / "CHANGELOG.md"

PROTECTED_BRANCHES = {"main", "master", "develop", "staging", "production"}
ALLOWED_BRANCH_PREFIXES = {
    "feat",
    "fix",
    "refactor",
    "docs",
    "test",
    "chore",
    "ci",
    "perf",
    "style",
    "build",
    "hotfix",
    "experiment",
}
ALLOWED_COMMIT_TYPES = {
    "feat",
    "fix",
    "refactor",
    "docs",
    "test",
    "chore",
    "ci",
    "perf",
    "style",
    "build",
    "revert",
}


class GitToolError(RuntimeError):
    pass


def run_command(command: list[str], *, check: bool = True, timeout: int = 180) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
        timeout=timeout,
    )

    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or f"exit={result.returncode}"
        raise GitToolError(f"{' '.join(command)}: {detail}")

    return result


def git(args: list[str], *, check: bool = True, timeout: int = 180) -> subprocess.CompletedProcess[str]:
    return run_command(["git", *args], check=check, timeout=timeout)


def ensure_git_repo() -> None:
    git(["rev-parse", "--is-inside-work-tree"])


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists() or yaml is None:
        return {}

    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def json_dumps(data: dict[str, Any]) -> str:
    import json

    return json.dumps(data)


def json_loads(text: str) -> dict[str, Any]:
    import json

    data = json.loads(text)
    return data if isinstance(data, dict) else {}


def load_config() -> dict[str, Any]:
    harness = read_yaml(HARNESS_CONFIG)
    cerebro = read_yaml(CEREBRO_CONFIG)

    merged = dict(cerebro)
    for key, value in harness.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            nested = dict(merged[key])
            nested.update(value)
            merged[key] = nested
        else:
            merged[key] = value

    return merged


def current_branch() -> str:
    name = git(["branch", "--show-current"]).stdout.strip()
    if name:
        return name
    return git(["rev-parse", "--short", "HEAD"]).stdout.strip()


def git_dir() -> Path:
    raw = git(["rev-parse", "--git-dir"]).stdout.strip()
    path = Path(raw)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path


def in_progress_operations() -> list[str]:
    gd = git_dir()
    ops: list[str] = []

    if (gd / "MERGE_HEAD").exists():
        ops.append("merge")
    if (gd / "rebase-merge").exists() or (gd / "rebase-apply").exists():
        ops.append("rebase")
    if (gd / "CHERRY_PICK_HEAD").exists():
        ops.append("cherry-pick")

    return ops


def last_commit() -> str:
    result = git(["log", "-1", "--oneline"], check=False)
    if result.returncode != 0:
        return "Sin commits"
    return result.stdout.strip() or "Sin commits"


def porcelain_status() -> list[str]:
    return git(["status", "--porcelain=v1"]).stdout.splitlines()


def classify_status(lines: list[str]) -> dict[str, list[str]]:
    staged: list[str] = []
    modified: list[str] = []
    untracked: list[str] = []

    for line in lines:
        if not line:
            continue

        code = line[:2]
        path = line[3:].strip()

        if code == "??":
            untracked.append(path)
            continue

        if code[0] != " ":
            staged.append(path)

        if code[1] != " ":
            modified.append(path)

    return {
        "staged": staged,
        "modified": modified,
        "untracked": untracked,
    }


def print_list(title: str, items: list[str]) -> None:
    print(f"{title}:")
    if not items:
        print("- Ninguno")
        return
    for item in items:
        print(f"- {item}")


def cmd_status(args: argparse.Namespace) -> None:
    ensure_git_repo()

    lines = porcelain_status()
    classified = classify_status(lines)
    ops = in_progress_operations()

    print("Git status")
    print("==========")
    print(f"Rama actual: {current_branch()}")
    print(f"Estado: {'sucio' if lines else 'limpio'}")
    print(f"Operación en curso: {', '.join(ops) if ops else 'ninguna'}")
    print(f"Último commit: {last_commit()}")
    print()
    print_list("Archivos staged", classified["staged"])
    print()
    print_list("Archivos modificados", classified["modified"])
    print()
    print_list("Archivos untracked", classified["untracked"])


def branch_pattern() -> re.Pattern[str]:
    prefixes = "|".join(sorted(ALLOWED_BRANCH_PREFIXES))
    return re.compile(rf"^({prefixes})/(\d{{14}})\.(\d{{3}})_([a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9])$")


def validate_branch_name(branch: str, config: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    git_cfg = config.get("git_tools", {}) if isinstance(config.get("git_tools"), dict) else {}
    max_branch_chars = int(git_cfg.get("max_branch_chars", 90))
    max_slug_chars = int(git_cfg.get("max_slug_chars", 48))

    if branch in PROTECTED_BRANCHES:
        errors.append(f"rama protegida: {branch}")

    if len(branch) > max_branch_chars:
        errors.append(f"rama demasiado larga: {len(branch)} > {max_branch_chars}")

    match = branch_pattern().match(branch)
    if not match:
        errors.append("formato inválido; esperado prefijo/YYYYMMDDhhmmss.xxx_slug")
        return False, errors

    prefix, timestamp, millis, slug = match.groups()

    if prefix not in ALLOWED_BRANCH_PREFIXES:
        errors.append(f"prefijo no permitido: {prefix}")

    try:
        datetime.strptime(timestamp, "%Y%m%d%H%M%S")
    except ValueError:
        errors.append(f"timestamp inválido: {timestamp}")

    if not millis.isdigit():
        errors.append(f"milisegundos inválidos: {millis}")

    if len(slug) > max_slug_chars:
        errors.append(f"slug demasiado largo: {len(slug)} > {max_slug_chars}")

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9]", slug):
        errors.append(f"slug inválido: {slug}")

    return not errors, errors


def cmd_validate_branch(args: argparse.Namespace) -> None:
    ensure_git_repo()

    config = load_config()
    branch = args.branch or current_branch()
    ok, errors = validate_branch_name(branch, config)

    print(f"Rama evaluada: {branch}")
    if ok:
        print("OK: rama válida")
        return

    print("FAIL: rama inválida")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)


def slugify_branch_name(value: str, max_chars: int) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return (value or "cambio")[:max_chars].strip("-") or "cambio"


def build_branch_name(branch_type: str, name: str, config: dict[str, Any]) -> str:
    git_cfg = config.get("git_tools", {}) if isinstance(config.get("git_tools"), dict) else {}
    max_slug_chars = int(git_cfg.get("max_slug_chars", 48))

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    millis = f"{int(now.microsecond / 1000):03d}"
    slug = slugify_branch_name(name, max_slug_chars)

    return f"{branch_type}/{timestamp}.{millis}_{slug}"


def confirm(prompt: str) -> bool:
    try:
        answer = input(f"{prompt} [y/N]: ").strip().lower()
    except EOFError:
        return False
    return answer in {"y", "yes", "s", "si", "sí"}


def cmd_create_branch(args: argparse.Namespace) -> None:
    ensure_git_repo()

    if args.type not in ALLOWED_BRANCH_PREFIXES:
        raise SystemExit(f"Tipo no permitido: {args.type}")

    config = load_config()
    branch = build_branch_name(args.type, args.name, config)
    ok, errors = validate_branch_name(branch, config)

    print(f"Rama propuesta: {branch}")
    if not ok:
        print("FAIL: rama propuesta inválida")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    if not confirm("Crear esta rama"):
        raise SystemExit("Cancelado.")

    git(["checkout", "-b", branch])
    print(f"OK: rama creada: {branch}")


def diff_numstat() -> list[tuple[int, int, str]]:
    result = git(["diff", "--numstat", "HEAD", "--"], check=False)
    if result.returncode != 0:
        return []

    rows: list[tuple[int, int, str]] = []
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added_raw, deleted_raw, path = parts[0], parts[1], parts[2]
        added = int(added_raw) if added_raw.isdigit() else 0
        deleted = int(deleted_raw) if deleted_raw.isdigit() else 0
        rows.append((added, deleted, path))
    return rows


def diff_name_status() -> list[str]:
    result = git(["diff", "--name-status", "HEAD", "--"], check=False)
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def extension_label(path: str) -> str:
    suffix = Path(path).suffix.lower()
    return suffix or "[sin extension]"


def build_diff_summary_text() -> str:
    rows = diff_numstat()
    name_status = diff_name_status()
    untracked = classify_status(porcelain_status())["untracked"]

    total_added = sum(row[0] for row in rows)
    total_deleted = sum(row[1] for row in rows)
    changed_files = [row[2] for row in rows]
    all_files = changed_files + untracked

    by_ext: dict[str, int] = {}
    for path in all_files:
        by_ext[extension_label(path)] = by_ext.get(extension_label(path), 0) + 1

    lines = [
        "Diff summary",
        "============",
        f"Archivos modificados: {len(all_files)}",
        f"Líneas añadidas: {total_added}",
        f"Líneas eliminadas: {total_deleted}",
        "",
        "Archivos:",
    ]

    if name_status:
        lines.extend(f"- {line}" for line in name_status)
    else:
        lines.append("- Ningún cambio tracked")

    if untracked:
        lines.append("")
        lines.append("Untracked:")
        lines.extend(f"- {path}" for path in untracked)

    lines.append("")
    lines.append("Tipos de archivo:")
    if by_ext:
        for ext, count in sorted(by_ext.items()):
            lines.append(f"- {ext}: {count}")
    else:
        lines.append("- Ninguno")

    lines.append("")
    if all_files:
        dominant = ", ".join(f"{ext} ({count})" for ext, count in sorted(by_ext.items()))
        lines.append(f"Resumen técnico: cambios locales en {len(all_files)} archivo(s), principalmente {dominant}.")
    else:
        lines.append("Resumen técnico: no hay cambios locales para resumir.")

    return "\n".join(lines)


def ollama_config(config: dict[str, Any]) -> dict[str, Any]:
    ollama = config.get("ollama", {}) if isinstance(config.get("ollama"), dict) else {}
    return {
        "base_url": ollama.get("base_url", "http://localhost:11434"),
        "commit_model": ollama.get("commit_model") or ollama.get("chat_model") or "qwen3.5:4b",
        "fallback_model": ollama.get("fallback_model") or ollama.get("fallback_chat_model") or "qwen3.5:cloud",
        "temperature": float(ollama.get("temperature", 0.2)),
        "timeout_seconds": int(ollama.get("timeout_seconds", 180)),
    }


def summarize_error(exc: Exception) -> str:
    text = str(exc).strip().replace("\n", " ")
    return text[:240] if text else exc.__class__.__name__


def extract_ollama_text(raw: dict[str, Any]) -> str:
    message = raw.get("message")
    if isinstance(message, dict):
        content = message.get("content")
        if content:
            return str(content).strip()

    response = raw.get("response")
    if response:
        return str(response).strip()

    return ""


def call_ollama_endpoint(
    *,
    base_url: str,
    endpoint: str,
    model: str,
    prompt: str,
    temperature: float,
    timeout_seconds: int,
) -> str:
    url = base_url.rstrip("/") + endpoint

    if endpoint == "/api/chat":
        body = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un asistente técnico conciso. Devuelve solo un mensaje Conventional Commit.",
                },
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "think": False,
            "options": {"temperature": temperature},
        }
    else:
        body = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "options": {"temperature": temperature},
        }

    raw: dict[str, Any]
    if requests is not None:
        response = requests.post(url, json=body, timeout=timeout_seconds)
        response.raise_for_status()
        raw = response.json()
    else:
        payload = json_dumps(body).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                raw = json_loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body_text = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {exc.code}: {body_text[:240]}") from exc

    return extract_ollama_text(raw)


def ask_ollama(prompt: str, *, debug: bool = False) -> tuple[str | None, dict[str, Any]]:
    metadata: dict[str, Any] = {
        "base_url": None,
        "model": None,
        "endpoint": None,
        "duration_seconds": 0.0,
        "used_fallback": False,
        "error": None,
    }

    config = load_config()
    cfg = ollama_config(config)
    base_url = str(cfg["base_url"])
    metadata["base_url"] = base_url

    models = [str(cfg["commit_model"])]
    fallback_model = str(cfg["fallback_model"]) if cfg.get("fallback_model") else ""
    if fallback_model and fallback_model not in models:
        models.append(fallback_model)

    errors: list[str] = []
    started = time.monotonic()

    for model_index, model in enumerate(models):
        if not model:
            continue

        for endpoint in ["/api/chat", "/api/generate"]:
            metadata["model"] = model
            metadata["endpoint"] = endpoint
            metadata["used_fallback"] = model_index > 0

            try:
                text = call_ollama_endpoint(
                    base_url=base_url,
                    endpoint=endpoint,
                    model=model,
                    prompt=prompt,
                    temperature=float(cfg["temperature"]),
                    timeout_seconds=int(cfg["timeout_seconds"]),
                )
                metadata["duration_seconds"] = round(time.monotonic() - started, 2)
                if text:
                    return text, metadata
                errors.append(f"{model} {endpoint}: respuesta vacía")
            except Exception as exc:
                errors.append(f"{model} {endpoint}: {summarize_error(exc)}")

    metadata["duration_seconds"] = round(time.monotonic() - started, 2)
    metadata["error"] = "; ".join(errors[-4:]) if errors else "Ollama no produjo respuesta"
    return None, metadata


def cmd_diff_summary(args: argparse.Namespace) -> None:
    ensure_git_repo()

    summary = build_diff_summary_text()
    print(summary)

    if args.no_ollama:
        return

    ai, metadata = ask_ollama(
        "Resume brevemente estos cambios Git y sugiere un tipo Conventional Commit permitido.\n\n"
        f"{summary}\n\n"
        "Responde en español en máximo 5 líneas.",
    )
    if ai:
        print()
        print("Resumen Ollama:")
        print(ai)
    elif metadata.get("error"):
        print()
        print(f"Ollama no disponible: {metadata['error']}")


def staged_files() -> list[str]:
    return classify_status(porcelain_status())["staged"]


def validate_commit_message(message: str) -> tuple[bool, str | None]:
    first = message.strip().splitlines()[0] if message.strip() else ""
    match = re.match(r"^([a-z]+)(\([a-z0-9._-]+\))?: .{1,72}$", first)
    if not match:
        return False, "formato esperado: tipo(scope): resumen breve"

    commit_type = match.group(1)
    if commit_type not in ALLOWED_COMMIT_TYPES:
        return False, f"tipo no permitido: {commit_type}"

    return True, None


def clean_commit_message(raw: str) -> str:
    text = raw.strip()

    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", text)
        text = re.sub(r"\s*```$", "", text).strip()

    lines = [line.rstrip() for line in text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    return "\n".join(lines)


def generate_commit_message(summary: str, *, debug: bool = False) -> tuple[str | None, dict[str, Any]]:
    prompt = (
        "Genera SOLO un mensaje Conventional Commit para estos cambios.\n"
        "Tipos permitidos: feat, fix, refactor, docs, test, chore, ci, perf, style, build, revert.\n"
        "Formato exacto:\n\n"
        "tipo(scope): título breve\n\n"
        "- punto 1\n"
        "- punto 2\n\n"
        "No uses JSON. No uses Markdown fenced code blocks. No expliques nada fuera del mensaje.\n\n"
        f"{summary}"
    )
    raw, metadata = ask_ollama(prompt, debug=debug)
    if not raw:
        return None, metadata

    return clean_commit_message(raw), metadata


def manual_commit_message() -> str:
    if not sys.stdin.isatty():
        raise SystemExit("Fallback manual requiere una terminal interactiva.")

    print("Fallback manual. Escribe el título Conventional Commit.")
    print("Ejemplo: chore(harness): corrige generación de commits")
    try:
        subject = input("Título: ").strip()
    except EOFError:
        subject = ""

    print("Cuerpo opcional. Termina con una línea vacía.")
    body_lines: list[str] = []
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if not line.strip():
            break
        body_lines.append(line.rstrip())

    body = "\n".join(body_lines).strip()
    return f"{subject}\n\n{body}" if body else subject


def append_changelog(summary: str, details: str | None = None, files: str | None = None) -> None:
    lines = ["", "## Cambio", "", f"- {summary}"]
    if details:
        lines.append(f"- Detalle: {details}")
    if files:
        lines.append(f"- Archivos: {files}")
    with CHANGELOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def register_harness_change(summary: str, details: str, files: str) -> None:
    sys.path.insert(0, str(HARNESS_DIR))
    try:
        from tools.memory import add_change

        add_change(DB_PATH, summary, details, files)
    except Exception:
        pass
    append_changelog(summary, details, files)


def cmd_commit(args: argparse.Namespace) -> None:
    ensure_git_repo()

    ops = in_progress_operations()
    if ops:
        raise SystemExit(f"No se puede commitear con operación en curso: {', '.join(ops)}")

    staged = staged_files()
    if not staged:
        raise SystemExit("No hay archivos staged. Stagea cambios explícitamente antes de commitear.")

    print("Archivos staged:")
    for path in staged:
        print(f"- {path}")

    print()
    summary = build_diff_summary_text()
    print(summary)

    if not confirm("Continuar con generación de commit"):
        raise SystemExit("Cancelado.")

    message, metadata = generate_commit_message(summary, debug=args.debug)
    if args.debug:
        print()
        print("Debug Ollama:")
        print(f"- base_url: {metadata.get('base_url')}")
        print(f"- modelo: {metadata.get('model')}")
        print(f"- endpoint: {metadata.get('endpoint')}")
        print(f"- duración: {metadata.get('duration_seconds')}s")
        print(f"- usó fallback: {metadata.get('used_fallback')}")

    if not message:
        if metadata.get("error"):
            print(f"Ollama no generó mensaje utilizable: {metadata['error']}")
        message = manual_commit_message()

    ok, error = validate_commit_message(message)
    while not ok:
        print(f"Mensaje inválido: {error}")
        message = manual_commit_message()
        ok, error = validate_commit_message(message)

    print()
    print("Commit propuesto:")
    print("-----------------")
    print(message)

    if not confirm("Ejecutar commit"):
        raise SystemExit("Cancelado.")

    git(["commit", "-m", message])
    register_harness_change(
        summary="Commit creado con git_tools",
        details=message.splitlines()[0],
        files=" ".join(staged),
    )
    print("OK: commit creado y registrado en harness.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Git Safety Tools para Cerebro.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("status", help="Mostrar estado Git seguro.")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("validate-branch", help="Validar nombre de rama.")
    p.add_argument("--branch", help="Rama a validar. Por defecto usa la rama actual.")
    p.set_defaults(func=cmd_validate_branch)

    p = sub.add_parser("create-branch", help="Crear rama validada con confirmación.")
    p.add_argument("--type", required=True, choices=sorted(ALLOWED_BRANCH_PREFIXES))
    p.add_argument("--name", required=True)
    p.set_defaults(func=cmd_create_branch)

    p = sub.add_parser("diff-summary", help="Mostrar resumen de diff local.")
    p.add_argument("--no-ollama", action="store_true", help="No intentar resumen con Ollama.")
    p.set_defaults(func=cmd_diff_summary)

    p = sub.add_parser("commit", help="Crear commit seguro a partir de staged changes.")
    p.add_argument("--debug", action="store_true", help="Mostrar detalles de Ollama durante generación del commit.")
    p.set_defaults(func=cmd_commit)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except GitToolError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
