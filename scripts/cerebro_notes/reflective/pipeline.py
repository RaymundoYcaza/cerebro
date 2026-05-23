from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from core.tags import normalize_tags
from core.text_utils import compact_for_prompt, normalize_newlines, sha256_short, slugify, unique_path
from technical.config import AppConfig

from .llm import chat_reflective_json
from .markdown import render_reflective_session


@dataclass
class ReflectivePipelineResult:
    title: str
    output_path: Path | None
    markdown: str
    extracted: dict
    tags: list[str]
    model_used: str
    source_hash: str


def process_reflective_content(
    raw_content: str,
    cfg: AppConfig,
    *,
    write: bool = False,
    dry_run: bool = False,
    think: bool | None = None,
) -> ReflectivePipelineResult:
    content = normalize_newlines(raw_content)
    source_hash = sha256_short(content)
    prompt_content = compact_for_prompt(content)

    extracted, model_used = chat_reflective_json(
        base_url=cfg.ollama.base_url,
        model=cfg.ollama.chat_model,
        fallback_model=cfg.ollama.fallback_chat_model,
        content=prompt_content,
        think=cfg.ollama.think_default if think is None else think,
        temperature=cfg.ollama.temperature,
        timeout_seconds=cfg.ollama.timeout_seconds,
    )

    forced_main = ["note/reflection", "note/atomic"]
    model_main_tags = extracted.get("main_tags", [])
    model_z_tags = extracted.get("z_tags", [])

    tag_result = normalize_tags(
        model_main_tags=model_main_tags,
        model_z_tags=model_z_tags,
        default_main_tags=forced_main,
        default_z_tags=["z/LYT"],
        allowed_roots=cfg.tag_policy.allowed_roots,
        general_root=cfg.tag_policy.general_root,
        max_main_tags=cfg.tag_policy.max_main_tags,
        max_z_tags=cfg.tag_policy.max_z_tags,
    )

    markdown = render_reflective_session(
        extracted=extracted,
        tags=tag_result.tags,
        source_hash=source_hash,
        model_used=model_used,
        original_content=content,
        review_status="guided",
    )

    output_path = None

    if write and not dry_run:
        final_dir = cfg.paths.output_dir / "reflective-session"
        final_dir.mkdir(parents=True, exist_ok=True)

        title = extracted.get("thing_note_candidate") or "nota-reflexiva"
        filename = f"{slugify(title)}.md"

        output_path = unique_path(final_dir / filename)
        output_path.write_text(markdown, encoding="utf-8")

    return ReflectivePipelineResult(
        title=extracted.get("thing_note_candidate") or "Nota reflexiva sin título",
        output_path=output_path,
        markdown=markdown,
        extracted=extracted,
        tags=tag_result.tags,
        model_used=model_used,
        source_hash=source_hash,
    )
