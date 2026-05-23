"""Smoke tests for transactional utilities.

These tests ensure that atomic_write_text and safe_move_file correctly
roll back changes when an exception occurs.
"""

import os
import tempfile
from pathlib import Path

from core.transactions import Transaction, atomic_write_text, safe_move_file


def test_atomic_write_rollback() -> None:
    with tempfile.TemporaryDirectory() as td:
        target = Path(td) / "note.txt"
        # No file initially
        try:
            with Transaction() as txn:
                atomic_write_text(target, "hello", txn)
                raise RuntimeError("trigger rollback")
        except RuntimeError:
            pass
        # After rollback the file must not exist
        assert not target.exists()


def test_safe_move_rollback() -> None:
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "src.txt"
        src.write_text("data", encoding="utf-8")
        dst_dir = Path(td) / "dest"
        dst_dir.mkdir()
        dst = dst_dir / "src.txt"
        try:
            with Transaction() as txn:
                safe_move_file(src, dst, txn)
                raise RuntimeError("trigger rollback")
        except RuntimeError:
            pass
        # After rollback source should still exist and destination should not
        assert src.exists()
        assert not dst.exists()
