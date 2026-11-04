---
title: Pretraining data: dedupe and filter
xp: 50
---
# Trillions of tokens, mostly cleaning

> **Warm-up:** the web has thousands of copies of the same cookie banner and licence text. What happens to a model trained on all of them?

It memorizes them, wastes compute on them, and repeats them. Building pretraining data is mostly **filtering**. A typical pipeline (as in Hugging Face's FineWeb, 2024, about 15 T tokens from Common Crawl):

1. **Extract** text from raw web pages (drop HTML, menus, ads).
2. **Language ID** and **URL filters** (adult and spam domains).
3. **Quality filters**: rules (too short, too many symbols, too few real words, repeated lines) and **classifier scores** (FineWeb-Edu kept pages a model rated as educational, which trained noticeably better models).
4. **Deduplication**: exact (hash each document) and **near-duplicate**.
5. **Remove personal data** (emails, phone numbers) and benchmark questions, so evaluations aren't contaminated.
6. **Mix** sources (web, code, books, math, papers) in chosen proportions, then tokenize.

**Near-duplicate detection** compares **shingles**: the set of all n-word windows of a document. Two documents are near-duplicates when the **Jaccard similarity** of their shingle sets is high:

```
J(A, B) = |A ∩ B| / |A ∪ B|
```

Comparing every pair is too slow for billions of documents, so real pipelines use **MinHash + LSH**, which estimates J from short signatures and only compares likely candidates. The idea is the same.

## Python you need

Sets: `a & b` (intersection), `a | b` (union), `len(s)`. Words without punctuation: `"".join(c for c in text.lower() if c.isalnum() or c.isspace()).split()`.

## Your quest

1. `shingles(text, n=3)`: lowercase, remove everything except letters, digits and spaces, split into words, return the **set** of n-word tuples.
2. `jaccard(a, b)`: as above; return `0.0` if both are empty.
3. `dedupe(docs, threshold)`: keep a document only if its Jaccard similarity to **every** document kept so far is below `threshold`. Return the kept documents in order.

## Review

<details><summary>Compute-optimal tokens per parameter according to Chinchilla?</summary>About 20.</details>
<details><summary>Why are small models trained far beyond that?</summary>To be cheap at inference: more training makes a small model better, and it's run many times.</details>
