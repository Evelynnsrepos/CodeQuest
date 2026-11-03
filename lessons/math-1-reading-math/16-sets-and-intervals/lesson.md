---
title: Sets, ∈ and intervals
xp: 35
---
# Collections and ranges

> **Warm-up:** a paper says "p ∈ [0, 1]" and "x ∈ ℝ⁴⁰⁹⁶". Without knowing the signs, can you guess what kind of statement each one is?

**In one sentence:** a set is a collection of things, `∈` means "is in", and an interval is a range of numbers with or without its ends.

## 🪜 Plain words

A **set** is a bag of things with no duplicates and no order: the set of vowels is {a, e, i, o, u}. You can ask "is this thing in the bag?".

An **interval** is a stretch of the number line, "all numbers from here to there". The only tricky part: are the two **ends** included or not? "From 0 up to, but not including, 1" is different from "0 to 1, both included".

## 🪜 With numbers

- Is 3 in {1, 2, 3}? Yes. Is 4? No.
- "Between 0 and 1, both ends included": 0 yes, 0.5 yes, 1 yes, 1.2 no.
- "From 0 up to but not including 1": 0 yes, 0.999 yes, **1 no**.
- A probability must always be between 0 and 1, ends included.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `{1, 2, 3}` | "the set one, two, three" | a collection | `{1, 2, 3}` |
| `x ∈ A` | "x is in A" | membership | `x in A` |
| `x ∉ A` | "x is not in A" | | `x not in A` |
| `A ∪ B` | "A union B" | everything in A or B | `A \| B` |
| `A ∩ B` | "A intersect B" | only what's in both | `A & B` |
| `∅` | "the empty set" | an empty bag | `set()` |
| `ℝ` | "the reals" | every number on the number line | |
| `ℝⁿ` | "R n" | all lists of n numbers | a list of n floats |
| `[a, b]` | "closed interval a to b" | ends **included**: a ≤ x ≤ b | `a <= x <= b` |
| `(a, b)` | "open interval a to b" | ends **excluded**: a < x < b | `a < x < b` |
| `[a, b)` | "half-open" | a included, b excluded | `a <= x < b` |
| `∀` | "for all" | every one | `all(...)` |
| `∃` | "there exists" | at least one | `any(...)` |

Python's `range(a, b)` is like `[a, b)`: start included, end excluded.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">p</span> <span class="k2">∈</span> <span class="k3">[</span><span class="k4">0, 1</span><span class="k5">)</span></div>

| Piece | Say it | Means | Is p = 1 allowed? |
|---|---|---|---|
| <span class="k1">p</span> | "p" | the number we're talking about | |
| <span class="k2">∈</span> | "is in" | belongs to | |
| <span class="k3">[</span> | "closed on the left" | 0 **is** included | |
| <span class="k4">0, 1</span> | "zero to one" | the two ends | |
| <span class="k5">)</span> | "open on the right" | 1 is **not** included | **no** |

<div class="formula"><span class="k1">∀ i</span><span class="k2">:</span> <span class="k3">pᵢ ≥ 0</span></div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">∀ i</span> | "for all i" | for every position i |
| <span class="k2">:</span> | "it holds that" / "such that" | |
| <span class="k3">pᵢ ≥ 0</span> | "p i is at least zero" | every probability is not negative |

## 🔀 What if the formula were different?

<div class="wrong"><b>p ∈ (0, 1)</b> instead of [0, 1]: a model could never be 100% or 0% sure. Sometimes that's on purpose (sigmoid's output is (0, 1)), but for probabilities in general it's wrong.</div>
<div class="wrong"><b>∃ i: pᵢ ≥ 0</b> ("there exists" instead of "for all"): only one probability needs to be non-negative; the rest could be −5. Not a valid distribution.</div>
<div class="right"><b>∀ i: pᵢ ∈ [0, 1]</b> and they add to 1: a valid probability distribution ✓</div>

## 🗣️ Say it out loud

`x ∈ ℝ⁴⁰⁹⁶` → "x is in R four thousand ninety-six" → "x is a list of 4096 numbers": one token's vector in Llama 3 8B.

## 🤖 Where AI uses it

Probabilities in [0, 1], vectors in ℝᵈ, vocabularies as sets, Jaccard similarity `|A ∩ B| / |A ∪ B|` for deduplication, "for all tokens" in loss formulas.

## 🎯 Your quest

1. `in_interval(x, text)`: `text` looks like `"[0, 1)"`: first character `[` or `(`, last `]` or `)`, two numbers separated by a comma. Return whether `x` is inside.
2. `is_distribution(ps)`: `True` if `∀ i: pᵢ ∈ [0, 1]` and the sum is 1 (within `1e-9`).

**Remember:** square bracket = end included, round bracket = end excluded.

## Review

<details><summary>What is e⁰?</summary>1.</details>
<details><summary>What range does the sigmoid output?</summary>Between 0 and 1, never reaching either.</details>
