---
title: Pretraining data: dedupe and filter
minutes: 50
xp: 50
hint: shingles: clean = "", for c in text.lower(): if c.isalnum() or c.isspace(): clean = clean + c. Then words = clean.split()
hint: shingles continued: result = set(), for i in range(len(words) - n + 1): result.add(tuple(words[i:i + n])), return result
hint: jaccard: if len(a) == 0 and len(b) == 0: return 0.0, then return len(a & b) / len(a | b)
hint: dedupe: for each doc, s = shingles(d), unique = True, and set unique = False if jaccard(s, k) >= threshold for any kept k
---
# Trillions of tokens, mostly cleaning

⏱️ About 50 minutes

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

## 🔬 Take the formula apart

**Shingles** are overlapping word groups. "the cat sat on" with n = 3: ("the", "cat", "sat") and ("cat", "sat", "on"). Two documents that share many shingles share whole phrases.

**Jaccard similarity** <div class="formula">J(a, b) = <span class="k1">|a ∩ b|</span> / <span class="k2">|a ∪ b|</span></div>
- `∩` ("intersection"): what's in **both** sets. `∪` ("union"): what's in **either**.
- `| |` around a set means "how many things in it".
- 0 = nothing shared, 1 = identical.

Numbers: a = {1, 2, 3}, b = {2, 3, 4}. Both: {2, 3} → 2. Either: {1, 2, 3, 4} → 4. J = 2 / 4 = **0.5**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `c.isalnum()` | "is alphanumeric" | true for letters and digits |
| `c.isspace()` | | true for spaces |
| `clean = clean + c` | | build the cleaned text one character at a time |
| `words[i:i + n]` | | n words starting at i |
| `tuple(...)` | | a list turned into a tuple, which a set can hold |
| `result.add(x)` | | add to a set (repeats are ignored) |
| `a & b`, `a | b` | | set intersection ∩ and union ∪ |
| `unique = True` … `unique = False` | | a flag (LLMs 7, lesson 4) |

### 👀 Worked example: shingles of a short text

"The cat sat, on!" → lower and clean: "the cat sat on" → words `["the", "cat", "sat", "on"]`. With n = 3, `range(4 − 3 + 1)` = 0, 1:

1. i = 0: ("the", "cat", "sat")
2. i = 1: ("cat", "sat", "on")

## 🎯 Your quest

`shingles(text, n=3)`: replace `return set()` with:

1. `    clean = ""`
2. `    for c in text.lower():`
3. `        if c.isalnum() or c.isspace():`
4. `            clean = clean + c`
5. `    words = clean.split()`
6. `    result = set()`
7. `    for i in range(len(words) - n + 1):`
8. `        result.add(tuple(words[i:i + n]))`
9. `    return result`

`jaccard(a, b)`: replace `return 0.0` with:

1. `    if len(a) == 0 and len(b) == 0:`
2. `        return 0.0`
3. `    return len(a & b) / len(a | b)`

`dedupe(docs, threshold)`: replace `return docs` with:

1. `    kept = []`
2. `    kept_sh = []`
3. `    for d in docs:`
4. `        s = shingles(d)`
5. `        unique = True`
6. `        for k in kept_sh:`
7. `            if jaccard(s, k) >= threshold:`
8. `                unique = False`
9. `        if unique:`
10. `            kept.append(d)`
11. `            kept_sh.append(s)`
12. `    return kept`

The second document (the same sentence with "!") and the third (one word changed) are dropped.

## Review

<details><summary>Compute-optimal tokens per parameter according to Chinchilla?</summary>About 20.</details>
<details><summary>Why are small models trained far beyond that?</summary>To be cheap at inference: more training makes a small model better, and it's run many times.</details>
