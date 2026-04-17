import re
from pathlib import Path

from efforts.models import EffortProject, EffortTask

TASK_RE = re.compile(r"^- \[( |x)\]\s+(.*)$")
HEADER_RE = re.compile(r"^##\s+(.+)$")
PRIORITY_RE = re.compile(r"\s+\^(alta|media|baja)\b", re.IGNORECASE)
DATE_RE = re.compile(r"\s+@(\d{4}-\d{2}-\d{2})\b")


def parse_project(path: Path) -> EffortProject:
    lines = path.read_text(encoding="utf-8").splitlines()
    subprojects = []
    for line in lines:
        match = HEADER_RE.match(line)
        if match:
            subprojects.append(match.group(1).strip())
    return EffortProject(
        path=path,
        title=path.stem,
        status=path.parent.name,
        subprojects=subprojects,
    )


def parse_tasks(path: Path) -> list[EffortTask]:
    tasks = []
    current_subproject = None
    lines = path.read_text(encoding="utf-8").splitlines()

    for index, line in enumerate(lines):
        header_match = HEADER_RE.match(line)
        if header_match:
            current_subproject = header_match.group(1).strip()
            continue

        task_match = TASK_RE.match(line)
        if not task_match:
            continue

        done = task_match.group(1) == "x"
        body = task_match.group(2).strip()

        priority_match = PRIORITY_RE.search(body)
        priority = priority_match.group(1).lower() if priority_match else None

        date_match = DATE_RE.search(body)
        scheduled_date = date_match.group(1) if date_match else None

        text = PRIORITY_RE.sub("", body)
        text = DATE_RE.sub("", text).strip()

        tasks.append(
            EffortTask(
                file=path,
                project=path.stem,
                status=path.parent.name,
                subproject=current_subproject,
                text=text,
                done=done,
                priority=priority,
                scheduled_date=scheduled_date,
                line_number=index,
                raw_line=line,
            )
        )

    return tasks
