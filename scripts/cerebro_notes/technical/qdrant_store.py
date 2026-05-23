\
from __future__ import annotations

import uuid
from typing import Any

from .llm import embed
from core.text_utils import chunk_text


def index_markdown_note(
    *,
    qdrant_url: str,
    collection: str,
    ollama_base_url: str,
    embedding_model: str,
    markdown_content: str,
    source_hash: str,
    title: str,
    file_path: str,
    tags: list[str],
    chunk_chars: int,
    chunk_overlap: int,
    timeout_seconds: int,
) -> int:
    """
    Indexa la nota en Qdrant.
    Importa qdrant-client aquí para que el sistema pueda usarse sin Qdrant si vector.enabled=false.
    """
    try:
        from qdrant_client import QdrantClient
        from qdrant_client.models import Distance, PointStruct, VectorParams
    except ImportError as exc:
        raise RuntimeError("Falta qdrant-client. Instala: pip install qdrant-client") from exc

    chunks = chunk_text(markdown_content, chunk_chars=chunk_chars, overlap=chunk_overlap)
    if not chunks:
        return 0

    vectors = embed(
        base_url=ollama_base_url,
        model=embedding_model,
        inputs=chunks,
        timeout_seconds=timeout_seconds,
    )
    if not vectors:
        return 0

    client = QdrantClient(url=qdrant_url)
    existing = [c.name for c in client.get_collections().collections]
    if collection not in existing:
        client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=len(vectors[0]), distance=Distance.COSINE),
        )

    points = []
    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
        point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_hash}:{i}:{file_path}"))
        payload: dict[str, Any] = {
            "source_hash": source_hash,
            "chunk_index": i,
            "title": title,
            "file_path": file_path,
            "tags": tags,
            "text": chunk,
        }
        points.append(PointStruct(id=point_id, vector=vector, payload=payload))

    client.upsert(collection_name=collection, points=points)
    return len(points)
