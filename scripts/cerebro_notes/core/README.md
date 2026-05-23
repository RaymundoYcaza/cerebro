# Core Transaction Utilities

The **transactions** module provides minimal transactional support for file operations used by the Cerebro scripts.

## Functions

- `Transaction`: context‑manager‑like object that records undo actions. If an exception occurs, all recorded undo actions are executed in reverse order.
- `atomic_write_text(path, text, txn=None)`: writes *text* to *path* atomically via a temporary file. If a `Transaction` is supplied, the previous contents (or the file's existence) are recorded so they can be restored on rollback.
- `safe_move_file(src, dst, txn=None)`: moves *src* to *dst* (ensuring a unique destination). When used inside a `Transaction`, the move can be undone on rollback.

These helpers are used by `run_reflective_from_note.py` to ensure that source notes are only moved and new notes are only written when the whole operation succeeds.

## Usage example
```python
from core.transactions import Transaction, atomic_write_text, safe_move_file
from pathlib import Path

src = Path('source.md')
 dst = Path('dest/source.md')

with Transaction() as txn:
    safe_move_file(src, dst, txn)
    atomic_write_text(dst.with_name('new.md'), 'content', txn)
```
If any step raises an exception, the original source file is restored and no new file is left behind.
