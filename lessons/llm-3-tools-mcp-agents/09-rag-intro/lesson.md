---
title: RAG, looking things up instead of retraining
xp: 45
---
# Retrieval-Augmented Generation

> **Warm-up:** you want your model to answer questions about your 300 pages of notes. They don't fit in the context window, and the model was never trained on them. What could you do?

Look up the relevant parts at question time and put only those in the prompt. That's **RAG**:

```
once, ahead of time (indexing):
    split documents into chunks → embed each chunk → store the vectors
for every question (retrieval + generation):
    embed the question → find the most similar chunks → put them in the prompt → ask the model
```

The pieces:

- **Chunking.** Pieces of a few hundred tokens, usually with some **overlap** so a sentence cut at a border still appears whole in one chunk. Too small loses context; too big wastes the window and dilutes the match.
- **Embedding model.** A separate, small model that turns text into a vector so that similar meaning gives similar direction (LLMs 1, lesson 11). Examples: `nomic-embed-text`, `bge-m3`, `Qwen3-Embedding`. LM Studio serves them on `/v1/embeddings`. Questions and chunks must use the **same** embedding model.
- **Retrieval.** Cosine similarity between the question vector and every chunk vector; take the top `k`. With many chunks, a **vector database** (Chroma, Qdrant, pgvector…) does this fast. Production systems often add keyword search (BM25) and a **reranker** model.
- **The prompt.** "Answer using only these excerpts: … Question: …". Asking the model to cite which excerpt it used makes answers checkable.

RAG gives a model **knowledge** without training it, and the knowledge can be updated by editing files. In Module 6 you'll compare it with fine-tuning, and boot.dev's *Learn Retrieval Augmented Generation* course goes much deeper.

Here we use a toy embedding: a vector of word counts. It only matches *exact words*, which shows exactly why real embedding models (which match *meaning*) are better.

## Python you need

`words[i:i + n]` slices a list. `range(0, len(words), step)` counts 0, step, 2·step, … `sorted(items, key=..., reverse=True)` sorts by a score.

## Your quest

1. `chunk(text, size, overlap)`: split `text` into words; make chunks of `size` words, each starting `size - overlap` words after the previous one; join each chunk's words with spaces. Stop once a chunk reaches the end of the text.
2. `retrieve(question, chunks, k)`: return the `k` chunks with the highest `cosine(embed(question), embed(chunk))`, best first.

`embed` and `cosine` are given.

## Review

<details><summary>Protocol error vs tool failure in MCP: how is each reported?</summary>Protocol errors are JSON-RPC errors (like -32601 Method not found). Tool failures are normal results with isError true, so the model can read them.</details>
<details><summary>What does the official Python SDK use to build a tool's schema?</summary>The function's name, docstring and type hints.</details>
<details><summary>Why pin MCP server versions?</summary>Unpinned npx/uvx runs fetch the newest release, so a compromised update would run automatically.</details>
