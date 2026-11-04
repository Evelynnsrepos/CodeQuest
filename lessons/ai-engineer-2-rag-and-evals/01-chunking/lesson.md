---
title: Chunking documents
xp: 50
---
# Cut documents into searchable pieces

> **Warm-up:** you have a 40-page PDF manual. Why not give the whole thing to the model with every question?

RAG ("retrieval-augmented generation", LLMs 3) means: find the few pieces of your documents that answer the question, and paste only those into the prompt. The pieces are **chunks**.

Chunk size is a trade-off:

| Too small (a sentence) | Too big (a whole page) |
|---|---|
| loses context ("it" refers to what?) | the answer drowns in unrelated text |
| many chunks to search | fewer fit in the prompt; the embedding of a big chunk is a blurry average |

Common starting point: **200–500 words** with **10–20% overlap**, so a sentence cut at a border still appears whole in one of the two neighbours. Better still: cut at natural borders (paragraphs, headings, sentences) and only fall back to word counts for very long ones.

Each chunk keeps **metadata**: which document it came from and where, so the answer can cite its source.

## Python you need

```python
import re
re.split(r"(?<=[.!?])\s+", text)   # split after . ! ? followed by spaces
words[i:i + size]                  # a window of words
```

## Your quest

1. `chunk_words(text, size, overlap)`: windows of `size` words that start every `size − overlap` words; each chunk is the words joined by single spaces. The last chunk may be shorter. Stop once a window reaches the end. Raise `ValueError` if `overlap >= size`.
2. `chunk_sentences(text, max_words)`: split into sentences, then pack whole sentences into chunks of at most `max_words` words (a single sentence longer than that becomes its own chunk).
3. `with_meta(doc_id, chunks)`: a list of dicts `{"id": f"{doc_id}#{i}", "doc": doc_id, "text": chunk}`.

**Remember:** cut at natural borders, overlap a little, keep the source.

## Review

<details><summary>What does R² = 0 mean?</summary>The model is no better than always predicting the average.</details>
