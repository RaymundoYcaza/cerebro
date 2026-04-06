import re
from datetime import datetime
from pathlib import Path


def now_date(fmt="%Y-%m-%d") -> str:
    return datetime.now().strftime(fmt)


def now_timestamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def slugify(text: str, max_length: int = 80) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:max_length] if text else "untitled"


def build_filename(strategy: str, title: str, max_length: int = 80) -> str:
    title_slug = slugify(title, max_length=max_length)
    if strategy == "timestamp-title":
        return f"{now_timestamp()}-{title_slug}.md"
    if strategy == "title":
        return f"{title_slug}.md"
    return f"{now_timestamp()}-{title_slug}.md"


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def write_note(path: Path, content: str):
    ensure_dir(path.parent)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
