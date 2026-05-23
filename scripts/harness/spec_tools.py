#!/usr/bin/env python3
"""Spec management CLI for Cerebro harness.
Supports listing, moving, progress reporting, and completing microtasks.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

VALID_STATES = {"backlog", "active", "done", "cancelled"}
SPEC_ROOT = Path("specs")


def error(msg: str) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)


def resolve_spec_path(spec: str) -> Path:
    p = Path(spec)
    if not str(p).startswith(str(SPEC_ROOT)):
        error("Spec path must be inside the 'specs/' directory.")
    if p.suffix != ".md":
        error("Spec file must have a .md extension.")
    if not p.is_file():
        error(f"Spec file does not exist: {spec}")
    return p


def ensure_state_dir(state: str) -> Path:
    if state not in VALID_STATES:
        error(f"Invalid state '{state}'. Valid states: {', '.join(VALID_STATES)}")
    d = SPEC_ROOT / state
    d.mkdir(parents=True, exist_ok=True)
    return d


def read_lines(path: Path):
    return path.read_text(encoding="utf-8").splitlines()


def write_lines(path: Path, lines, dry_run: bool):
    if dry_run:
        print(f"[dry-run] Would write to {path}")
        return
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_estado_line(lines, new_state: str):
    pattern = re.compile(r"^\s*Estado:\s*.*", re.IGNORECASE)
    for i, line in enumerate(lines):
        if pattern.match(line):
            lines[i] = f"Estado: {new_state}"
            return lines
    # No existing line, insert after first title
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#"):
            lines.insert(i + 1, f"Estado: {new_state}")
            return lines
    # No title, prepend
    lines.insert(0, f"Estado: {new_state}")
    return lines


def cmd_list(args):
    results = []
    states = [args.state] if args.state else list(VALID_STATES)
    for state in states:
        dir_path = SPEC_ROOT / state
        if not dir_path.is_dir():
            continue
        for entry in dir_path.iterdir():
            if entry.is_file() and entry.suffix == ".md":
                rel = str(entry)
                results.append({"path": rel, "state": state})
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for item in results:
            print(f"{item['path']}  [{item['state']}]")


def cmd_move(args):
    src = resolve_spec_path(args.spec)
    dest_state = args.to
    if dest_state not in VALID_STATES:
        error(f"Invalid destination state '{dest_state}'.")
    dest_dir = ensure_state_dir(dest_state)
    dest = dest_dir / src.name
    if dest.exists():
        error(f"Destination file already exists: {dest}")
    # Update Estado line
    lines = read_lines(src)
    lines = update_estado_line(lines, dest_state)
    write_lines(src, lines, args.dry_run)
    if not args.dry_run:
        src.rename(dest)
        print(f"Moved {src} -> {dest}")
    else:
        print(f"[dry-run] Would move {src} -> {dest}")


def parse_microtasks(lines):
    mt_pattern = re.compile(r"^##\s+(MT-\d+)")
    checkbox_pattern = re.compile(r"^\s*- \[( |x)\]")
    tasks = {}
    current = None
    for line in lines:
        m = mt_pattern.match(line)
        if m:
            current = m.group(1)
            tasks[current] = {"total": 0, "done": 0}
            continue
        if current:
            cb = checkbox_pattern.match(line)
            if cb:
                tasks[current]["total"] += 1
                if cb.group(1) == "x":
                    tasks[current]["done"] += 1
    return tasks


def cmd_progress(args):
    spec_path = resolve_spec_path(args.spec)
    lines = read_lines(spec_path)
    tasks = parse_microtasks(lines)
    total_mts = len(tasks)
    total_checks = sum(t["total"] for t in tasks.values())
    done_checks = sum(t["done"] for t in tasks.values())
    result = {
        "spec": str(spec_path),
        "microtasks": total_mts,
        "checkboxes": {"total": total_checks, "done": done_checks},
        "detail": tasks,
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Spec: {spec_path}")
        print(f"Microtasks detected: {total_mts}")
        print(f"Checkboxes - total: {total_checks}, done: {done_checks}")
        if total_checks:
            pct = (done_checks / total_checks) * 100
            print(f"Progress: {pct:.1f}%")


def cmd_complete_task(args):
    spec_path = resolve_spec_path(args.spec)
    task_id = args.task.upper()
    lines = read_lines(spec_path)
    mt_header = f"## {task_id}"
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower() == mt_header.lower():
            start = i + 1
            break
    if start is None:
        error(f"Microtask '{task_id}' not found in spec.")
    # Determine end: next MT heading or EOF
    end = len(lines)
    mt_pattern = re.compile(r"^##\s+MT-\d+")
    for j in range(start, len(lines)):
        if mt_pattern.match(lines[j]):
            end = j
            break
    changed = False
    checkbox_pat = re.compile(r"^(\s*- \[) \](.*)")
    for i in range(start, end):
        m = checkbox_pat.match(lines[i])
        if m:
            # replace unchecked with checked
            lines[i] = f"{m.group(1)}x]{m.group(2)}"
            changed = True
    if not changed:
        print("No unchecked boxes to complete in the specified microtask.")
        return
    write_lines(spec_path, lines, args.dry_run)
    if not args.dry_run:
        print(f"Microtask {task_id} checkboxes marked as done in {spec_path}")
    else:
        print(f"[dry-run] Would mark checkboxes in {task_id} as done.")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="spec_tools", description="Manage spec lifecycle."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    # list
    p_list = sub.add_parser("list", help="List specs")
    p_list.add_argument("--state", choices=sorted(VALID_STATES), help="Filter by state")
    p_list.add_argument("--json", action="store_true", help="JSON output")
    p_list.set_defaults(func=cmd_list)
    # move
    p_move = sub.add_parser("move", help="Move spec to another state")
    p_move.add_argument("--spec", required=True, help="Path to spec file")
    p_move.add_argument(
        "--to", required=True, choices=sorted(VALID_STATES), help="Destination state"
    )
    p_move.add_argument(
        "--dry-run", action="store_true", help="Show actions without modifying files"
    )
    p_move.set_defaults(func=cmd_move)
    # progress
    p_prog = sub.add_parser("progress", help="Show progress of a spec")
    p_prog.add_argument("--spec", required=True, help="Path to spec file")
    p_prog.add_argument("--json", action="store_true", help="JSON output")
    p_prog.set_defaults(func=cmd_progress)
    # complete-task
    p_ct = sub.add_parser(
        "complete-task", help="Mark all checkboxes in a microtask as done"
    )
    p_ct.add_argument("--spec", required=True, help="Path to spec file")
    p_ct.add_argument("--task", required=True, help="Microtask ID like MT-01")
    p_ct.add_argument(
        "--dry-run", action="store_true", help="Show actions without modifying files"
    )
    p_ct.set_defaults(func=cmd_complete_task)
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
