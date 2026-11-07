---
title: Keyword search: BM25
minutes: 55
xp: 60
hint: __init__: for d in docs: words = tokenize(d), self.tokens.append(words), self.tf.append(Counter(words))
hint: __init__: avglen is the total of all token-list lengths divided by self.N. df: for words in self.tokens: for w in set(words): self.df[w] = self.df[w] + 1
hint: idf: n = self.df.get(t, 0), then return math.log((self.N - n + 0.5) / (n + 0.5) + 1)
hint: score: for each query word t: f = self.tf[i].get(t, 0), and if f > 0: add idf · f · (k1 + 1) / (f + k1 · norm)
hint: search: collect (i, score) pairs with score > 0, then pick the best one k times (best-so-far), removing each pick
---
# When the exact word matters

⏱️ About 55 minutes

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

## 🔬 The IDF, in small steps

`ln` is the **natural logarithm**: it asks "e to the power of what gives this number?" (e ≈ 2.718). ln(1) = 0, ln(e) = 1, ln(1.6) = 0.47. In Python: `math.log(x)`.

For "nix" in the worked example below: N = 3, n = 2.

1. Top: N − n + 0.5 = 3 − 2 + 0.5 = **1.5**.
2. Bottom: n + 0.5 = 2 + 0.5 = **2.5**.
3. 1.5 / 2.5 = 0.6, plus 1 = **1.6**.
4. ln(1.6) = **0.47**.

The fewer documents have the word (smaller n), the bigger the top and the smaller the bottom, so the IDF grows.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `Counter(words)` | | counts each word: `Counter(["a", "b", "a"])` is `{"a": 2, "b": 1}` |
| `self.tf[i].get(t, 0)` | | how often word t is in document i (0 if never) |
| `Counter()` then `self.df[w] = self.df[w] + 1` | | an empty counter; a missing word counts as 0, so `+ 1` just works |
| `set(words)` | | each word once, so a word repeated in one document still counts as **one** document |
| `math.log(x)` | | ln(x) |
| `scored.remove(top)` | | takes that pair out of the list, so the next round finds the next best |

## 🧮 Worked example
Three tiny documents, each 4 words long (so `len / avglen` = 1 and the length penalty cancels out):

1. "nix gc frees disk"  2. "nix flakes pin inputs"  3. "git gc packs objects"

- **Query "nix", document 1.** N = 3 documents, n = 2 contain "nix". IDF = ln( (3 − 2 + 0.5) / (2 + 0.5) + 1 ) = ln(1.6) = **0.47**. The word appears once (f = 1), so the fraction is 1 · 2.5 / (1 + 1.5 · 1) = 1. Score = **0.47**.
- **Query "flakes", document 2.** Only n = 1 document has it. IDF = ln( 2.5 / 1.5 + 1 ) = ln(2.67) = **0.98**. Same fraction, score = **0.98**.

The rare word scores twice as much as the common one. That's BM25's whole idea in one line.

## 🎯 Your quest

Complete `BM25(docs, k1=1.5, b=0.75)`, where `docs` is a list of strings:

1. In `__init__`: tokenize every doc, store the token lists, `avglen`, `N`, and `df` (for each word, in how many docs it appears).
2. `idf(t)`: the formula above.
3. `score(query, i)`: BM25 score of doc `i` (words not in the doc add 0).
4. `search(query, k=3)`: `(index, score)` pairs of the best `k` docs with score > 0, best first.

**Part 1:** `__init__`. Under `self.b = b`, type:

1. `self.tokens = []`
2. `self.tf = []`
3. `for d in docs:`
4. `    words = tokenize(d)`
5. `    self.tokens.append(words)`
6. `    self.tf.append(Counter(words))`
7. `self.N = len(docs)`
8. `total = 0`
9. `for words in self.tokens:`
10. `    total = total + len(words)`
11. `self.avglen = total / self.N`
12. `self.df = Counter()`
13. `for words in self.tokens:`
14. `    for w in set(words):`
15. `        self.df[w] = self.df[w] + 1`

**Part 2:** `idf`. Replace `return 0.0` with:

1. `n = self.df.get(t, 0)`
2. `return math.log((self.N - n + 0.5) / (n + 0.5) + 1)`

**Part 3:** `score`. Replace `return 0.0` with:

1. `length = len(self.tokens[i])`
2. `total = 0.0`
3. `for t in tokenize(query):`
4. `    f = self.tf[i].get(t, 0)`
5. `    if f > 0:`
6. `        norm = 1 - self.b + self.b * length / self.avglen`
7. `        total = total + self.idf(t) * f * (self.k1 + 1) / (f + self.k1 * norm)`
8. `return total`

**Part 4:** `search`. Replace `return []` with:

1. `scored = []`
2. `for i in range(self.N):`
3. `    s = self.score(query, i)`
4. `    if s > 0:`
5. `        scored.append((i, s))`
6. `best = []`
7. `for step in range(k):`
8. `    if len(scored) == 0:`
9. `        break`
10. `    top = scored[0]`
11. `    for pair in scored:`
12. `        if pair[1] > top[1]:`
13. `            top = pair`
14. `    best.append(top)`
15. `    scored.remove(top)`
16. `return best`

**Remember:** embeddings for meaning, BM25 for exact words. Lesson 05 combines them.

## Review

<details><summary>What does a metadata filter do in a vector store?</summary>Restricts the search to items whose fields match, before ranking.</details>
