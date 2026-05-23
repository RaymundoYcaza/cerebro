\
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .config import AppConfig
from .llm import chat_json
from .markdown import render_note
from .qdrant_store import index_markdown_note
from core.tags import normalize_tags
from core.text_utils import compact_for_prompt, normalize_newlines, sha256_short, slugify, unique_path

from core.source_note import move_source_note_to_sources

@dataclass
class PipelineResult:
    title: str
    output_path: Path | None
    markdown: str
    extracted: dict
    tags: list[str]
    model_used: str
    source_hash: str
    vector_points: int = 0


def process_content(
    raw_content: str,
    cfg: AppConfig,
    *,
    source_path: str | None = None,
    write: bool = False,
    dry_run: bool = False,
    think: bool | None = None,
    index: bool = False,
) -> PipelineResult:
    content = normalize_newlines(raw_content)
    source_hash = sha256_short(content)

    prompt_content = compact_for_prompt(content)
    extracted, model_used = chat_json(
        base_url=cfg.ollama.base_url,
        model=cfg.ollama.chat_model,
        fallback_model=cfg.ollama.fallback_chat_model,
        content=prompt_content,
        think=cfg.ollama.think_default if think is None else think,
        temperature=cfg.ollama.temperature,
        timeout_seconds=cfg.ollama.timeout_seconds,
    )

    kind = extracted.get("note_kind", "technical-reference")
    model_main_tags = extracted.get("main_tags", [])
    model_z_tags = extracted.get("z_tags", [])

    # Asegura tag estructural según tipo.
    forced_main = list(cfg.note.default_main_tags)
    if kind == "technical-howto":
        forced_main.append("note/technical/howto")
    elif kind == "technical-troubleshooting":
        forced_main.append("note/technical/troubleshooting")
    elif kind == "technical-reference":
        forced_main.append("note/technical/reference")
    elif kind == "technical-concept":
        forced_main.append("note/technical/concept")
    elif kind == "source-extract":
        forced_main.append("source/extract")

    tag_result = normalize_tags(
        model_main_tags=model_main_tags,
        model_z_tags=model_z_tags,
        default_main_tags=forced_main,
        default_z_tags=cfg.note.default_z_tags,
        allowed_roots=cfg.tag_policy.allowed_roots,
        general_root=cfg.tag_policy.general_root,
        max_main_tags=cfg.tag_policy.max_main_tags,
        max_z_tags=cfg.tag_policy.max_z_tags,
    )

    markdown = render_note(
        extracted=extracted,
        tags=tag_result.tags,
        source_hash=source_hash,
        model_used=model_used,
        source_type=cfg.note.default_source_type,
        review_status=cfg.note.review_status,
        original_content=content,
        source_path=source_path,
        include_original_excerpt=cfg.note.include_original_excerpt,
        max_original_excerpt_chars=cfg.note.max_original_excerpt_chars,
        vector_indexed=False,
        vector_collection=cfg.vector.collection,
    )

    output_path = None
    vector_points = 0

    if write and not dry_run:

        moved_source_path = move_source_note_to_sources(
            source_path=source_path,
            sources_dir=cfg.paths.sources_dir,
        )

        kind_dir_map = {
            "technical-howto": "technical-howto",
            "technical-troubleshooting": "technical-troubleshooting",
            "technical-reference": "technical-reference",
            "technical-concept": "technical-concept",
            "source-extract": "source-extract",
        }

        target_dir = kind_dir_map.get(kind, "technical-reference")

        final_dir = cfg.paths.output_dir / target_dir
        final_dir.mkdir(parents=True, exist_ok=True)

        title = extracted.get("title") or "nota-tecnica"
        filename = f"{slugify(title)}.md"

        output_path = unique_path(final_dir / filename)
        output_path.write_text(markdown, encoding="utf-8")

        if index or cfg.vector.enabled:
            vector_points = index_markdown_note(
                qdrant_url=cfg.vector.qdrant_url,
                collection=cfg.vector.collection,
                ollama_base_url=cfg.ollama.base_url,
                embedding_model=cfg.ollama.embedding_model,
                markdown_content=markdown,
                source_hash=source_hash,
                title=title,
                file_path=str(output_path),
                tags=tag_result.tags,
                chunk_chars=cfg.vector.chunk_chars,
                chunk_overlap=cfg.vector.chunk_overlap,
                timeout_seconds=cfg.ollama.timeout_seconds,
            )

            # Actualiza indicador vector.indexed en el archivo luego de indexar.
            if vector_points > 0:
                markdown = render_note(
                    extracted=extracted,
                    tags=tag_result.tags,
                    source_hash=source_hash,
                    model_used=model_used,
                    source_type=cfg.note.default_source_type,
                    review_status=cfg.note.review_status,
                    original_content=content,
                    source_path=source_path,
                    include_original_excerpt=cfg.note.include_original_excerpt,
                    max_original_excerpt_chars=cfg.note.max_original_excerpt_chars,
                    vector_indexed=True,
                    vector_collection=cfg.vector.collection,
                )
                output_path.write_text(markdown, encoding="utf-8")

    return PipelineResult(
        title=extracted.get("title") or "Nota técnica sin título",
        output_path=output_path,
        markdown=markdown,
        extracted=extracted,
        tags=tag_result.tags,
        model_used=model_used,
        source_hash=source_hash,
        vector_points=vector_points,
    )
