from typing import Tuple, Dict, List

import gzip
import json
import numpy as np

from blueness import module
from bluer_objects import objects

from bluer_agent import NAME
from bluer_agent.rag.corpus.embed import embed_fn
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def query(
    object_name: str,
    query: str,
    *,
    top_k: int = 5,
) -> Tuple[bool, Dict]:
    logger.info(f'{NAME}.query[{object_name}]("{query}")')

    # --- load roots ---
    roots_vec = np.load(
        objects.path_of(object_name=object_name, filename="roots.embeddings.npy")
    )

    with gzip.open(
        objects.path_of(object_name=object_name, filename="roots.meta.json.gz"),
        "rt",
        encoding="utf-8",
    ) as f:
        roots_meta = json.loads(f.read())

    roots = roots_meta["roots"]

    # --- embed query ---
    q_vec = np.asarray(embed_fn([query])[0], dtype=np.float32)

    # --- pick best root ---
    scores = [_cosine(q_vec, v) for v in roots_vec]
    best_root_idx = int(np.argmax(scores))
    best_root = roots[best_root_idx]

    logger.info(f"selected root = {best_root}")

    # --- load corpus embeddings ---
    corpus_vec = np.load(
        objects.path_of(object_name=object_name, filename="corpus.embeddings.npy")
    )

    corpus_meta_file = objects.path_of(
        object_name=object_name, filename="corpus.meta.jsonl.gz"
    )
    corpus_text_file = objects.path_of(
        object_name=object_name, filename="corpus.jsonl.gz"
    )

    candidates: List[Tuple[float, dict]] = []

    with gzip.open(corpus_meta_file, "rt", encoding="utf-8") as meta_f, gzip.open(
        corpus_text_file, "rt", encoding="utf-8"
    ) as text_f:
        for i, (meta_line, text_line) in enumerate(zip(meta_f, text_f)):
            meta = json.loads(meta_line)
            if meta.get("root") != best_root:
                continue

            record = json.loads(text_line)
            score = _cosine(q_vec, corpus_vec[i])

            candidates.append(
                (
                    score,
                    {
                        "url": meta["url"],
                        "chunk_id": meta["chunk_id"],
                        "text": record["text"],
                    },
                )
            )

    candidates.sort(key=lambda x: x[0], reverse=True)
    top = candidates[:top_k]

    chunks = [
        {
            "url": item["url"],
            "chunk_id": item["chunk_id"],
            "score": round(score, 4),
            "text": item["text"],
        }
        for score, item in top
    ]

    for chunk in chunks:
        logger.info(
            "#{} - {}: {:.2f}\n{}".format(
                chunk["chunk_id"],
                chunk["url"],
                chunk["score"],
                chunk["text"][:300],
            )
        )

    context = {
        "root": best_root,
        "chunks": chunks,
    }

    return True, context
