# -*- coding: utf-8 -*-
"""
Transactional utilities for safe file operations.
Provides:
- Transaction context manager with rollback support.
- atomic_write_text: write to a temporary file and replace atomically.
- safe_move_file: move a file with rollback capability.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Callable, List, Optional

# Import utilities from the existing codebase where appropriate


class Transaction:
    """Simple transaction manager.

    Records undo actions. On exception, all recorded undo actions are executed
    in reverse order. On successful exit, the actions are cleared.
    """

    def __init__(self) -> None:
        self._undo_actions: List[Callable[[], None]] = []

    def add_undo(self, fn: Callable[[], None]) -> None:
        """Register a callable that reverts a previous operation."""
        self._undo_actions.append(fn)

    def commit(self) -> None:
        """Clear undo actions – commit the transaction."""
        self._undo_actions.clear()

    def rollback(self) -> None:
        """Execute undo actions in reverse order."""
        for fn in reversed(self._undo_actions):
            try:
                fn()
            except Exception as exc:  # pragma: no cover - safety net
                print(f"Rollback action failed: {exc}")
        self._undo_actions.clear()

    def __enter__(self) -> "Transaction":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()


def atomic_write_text(path: Path, text: str, txn: Optional[Transaction] = None) -> None:
    """Write *text* to *path* atomically.

    A temporary file is written in the same directory and then renamed.
    If *txn* is provided, the previous state of *path* is saved so it can be
    restored on rollback.
    """
    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Record undo information if a transaction is active
    if txn is not None:
        if path.exists():
            # Save current content
            old_bytes = path.read_bytes()

            def undo() -> None:
                path.write_bytes(old_bytes)
        else:

            def undo() -> None:
                path.unlink(missing_ok=True)

        txn.add_undo(undo)

    # Write to a temporary file and replace atomically
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def safe_move_file(
    src: Path, dst: Path, overwrite: bool = False, txn: Optional[Transaction] = None
) -> Path:
    """Move *src* to *dst* safely, recording an undo action if *txn* is given.

    The destination is made unique using :func:`unique_path` to avoid
    overwriting existing files.
    Returns the final destination path.
    """
    if not src.exists():
        raise FileNotFoundError(f"Source file does not exist: {src}")

    if dst.exists() and not overwrite:
        raise FileExistsError(f"Destination file already exists: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))

    if txn is not None:
        # Record undo: move the file back to the original location.
        def undo() -> None:
            if dst.exists():
                shutil.move(str(dst), str(src))

        txn.add_undo(undo)

    return dst
