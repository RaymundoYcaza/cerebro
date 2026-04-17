import shutil
from pathlib import Path

from config import load_config
from efforts.models import EffortTask
from profiles import get_profile_config
from templates import load_template, render_template
from utils import build_filename, now_date, write_note


def _task_line(text: str, priority: str | None, scheduled_date: str | None, done: bool = False) -> str:
    marker = "x" if done else " "
    line = f"- [{marker}] {text.strip()}"
    if priority:
        line += f" ^{priority}"
    if scheduled_date:
        line += f" @{scheduled_date}"
    return line


def _read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def _write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _find_header_index(lines: list[str], header: str) -> int | None:
    needle = f"## {header}"
    for index, line in enumerate(lines):
        if line.strip() == needle:
            return index
    return None


def _ensure_blank_line_before(lines: list[str], index: int) -> None:
    if index > 0 and lines[index - 1].strip() != "":
        lines.insert(index, "")


def create_project(title: str, status: str, created: str | None = None) -> Path:
    config = load_config()
    vault_root = Path(config["vault_root"])
    profile_config = get_profile_config(config, "effort")
    output_dir = vault_root / "Efforts" / status
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = build_filename(
        profile_config["filename_strategy"],
        title,
        config["defaults"]["filename_max_length"],
    )
    destination = output_dir / filename

    template_text = load_template(config, profile_config["template_path"])
    rendered = render_template(
        template_text,
        {
            "created": created or now_date(config["defaults"]["date_format"]),
            "title": title,
            "status": status,
            "up": [],
            "related": [],
        },
    )
    write_note(destination, rendered.rstrip() + "\n")
    return destination


def move_project(project_path: Path, new_status: str) -> Path:
    new_dir = project_path.parent.parent / new_status
    new_dir.mkdir(parents=True, exist_ok=True)
    new_path = new_dir / project_path.name
    shutil.move(str(project_path), str(new_path))
    return new_path


def create_subproject(project_path: Path, name: str) -> None:
    lines = _read_lines(project_path)
    if _find_header_index(lines, name) is not None:
        return

    if lines and lines[-1].strip() != "":
        lines.append("")
    lines.extend([f"## {name}", ""])
    _write_lines(project_path, lines)


def append_task(
    project_path: Path,
    text: str,
    subproject: str | None = None,
    priority: str | None = None,
    scheduled_date: str | None = None,
) -> None:
    line = _task_line(text, priority, scheduled_date)
    lines = _read_lines(project_path)

    if not subproject:
        first_h2 = next((i for i, raw in enumerate(lines) if raw.startswith("## ")), None)
        if first_h2 is None:
            if lines and lines[-1].strip() != "":
                lines.append("")
            lines.append(line)
        else:
            _ensure_blank_line_before(lines, first_h2)
            lines.insert(first_h2, line)
        _write_lines(project_path, lines)
        return

    header_index = _find_header_index(lines, subproject)
    if header_index is None:
        if lines and lines[-1].strip() != "":
            lines.append("")
        lines.extend([f"## {subproject}", line])
        _write_lines(project_path, lines)
        return

    insert_at = header_index + 1
    while insert_at < len(lines) and not lines[insert_at].startswith("## "):
        insert_at += 1
    if insert_at > header_index + 1 and lines[insert_at - 1].strip() != "":
        lines.insert(insert_at, "")
        insert_at += 1
    lines.insert(insert_at, line)
    _write_lines(project_path, lines)


def _replace_task_line(task: EffortTask, new_line: str) -> None:
    lines = _read_lines(task.file)
    if not (0 <= task.line_number < len(lines)):
        raise ValueError("No se pudo ubicar la tarea en el archivo.")
    lines[task.line_number] = new_line
    _write_lines(task.file, lines)


def mark_task_done(task: EffortTask) -> None:
    _replace_task_line(task, _task_line(task.text, task.priority, task.scheduled_date, done=True))


def reschedule_task(task: EffortTask, new_date: str | None) -> None:
    _replace_task_line(task, _task_line(task.text, task.priority, new_date, done=task.done))


def change_task_priority(task: EffortTask, new_priority: str | None) -> None:
    _replace_task_line(task, _task_line(task.text, new_priority, task.scheduled_date, done=task.done))
