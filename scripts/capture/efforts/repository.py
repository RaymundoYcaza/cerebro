from pathlib import Path

from efforts import STATUS_OPTIONS
from efforts.models import EffortProject, EffortTask, TaskQuery
from efforts.parse import parse_project, parse_tasks


def list_statuses(efforts_dir: Path) -> list[str]:
    statuses = [status for status in STATUS_OPTIONS if (efforts_dir / status).exists()]
    discovered = sorted(
        directory.name
        for directory in efforts_dir.iterdir()
        if directory.is_dir() and not directory.name.startswith(".") and directory.name not in statuses
    ) if efforts_dir.exists() else []
    return statuses + discovered


def list_projects(efforts_dir: Path, status: str | None = None) -> list[EffortProject]:
    if not efforts_dir.exists():
        return []

    search_dir = efforts_dir / status if status else efforts_dir
    if status and not search_dir.exists():
        return []

    projects = []
    for path in sorted(search_dir.rglob("*.md")):
        if ".git" in path.parts:
            continue
        projects.append(parse_project(path))
    return projects


def get_project(path: Path) -> EffortProject:
    return parse_project(path)


def find_tasks(efforts_dir: Path, query: TaskQuery | None = None) -> list[EffortTask]:
    query = query or TaskQuery()
    tasks = []
    for project in list_projects(efforts_dir, status=query.status):
        for task in parse_tasks(project.path):
            if not query.include_done and task.done:
                continue
            if query.project and task.project != query.project:
                continue
            if query.priority and task.priority != query.priority:
                continue
            if query.scheduled_date and task.scheduled_date != query.scheduled_date:
                continue
            if query.text and query.text.lower() not in task.text.lower():
                continue
            tasks.append(task)
    return tasks
