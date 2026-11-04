---
title: Keyword search: BM25
xp: 60
---
# When the exact word matters

> **Warm-up:** search your notes for `nix-collect-garbage`. Would an embedding model or plain keyword search find it more reliably?

Embeddings are great at meaning, but weak at **exact terms**: command names, error codes, product numbers, names. Keyword search is the opposite. **BM25** is the standard keyword ranking, used by Elasticsearch and most search engines. For a query, a document's score adds up, for each query word **t**:

**IDF(t) · f · (k₁ + 1) / ( f + k₁ · (1 − b + b · len / avglen) )**

| Piece | Say it | Means |
|---|---|---|
| `f` | "frequency" | how often t appears in this document |
| `IDF(t)` = ln( (N − n + 0.5) / (n + 0.5) + 1 ) | "inverse document frequency" | rare words count more: N documents, n of them contain t |
| `k₁` (1.5) | "k one" | **saturation**: the 10th "nix" adds much less than the 1st |
| `b` (0.75) and `len / avglen` | | long documents are penalized a bit, since they contain more words by chance |

Tokenizing: lowercase and split on anything that isn't a letter, digit, `-` or `_` (so `nix-collect-garbage` stays one word): `re.findall(r"[\w-]+", text.lower())`.

## 🧮 Worked example

Three tiny documents, each 4 words long (so `len / avglen` = 1 and the length penalty cancels out):

1. "nix gc frees disk"  2. "nix flakes pin inputs"  3. "git gc packs objects"

- **Query "nix", document 1.** N = 3 documents, n = 2 contain "nix". IDF = ln( (3 − 2 + 0.5) / (2 + 0.5) + 1 ) = ln(1.6) = **0.47**. The word appears once (f = 1), so the fraction is 1 · 2.5 / (1 + 1.5 · 1) = 1. Score = **0.47**.
- **Query "flakes", document 2.** Only n = 1 document has it. IDF = ln( 2.5 / 1.5 + 1 ) = ln(2.67) = **0.98**. Same fraction, score = **0.98**.

The rare word scores twice as much as the common one. That's BM25's whole idea in one line.

## Your quest

Complete `BM25(docs, k1=1.5, b=0.75)`, where `docs` is a list of strings:

1. In `__init__`: tokenize every doc, store the token lists, `avglen`, `N`, and `df` (for each word, in how many docs it appears).
2. `idf(t)`: the formula above.
3. `score(query, i)`: BM25 score of doc `i` (words not in the doc add 0).
4. `search(query, k=3)`: `(index, score)` pairs of the best `k` docs with score > 0, best first.

**Remember:** embeddings for meaning, BM25 for exact words. Lesson 05 combines them.

## Review

<details><summary>What does a metadata filter do in a vector store?</summary>Restricts the search to items whose fields match, before ranking.</details>
