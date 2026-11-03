---
title: Π products and n! factorials
xp: 35
---
# The multiplying cousin of Σ

> **Warm-up:** a model gives the tokens of "the cat sat" probabilities 0.1, 0.05 and 0.2. What's the probability of the whole sentence?

**In one sentence:** `Π` is like `Σ` but multiplies instead of adds, and `n!` multiplies all whole numbers from 1 to n.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `Π` | "pi" (capital) / "the product of" | multiply everything | `math.prod(...)` |
| `Πᵢ₌₁ⁿ pᵢ` | "the product from i equals 1 to n of p i" | `p₁ · p₂ · … · pₙ` | `math.prod(p)` |
| `n!` | "n factorial" | `1 · 2 · 3 · … · n`; `0! = 1` | `math.factorial(n)` |
| `C(n, k)` or `(n k)` stacked | "n choose k" | how many ways to pick k items from n | `math.comb(n, k)` |

Don't mix up the two pis: lowercase `π` is 3.14159…, capital `Π` is "multiply all".

## The idea

- `Π` works like `Σ`, but the running total starts at **1** (multiplying by 1 changes nothing), not 0.
- `n!` grows insanely fast: `5! = 120`, `10! = 3,628,800`, `20!` has 19 digits.
- **Choose:** `C(n, k) = n! / (k! · (n − k)!)`. Picking 2 of 4 items: `4! / (2! · 2!) = 24 / 4 = 6`.

## 🗣️ Say it out loud

`P(sentence) = Πₜ P(tokenₜ | earlier tokens)` → "the probability of the sentence is the product, over every position t, of the probability of that token given the earlier ones."

## 🧮 Worked example

"the cat sat" with 0.1, 0.05, 0.2:

1. `0.1 · 0.05 = 0.005`
2. `0.005 · 0.2 = 0.001`

One in a thousand. With 1,000 tokens, this product gets so tiny that computers round it to 0, which is why we take logarithms (lesson 10).

## 🤖 Where AI uses it

The probability of a whole text is a product. pass@k (LLMs 8) uses `C(n, k)`. Counting possible outputs ("how many 10-token texts with a 128K vocabulary?" = `128000¹⁰`) uses powers.

## 🎯 Your quest

Without `math.prod`, `math.factorial` or `math.comb`:

1. `product(xs)`: `Π xᵢ` (empty list → 1).
2. `factorial(n)`.
3. `choose(n, k)`: with the factorial formula (use `//` for whole-number division).

**Remember:** `Σ` starts at 0 and adds, `Π` starts at 1 and multiplies.

## Review

<details><summary>Python for Σᵢ₌₁ⁿ xᵢ when x is a list?</summary>sum(x) (and x₁ is x[0]).</details>
<details><summary>What does x̄ mean?</summary>The mean (average) of x.</details>
