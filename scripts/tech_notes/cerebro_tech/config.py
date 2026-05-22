\
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class PathsConfig:
    cerebro_root: Path
    vault_root: Path
    output_dir: Path
    archive_input_dir: Path
    log_dir: Path


@dataclass
class OllamaConfig:
    base_url: str = "http://localhost:11434"
    chat_model: str = "qwen3.5:0.8b"
    fallback_chat_model: str = "qwen3.5:2b"
    embedding_model: str = "embeddinggemma"
    temperature: float = 0
    think_default: bool = False
    timeout_seconds: int = 180


@dataclass
class NoteConfig:
    default_source_type: str = "technical-note"
    default_main_tags: list[str] = field(default_factory=lambda: ["note/technical"])
    default_z_tags: list[str] = field(default_factory=lambda: ["z/Technical"])
    review_status: str = "pending"
    language: str = "es"
    include_original_excerpt: bool = True
    max_original_excerpt_chars: int = 3500


@dataclass
class TagPolicyConfig:
    allowed_roots: list[str] = field(default_factory=lambda: ["source", "output", "note", "map", "cerebro"])
    general_root: str = "z"
    max_z_tags: int = 12
    max_main_tags: int = 8


@dataclass
class VectorConfig:
    enabled: bool = False
    qdrant_url: str = "http://localhost:6333"
    collection: str = "cerebro_technical_notes"
    chunk_chars: int = 1400
    chunk_overlap: int = 180


@dataclass
class AppConfig:
    paths: PathsConfig
    ollama: OllamaConfig
    note: NoteConfig
    tag_policy: TagPolicyConfig
    vector: VectorConfig


def _path(value: str | Path) -> Path:
    return Path(str(value)).expanduser()


def load_config(config_path: str | Path) -> AppConfig:
    path = Path(config_path)
    raw: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    paths_raw = raw.get("paths", {})
    ollama_raw = raw.get("ollama", {})
    note_raw = raw.get("note", {})
    tag_raw = raw.get("tag_policy", {})
    vector_raw = raw.get("vector", {})

    paths = PathsConfig(
        cerebro_root=_path(paths_raw.get("cerebro_root", "/mnt/c/cerebro")),
        vault_root=_path(paths_raw.get("vault_root", "/mnt/c/cerebro/vault")),
        output_dir=_path(paths_raw.get("output_dir", "/mnt/c/cerebro/vault/00_INBOX_IA/technical")),
        archive_input_dir=_path(paths_raw.get("archive_input_dir", "/mnt/c/cerebro/notas/procesadas_ia")),
        log_dir=_path(paths_raw.get("log_dir", "/mnt/c/cerebro/scripts/cerebro/tech_notes/logs")),
    )

    return AppConfig(
        paths=paths,
        ollama=OllamaConfig(**ollama_raw),
        note=NoteConfig(**note_raw),
        tag_policy=TagPolicyConfig(**tag_raw),
        vector=VectorConfig(**vector_raw),
    )
