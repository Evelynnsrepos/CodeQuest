---
title: Checkpoint: RAG over your notes, measured
xp: 120
---
# A retriever you can defend with numbers

> **Warm-up:** what three numbers would you show someone to prove your RAG system works?

(Retrieval recall@k and MRR on a golden set; the share of answers with valid citations; and, with a validated judge, answer quality.)

Build a **hybrid** retriever over the starter's `NOTES` and measure it against keyword search and embeddings alone on `GOLDEN`. `BM25`, `LocalEmbedder` and `rrf` from this course are given in the starter, so you can focus on putting them together.

## Your quest

1. `rank_bm25(question)` and `rank_embed(question)`: full rankings of the note ids (best first). For embeddings, fit one `LocalEmbedder` on `TEXTS` (once, outside the function) and rank by the dot product with the question's embedding.
2. `rank_hybrid(question)`: `rrf([rank_bm25(question), rank_embed(question)])`.
3. `report()`: a dict with, for each method `"bm25"`, `"embed"` and `"hybrid"`, a dict `{"recall@3": ..., "mrr": ...}` over `GOLDEN`.

The check wants hybrid recall@3 ≥ 0.9, and at least as good as the better of the other two.

**On your own machine:** swap `LocalEmbedder` for `ollama_embed` with `nomic-embed-text` (lesson 02), point it at your real notes, and write 30 golden questions from things you actually look up. That's a real, measurable RAG system, and the core of the AI engineer 3 capstone.

## Review

<details><summary>Name four things a trace span records.</summary>The step, the tool and its arguments, the result or error, and how long it took.</details>
<details><summary>What do cheap search and reranking each optimize?</summary>Cheap search: recall (don't miss the right chunk). Reranking: precision (put the best first).</details>
