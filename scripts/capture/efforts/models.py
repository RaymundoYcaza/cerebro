from dataclasses import dataclass
from pathlib import Path


@dataclass
class EffortTask:
    file: Path
    project: str
    status: str
    subproject: str | None
    text: str
    done: bool
    priority: str | None
    scheduled_date: str | None
    line_number: int
    raw_line: str


@dataclass
class EffortProject:
    path: Path
    title: str
    status: str
    subprojects: list[str]


@dataclass
class TaskQuery:
    status: str | None = None
    project: str | None = None
    priority: str | None = None
    scheduled_date: str | None = None
    text: str | None = None
    include_done: bool = False
