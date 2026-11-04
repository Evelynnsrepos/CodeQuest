---
title: Logarithms
xp: 50
---
# "How many times?"

> **Warm-up:** how many times do you have to double 1 to reach 8? To reach 1024?

**In one sentence:** a logarithm counts how many times you multiply a base to reach a number, and it turns multiplying into adding.

## 🪜 Plain words

Doubling: 1 → 2 → 4 → 8. That took **3** doublings. "How many doublings to reach 8?" has the answer 3, and that answer has a name: the **logarithm** of 8, base 2.

So a log is the **reverse of a power**: powers say "double 3 times gives?", logs say "8 needs how many doublings?".

The superpower: multiplying two numbers = **adding** their doubling-counts. 8 is 3 doublings, 4 is 2 doublings, and 8 times 4 = 32 is 3 + 2 = 5 doublings. Adding is much easier than multiplying, especially for tiny numbers.

## 🪜 With numbers

- Base 2: 1024 needs 10 doublings (2¹⁰ = 1024), so log₂ 1024 = 10.
- Base 10: 1000 is 10 times 10 times 10, so log₁₀ 1000 = 3. Roughly "how many zeros".
- Numbers **smaller than 1** need "negative doublings" (halvings): 0.5 is one halving, so log₂ 0.5 = −1. That's why logs of probabilities are negative.
- log of 1 is 0 (no doublings needed).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `log₂(x)` | "log base two of x" | how many 2s multiply to x | `math.log2(x)` |
| `log₁₀(x)` | "log base ten of x" | how many 10s | `math.log10(x)` |
| `ln(x)` | "L N of x" / "natural log" | base e = 2.718… (next lesson) | `math.log(x)` |
| `log(x)` | "log of x" | in AI papers this almost always means **ln** | `math.log(x)` |
| `log_b(x)` | "log base b of x" | any base | `math.log(x, b)` |

## 🔬 Take the formula apart

The definition:

<div class="formula"><span class="k1">log</span><sub><span class="k2">b</span></sub>(<span class="k3">x</span>) = <span class="k4">p</span> &nbsp;means&nbsp; <span class="k2">b</span><sup><span class="k4">p</span></sup> = <span class="k3">x</span></div>

| Piece | Say it | Means | log₂(8) |
|---|---|---|---|
| <span class="k1">log</span> | "log" | "how many times?" | |
| <sub><span class="k2">b</span></sub> | "base b" | the number being multiplied | 2 |
| (<span class="k3">x</span>) | "of x" | the target | 8 |
| <span class="k4">p</span> | "p" | the answer: how many times | 3, because 2³ = 8 |

The superpower rule:

<div class="formula"><span class="k1">log</span>(<span class="k2">a</span> · <span class="k3">b</span>) = <span class="k1">log</span>(<span class="k2">a</span>) <span class="k4">+</span> <span class="k1">log</span>(<span class="k3">b</span>)</div>

| Piece | Say it | Means | 8 · 4 in base 2 |
|---|---|---|---|
| <span class="k1">log</span>(<span class="k2">a</span> · <span class="k3">b</span>) | "log of a times b" | doublings to reach the product | log₂ 32 = 5 |
| <span class="k1">log</span>(<span class="k2">a</span>) | "log of a" | doublings to reach a | 3 |
| <span class="k4">+</span> | "plus" | **add** them | |
| <span class="k1">log</span>(<span class="k3">b</span>) | "log of b" | doublings to reach b | 2 → 3 + 2 = 5 ✓ |

More rules from the same idea: `log(a / b) = log a − log b`, `log(aⁿ) = n · log a`, `log(1) = 0`. Changing base: `log_b(x) = ln(x) / ln(b)`.

## 🔀 What if the formula were different?

<div class="wrong"><b>log(a · b) = log(a) · log(b)</b> (a very common mistake): log₂ 32 would be 3 · 2 = 6, but 2⁶ = 64, not 32.</div>
<div class="wrong"><b>log(a + b) = log a + log b</b>: also false: log₂(8 + 4) = log₂ 12 ≈ 3.58, not 5.</div>
<div class="wrong"><b>log(0)</b>: no number of doublings ever reaches 0. It's undefined (it goes to minus infinity). A model that gives the right token probability 0 has an infinite loss.</div>
<div class="right"><b>log(a · b) = log a + log b</b>: products become sums ✓</div>

## 🗣️ Say it out loud

`log P(text) = Σₜ log P(tokenₜ)` → "the log of the text's probability is the sum over t of the log of each token's probability."

## 🤖 Where AI uses it

- **Log-probabilities**: instead of multiplying 1,000 tiny probabilities (→ 0 on a computer), LLMs **add** their logs.
- **The loss**: `−log p(right token)` (Math 5).
- **Bits**: `log₂(128000) ≈ 17` bits to pick one token from Llama 3's vocabulary.

## 🎯 Your quest

1. `log_base(x, b)`: using only `math.log` and the change-of-base rule.
2. `bits_needed(n)`: whole bits needed for `n` different values: `log₂ n` rounded **up** (`math.ceil`).
3. `log_prob(ps)`: the sum of the natural logs of a list of probabilities.

**Remember:** logs turn multiplying into adding.

## Review

<details><summary>What is 4!?</summary>24.</details>
<details><summary>Why is a product of many probabilities a problem for computers?</summary>It gets so small it rounds to 0.</details>
