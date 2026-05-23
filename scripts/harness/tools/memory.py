from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    topic TEXT NOT NULL,
    decision TEXT NOT NULL,
    rationale TEXT,
    status TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'normal',
    area TEXT,
    files TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    goal TEXT,
    summary TEXT,
    changed_files TEXT,
    result TEXT
);

CREATE TABLE IF NOT EXISTS observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    kind TEXT NOT NULL,
    content TEXT NOT NULL,
    source_file TEXT,
    related_task_id INTEGER
);

CREATE TABLE IF NOT EXISTS errors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    command TEXT,
    error_text TEXT NOT NULL,
    suspected_cause TEXT,
    fix_applied TEXT,
    status TEXT DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS changes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    summary TEXT NOT NULL,
    details TEXT,
    files TEXT
);
"""


def now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Path) -> None:
    with connect(db_path) as conn:
        conn.executescript(SCHEMA)


def add_decision(db_path: Path, topic: str, decision: str, rationale: str | None = None) -> None:
    with connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO decisions (created_at, topic, decision, rationale)
            VALUES (?, ?, ?, ?)
            """,
            (now(), topic, decision, rationale),
        )


def add_task(
    db_path: Path,
    title: str,
    description: str | None = None,
    priority: str = "normal",
    area: str | None = None,
    files: str | None = None,
) -> None:
    timestamp = now()
    with connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO tasks (created_at, updated_at, title, description, priority, area, files)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (timestamp, timestamp, title, description, priority, area, files),
        )


def complete_task(db_path: Path, task_id: int) -> None:
    with connect(db_path) as conn:
        conn.execute(
            """
            UPDATE tasks
            SET status = 'done', updated_at = ?
            WHERE id = ?
            """,
            (now(), task_id),
        )


def add_error(
    db_path: Path,
    command: str | None,
    error_text: str,
    suspected_cause: str | None = None,
    fix_applied: str | None = None,
) -> None:
    with connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO errors (created_at, command, error_text, suspected_cause, fix_applied)
            VALUES (?, ?, ?, ?, ?)
            """,
            (now(), command, error_text, suspected_cause, fix_applied),
        )


def add_change(db_path: Path, summary: str, details: str | None = None, files: str | None = None) -> None:
    with connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO changes (created_at, summary, details, files)
            VALUES (?, ?, ?, ?)
            """,
            (now(), summary, details, files),
        )


def get_status(db_path: Path) -> dict:
    init_db(db_path)

    with connect(db_path) as conn:
        pending_tasks = conn.execute(
            "SELECT COUNT(*) AS n FROM tasks WHERE status = 'pending'"
        ).fetchone()["n"]

        done_tasks = conn.execute(
            "SELECT COUNT(*) AS n FROM tasks WHERE status = 'done'"
        ).fetchone()["n"]

        open_errors = conn.execute(
            "SELECT COUNT(*) AS n FROM errors WHERE status = 'open'"
        ).fetchone()["n"]

        recent_decisions = conn.execute(
            """
            SELECT created_at, topic, decision
            FROM decisions
            ORDER BY id DESC
            LIMIT 5
            """
        ).fetchall()

        recent_changes = conn.execute(
            """
            SELECT created_at, summary
            FROM changes
            ORDER BY id DESC
            LIMIT 5
            """
        ).fetchall()

    return {
        "pending_tasks": pending_tasks,
        "done_tasks": done_tasks,
        "open_errors": open_errors,
        "recent_decisions": recent_decisions,
        "recent_changes": recent_changes,
    }


def list_tasks(db_path: Path, status: str = "pending") -> list[sqlite3.Row]:
    init_db(db_path)

    query = """
    SELECT id, created_at, updated_at, title, status, priority, area, files
    FROM tasks
    """

    params: tuple = ()

    if status != "all":
        query += " WHERE status = ?"
        params = (status,)

    query += " ORDER BY id DESC"

    with connect(db_path) as conn:
        return conn.execute(query, params).fetchall()


def recent_context(db_path: Path) -> dict:
    init_db(db_path)

    with connect(db_path) as conn:
        decisions = conn.execute(
            """
            SELECT created_at, topic, decision, rationale
            FROM decisions
            ORDER BY id DESC
            LIMIT 10
            """
        ).fetchall()

        tasks = conn.execute(
            """
            SELECT id, title, status, priority, area
            FROM tasks
            ORDER BY id DESC
            LIMIT 10
            """
        ).fetchall()

        changes = conn.execute(
            """
            SELECT created_at, summary, details, files
            FROM changes
            ORDER BY id DESC
            LIMIT 10
            """
        ).fetchall()

        errors = conn.execute(
            """
            SELECT created_at, command, error_text, suspected_cause, fix_applied, status
            FROM errors
            ORDER BY id DESC
            LIMIT 5
            """
        ).fetchall()

    return {
        "decisions": decisions,
        "tasks": tasks,
        "changes": changes,
        "errors": errors,
    }
