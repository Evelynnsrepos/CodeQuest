---
title: makemore 1: a bigram model by counting
minutes: 60
xp: 45
hint: count_bigrams: for name in names: s = "." + name + ".", then for i in range(len(s) - 1): a = STOI[s[i]] and b = STOI[s[i + 1]]
hint: count_bigrams, innermost line: N[a][b] = N[a][b] + 1
hint: to_probs: for row in N: total = 0, for c in row: total = total + c + 1. Then new_row = [], for c in row: new_row.append((c + 1) / total), and P.append(new_row)
hint: nll: same two loops as count_bigrams, but total = total - math.log(P[a][b]) and n = n + 1. At the end: return total / n
---
# The simplest language model

⏱️ About 60 minutes

> **Warm-up:** if you could only look at the *previous letter*, how would you guess the next letter of a name?

Count. Andrej Karpathy's *makemore* lectures (episode 2 of *Zero to Hero*) start exactly here: a **character-level bigram model**, which predicts each character from the one before it. Tokens are the 26 letters plus a special `.` that marks both the start and the end of a name, so `"emma"` becomes the pairs:

```
. → e    e → m    m → m    m → a    a → .
```

Count every pair over a list of names in a 27 × 27 table `N`. Row `a` of `N`, divided by its sum, is the **probability distribution of the next character after `a`**. That table *is* the model: generation samples a character from the current row, moves to that row, and repeats until it samples `.`.

Two details that matter for every language model:

- **Smoothing.** A pair never seen in training gets probability 0, and then `log 0 = −∞` breaks the loss. Adding 1 to every count ("add-one smoothing") gives everything a small chance.
- **Evaluation** uses the same loss as any LLM: the average **negative log-likelihood** of the true next characters (LLMs 1, lesson 6; LLMs 4, lesson 10). A model that guesses uniformly among 27 characters scores `log 27 ≈ 3.30`. Lower is better.

## 🔬 Take the formulas apart

**From counts to probabilities, with smoothing**
<div class="formula">P[a][b] = <span class="k1">(N[a][b] + 1)</span> / <span class="k2">(sum of row a, each count + 1)</span></div>

For the names `["ab", "a"]`, the start row `.` has: `. → a` twice, everything else 0.
1. Add 1 to every one of the 27 counts: `a` becomes 3, the other 26 become 1.
2. Row total: 3 + 26 × 1 = **29**.
3. P[.][a] = 3 / 29 ≈ 0.103. P[.][z] = 1 / 29 ≈ 0.034: unseen, but not impossible.

**The loss: average negative log-likelihood**
<div class="formula">NLL = <span class="k1">(1/n)</span> <span class="k2">Σ</span> <span class="k3">−log P[a][b]</span></div>
- <span class="k3">−log P</span> is the "surprise" from LLMs 4, lesson 10: P = 1 → 0, P small → big.
- <span class="k2">Σ</span> over every pair of every name, <span class="k1">(1/n)</span>: divided by the number of pairs.

Numbers: if a model gave every pair probability 1/27, each surprise is −log(1/27) = log 27 ≈ 3.30, and so is the average. Your counting model gets about **2.41**: it learned something.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"." + name + "."` | | `"emma"` → `".emma."` |
| `range(len(s) - 1)` | | positions 0 … second to last, so `s[i + 1]` still exists |
| `s[i]`, `s[i + 1]` | | a character and the one after it: one pair |
| `STOI[ch]` | "s to i" | **s**tring **to** **i**ndex: `STOI["."]` = 0, `STOI["a"]` = 1, … `STOI["z"]` = 26 |
| `N[a][b] = N[a][b] + 1` | | row `a`, column `b` of the table, one more |
| `math.log(x)` | | natural log |
| `total = total - math.log(...)` | | subtracting a log is adding the surprise |

The given `sample` picks the next character with `rng.choices(..., weights=P[i])`, like your `sample` in LLMs 4 lesson 9, until it picks `.`.

### 👀 Worked example: counting the pairs of "emma"

```python
s = ".emma."
for i in range(len(s) - 1):      # i = 0, 1, 2, 3, 4
    print(s[i], "→", s[i + 1])
```

1. `i` = 0: `. → e`
2. `i` = 1: `e → m`
3. `i` = 2: `m → m`
4. `i` = 3: `m → a`
5. `i` = 4: `a → .`

`len(".emma.")` is 6, so `range(5)` stops at 4: exactly the 5 pairs. Each pair adds 1 at `N[STOI[first]][STOI[second]]`.

## 🎯 Your quest

**Part 1:** `count_bigrams(names)`. The empty 27 × 27 table is given. Before `return N`, add:

1. `    for name in names:`
2. `        s = "." + name + "."`
3. `        for i in range(len(s) - 1):`
4. `            a = STOI[s[i]]`
5. `            b = STOI[s[i + 1]]`
6. `            N[a][b] = N[a][b] + 1`

**Part 2:** `to_probs(N)`. Between `P = []` and `return P`, add:

1. `    for row in N:`
2. `        total = 0`
3. `        for c in row:`
4. `            total = total + c + 1`
5. `        new_row = []`
6. `        for c in row:`
7. `            new_row.append((c + 1) / total)`
8. `        P.append(new_row)`

**Part 3:** `nll(P, names)`. Replace `return 0` with:

1. `    total = 0.0`
2. `    n = 0`
3. `    for name in names:`
4. `        s = "." + name + "."`
5. `        for i in range(len(s) - 1):`
6. `            a = STOI[s[i]]`
7. `            b = STOI[s[i + 1]]`
8. `            total = total - math.log(P[a][b])`
9. `            n = n + 1`
10. `    return total / n`

It prints 31 for `a → n`, an NLL of 2.406, and six odd "names".

## Review

<details><summary>Write the AdamW update for one weight.</summary>m = β₁m + (1−β₁)g; v = β₂v + (1−β₂)g²; bias-correct both; p = p − lr·wd·p − lr·m̂/(√v̂ + ε).</details>
<details><summary>Why use LR warmup?</summary>Early on, Adam's running statistics are unreliable; ramping the LR up avoids huge bad steps.</details>
