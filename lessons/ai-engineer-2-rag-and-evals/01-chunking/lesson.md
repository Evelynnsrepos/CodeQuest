---
title: Chunking documents
minutes: 45
xp: 50
hint: chunk_words: first the ValueError check, then words = text.split() and for start in range(0, len(words), size - overlap):
hint: Inside: chunks.append(" ".join(words[start:start + size])), then if start + size >= len(words): break
hint: chunk_sentences: keep current (the sentences so far) and count (their words). If adding the next sentence would go over max_words, save current first
hint: with_meta: for i in range(len(chunks)): out.append({"id": str(doc_id) + "#" + str(i), "doc": doc_id, "text": chunks[i]})
---
# Cut documents into searchable pieces

⏱️ About 45 minutes

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

| You write | Say it | What it does |
|---|---|---|
| `raise ValueError("...")` | "raise a value error" | stops the function with an error message, on purpose |
| `text.split()` | | the list of words |
| `range(0, len(words), size - overlap)` | | the start positions: with size 4 and overlap 1 that's 0, 3, 6, ... |
| `words[start:start + size]` | | a window of `size` words (shorter at the end) |
| `" ".join(window)` | | the words back into one text, with single spaces |
| `break` | | leaves the loop once a window reached the end |
| `re.split(r"(?<=[.!?])\s+", text)` | | cuts the text **after** each `.`, `!` or `?` that is followed by spaces. The `(?<=...)` part means "look behind": the punctuation stays with its sentence. |
| `len(current) > 0` | | "we already have at least one sentence" |
| `str(doc_id) + "#" + str(i)` | | builds ids like `manual#0`, `manual#1` |

### 👀 Worked example: windows with overlap

Ten words, `size` = 4, `overlap` = 1, so each new window starts 4 − 1 = 3 words later:

1. start 0: words 0–3 → `One two three four`. 0 + 4 ≥ 10? No.
2. start 3: words 3–6 → `four five six seven`. The word "four" is in both: that's the overlap.
3. start 6: words 6–9 → `seven eight nine ten`. 6 + 4 ≥ 10? Yes → `break`.

And packing sentences with `max_words` = 6: "Short one." (2 words) goes in. "This is the second sentence here." (6 words): 2 + 6 = 8 > 6, so save `Short one.` as a chunk and start fresh with this sentence.

## 🎯 Your quest

1. `chunk_words(text, size, overlap)`: windows of `size` words that start every `size − overlap` words; each chunk is the words joined by single spaces. The last chunk may be shorter. Stop once a window reaches the end. Raise `ValueError` if `overlap >= size`.
2. `chunk_sentences(text, max_words)`: split into sentences, then pack whole sentences into chunks of at most `max_words` words (a single sentence longer than that becomes its own chunk).
3. `with_meta(doc_id, chunks)`: a list of dicts `{"id": f"{doc_id}#{i}", "doc": doc_id, "text": chunk}`.

**Part 1:** `chunk_words`. Replace `return [text]` with:

1. `if overlap >= size:`
2. `    raise ValueError("overlap must be smaller than size")`
3. `words = text.split()`
4. `chunks = []`
5. `for start in range(0, len(words), size - overlap):`
6. `    chunks.append(" ".join(words[start:start + size]))`
7. `    if start + size >= len(words):`
8. `        break`
9. `return chunks`

**Part 2:** `chunk_sentences`. Replace `return [text]` with:

1. `chunks = []`
2. `current = []`
3. `count = 0`
4. `for sentence in re.split(r"(?<=[.!?])\s+", text.strip()):`
5. `    n = len(sentence.split())`
6. `    if len(current) > 0 and count + n > max_words:`
7. `        chunks.append(" ".join(current))`
8. `        current = []`
9. `        count = 0`
10. `    current.append(sentence)`
11. `    count = count + n`
12. `if len(current) > 0:`
13. `    chunks.append(" ".join(current))`
14. `return chunks`

Lines 12 and 13 save the last chunk, which the loop never got to save.

**Part 3:** `with_meta`. Replace `return []` with:

1. `out = []`
2. `for i in range(len(chunks)):`
3. `    out.append({"id": str(doc_id) + "#" + str(i), "doc": doc_id, "text": chunks[i]})`
4. `return out`

**Remember:** cut at natural borders, overlap a little, keep the source.

## Review

<details><summary>What does R² = 0 mean?</summary>The model is no better than always predicting the average.</details>
