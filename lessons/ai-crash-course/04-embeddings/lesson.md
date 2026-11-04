---
title: Embeddings: meaning as numbers
xp: 25
---
# Similar meaning, nearby vectors

> **Warm-up:** "cat" and "kitten" look different as text. How could a computer know they're related?

An **embedding** turns a word, sentence or image into a list of numbers (a **vector**), arranged so that similar meanings end up pointing in similar directions. Search engines, recommendation systems and RAG (lesson 07) all run on this.

To compare two vectors, use **cosine similarity**: 1 = same direction (same meaning), 0 = unrelated, −1 = opposite.

**cos(a, b) = (a · b) / (|a| · |b|)**

- `a · b` ("dot product"): multiply matching numbers and add them up.
- `|a|` ("length"): the square root of the sum of squares.

```
a = [1, 2]  b = [2, 4]   a·b = 2 + 8 = 10   |a| = √5   |b| = √20   cos = 10 / 10 = 1
```

**Go deeper:** LLMs 1 lesson 11, LLMs 3 (RAG), Math 2 lessons 03–05, AI engineer 2.

## Your quest

1. `cosine(a, b)`.
2. `closest(query, items)`: `items` is a dict name → vector. Return the name with the highest cosine to `query`.

**Remember:** meaning becomes direction; cosine measures it.
