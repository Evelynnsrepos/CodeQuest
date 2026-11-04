---
title: Duplicates and near-duplicates
xp: 55
---
# The same thing, twice

> **Warm-up:** a customer signed up twice, once as "Ada Lovelace" and once as "ada lovelace ". How many customers do you have?

**Exact duplicates** are easy once the text is tidy: build a **key** from the columns that identify a row (for a customer: email; for a training example: the prompt), and keep only the first row with each key.

**Near-duplicates** differ a little: a typo, a word changed, punctuation. For AI training data they matter a lot: the same question 30 times with tiny changes makes the model memorize it, and a near-copy of a test question in the training set makes your evaluation lie.

To find them, measure **similarity** between two texts, from 0 (nothing alike) to 1 (identical). Python has one built in: `difflib.SequenceMatcher(None, a, b).ratio()`. Then call two texts near-duplicates when the ratio is at least a **threshold** like 0.9.

Comparing every pair is slow for big data (n² pairs: 1 million rows = 500 billion pairs). Real pipelines use tricks like MinHash (LLMs 8, lesson 09). For a few thousand rows, pairs are fine.

## Python you need

```python
from difflib import SequenceMatcher
SequenceMatcher(None, "what is a flake", "what is a flake?").ratio()   # 0.968
```

`key(s)` from lesson 03 is given in the starter.

## Your quest

1. `dedupe(rows, cols)`: keep the **first** row for each combination of `key(row[c])` over `cols`, in the original order.
2. `similarity(a, b)`: the `SequenceMatcher` ratio of `key(a)` and `key(b)`.
3. `near_duplicates(texts, threshold=0.9)`: all index pairs `(i, j)` with `i < j` whose similarity is ≥ threshold, in order.

**Remember:** decide which columns make a row "the same" before you delete anything.

## Review

<details><summary>What do you do with category values your map doesn't know?</summary>Collect them, look at them, and extend the map; don't guess.</details>
