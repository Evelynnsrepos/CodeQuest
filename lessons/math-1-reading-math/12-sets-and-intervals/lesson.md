---
title: Sets, ∈ and intervals
xp: 35
---
# Collections and ranges

> **Warm-up:** a paper says "p ∈ [0, 1]" and "x ∈ ℝ⁴⁰⁹⁶". What do you think each one says?

**In one sentence:** a set is a collection of things, `∈` means "is in", and an interval is a range of numbers with or without its ends.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `{1, 2, 3}` | "the set one, two, three" | a collection, no duplicates, no order | `{1, 2, 3}` |
| `x ∈ A` | "x is in A" / "x is an element of A" | membership | `x in A` |
| `x ∉ A` | "x is not in A" | | `x not in A` |
| `A ∪ B` | "A union B" | everything in A or B | `A \| B` |
| `A ∩ B` | "A intersect B" | only what's in both | `A & B` |
| `A ⊆ B` | "A is a subset of B" | everything in A is also in B | `A <= B` |
| `∅` | "the empty set" | nothing | `set()` |
| `ℕ`, `ℤ`, `ℝ` | "naturals, integers, reals" | 0, 1, 2…; … −1, 0, 1 …; all numbers on the line | |
| `ℝⁿ` | "R n" | lists (vectors) of n real numbers | a list of n floats |
| `[a, b]` | "closed interval a to b" | a ≤ x ≤ b, ends included | `a <= x <= b` |
| `(a, b)` | "open interval" | a < x < b, ends excluded | `a < x < b` |
| `[a, b)` | "half-open" | a ≤ x < b | `a <= x < b` |
| `∀` / `∃` | "for all" / "there exists" | every / at least one | `all(...)` / `any(...)` |

## The idea

- Square bracket `[ ]` = **include** that end. Round bracket `( )` = **exclude** it. (Same idea as Python's `range(a, b)`, which is `[a, b)`.)
- `ℝ` is the set of all real numbers; `ℝⁿ` is all lists of n of them. "`x ∈ ℝ⁴⁰⁹⁶`" means "x is a list of 4096 numbers": a token's vector in Llama 3 8B.
- `∀ i: pᵢ ≥ 0` means "for all i, p i is at least zero".

## 🗣️ Say it out loud

`σ: ℝ → (0, 1)` → "sigmoid takes any real number and gives a number strictly between 0 and 1" (it never actually reaches 0 or 1).

## 🧮 Worked example

Is `x = 1` in `[0, 1)`? `0 ≤ 1` yes, `1 < 1` no. So **no**. Is it in `[0, 1]`? Yes.

## 🤖 Where AI uses it

Probabilities `∈ [0, 1]`, vectors `∈ ℝᵈ`, vocabularies as sets of tokens, Jaccard similarity `|A ∩ B| / |A ∪ B|` (LLMs 8, deduplication), "for all tokens" in loss formulas.

## 🎯 Your quest

1. `in_interval(x, text)`: `text` looks like `"[0, 1)"`: first character `[` or `(`, last `]` or `)`, two numbers separated by a comma. Return whether `x` is inside.
2. `is_distribution(ps)`: `True` if `∀ i: pᵢ ∈ [0, 1]` and `Σ pᵢ` is 1 (within `1e-9`).

**Remember:** square bracket = included, round bracket = excluded.

## Review

<details><summary>What is e⁰?</summary>1.</details>
<details><summary>What range of values can sigmoid output?</summary>Between 0 and 1, never reaching either.</details>
