---
title: Π products and n! factorials
xp: 35
---
# Σ's multiplying cousin

> **Warm-up:** a model is 10% sure about the first word, 5% about the second, 20% about the third. How sure is it about all three together?

**In one sentence:** the big `Π` means "multiply a list of things together", and `n!` means "multiply all whole numbers from 1 up to n".

## 🪜 Plain words

When several things must **all** happen, you multiply their chances. If there's a 1 in 10 chance for the first and a 1 in 20 chance for the second, both together is 1 in 200. Math has a sign for "multiply them all": a big Greek P (for **P**roduct) called capital **pi**, `Π`.

**Factorial** answers "in how many orders can I line things up?". 3 books: 3 choices for the first spot, then 2, then 1: 3 times 2 times 1 = 6 orders.

## 🪜 With numbers

- 0.1 times 0.05 = 0.005. Times 0.2 = **0.001**: one in a thousand.
- 5! = 5 times 4 times 3 times 2 times 1 = **120**.
- Choosing 2 out of 4 people (order doesn't matter): **6** ways (AB, AC, AD, BC, BD, CD).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Π` | "pi" (capital) / "the product of" | multiply all of them | `math.prod(...)` |
| `n!` | "n factorial" | 1 · 2 · … · n, and `0! = 1` | `math.factorial(n)` |
| `C(n, k)` | "n choose k" | ways to pick k from n | `math.comb(n, k)` |

Two different pis: small `π` = 3.14159…; big `Π` = "multiply all".

## 🔬 Take the formula apart

Probability of a whole sentence:

<div class="formula"><span class="k1">P(text)</span> = <span class="k2">Π</span><sub><span class="k3">t</span></sub> <span class="k4">P(tokenₜ)</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k1">P(text)</span> | "P of text" | chance of the whole sentence | 0.001 |
| <span class="k2">Π</span> | "the product of" | multiply all of… | |
| <sub><span class="k3">t</span></sub> | "over t" | t counts the positions: 1, 2, 3 … | 3 positions |
| <span class="k4">P(tokenₜ)</span> | "P of token t" | chance of the token at position t | 0.1, 0.05, 0.2 |

"n choose k":

<div class="formula"><span class="k1">C(n, k)</span> = <span class="k2">n!</span> / (<span class="k3">k!</span> · <span class="k4">(n − k)!</span>)</div>

| Piece | Say it | Means | 2 from 4 |
|---|---|---|---|
| <span class="k2">n!</span> | "n factorial" | all orders of all n | 4! = 24 |
| <span class="k3">k!</span> | "k factorial" | orders inside the chosen group don't matter, so divide them out | 2! = 2 |
| <span class="k4">(n − k)!</span> | "n minus k, factorial" | orders of the ones left out don't matter either | 2! = 2 |
| result | | 24 / (2 · 2) | 6 |

## 🔀 What if the formula were different?

<div class="wrong"><b>Σ instead of Π</b>: 0.1 + 0.05 + 0.2 = 0.35. "35% chance for the whole sentence" is far too high; with 20 tokens, adding could even go over 100%.</div>
<div class="wrong"><b>Starting the product at 0</b> (like a sum): 0 · anything = 0. Products must start at 1.</div>
<div class="wrong"><b>C(n, k) = n! / k!</b> (forgot (n − k)!): 24 / 2 = 12, which counts AB and BA as different.</div>
<div class="right">Π: 0.001, and C(4, 2) = 6 ✓</div>

## 🗣️ Say it out loud

`Πₜ P(tokenₜ)` → "the product over t of P of token t" → "multiply the chances of every token."

## 🤖 Where AI uses it

A text's probability is a product, which gets **tiny**: 1,000 tokens at 0.1 each is 10⁻¹⁰⁰⁰, which a computer rounds to 0. That's exactly why the next lesson (logarithms) matters. pass@k (LLMs 8) uses "n choose k".

## 🎯 Your quest

Without `math.prod`, `math.factorial` or `math.comb`:

1. `product(xs)`: `Π xᵢ` (empty list → 1).
2. `factorial(n)`.
3. `choose(n, k)`: with the factorial formula (use `//` for whole-number division).

**Remember:** Σ starts at 0 and adds; Π starts at 1 and multiplies.

## Review

<details><summary>Python for Σᵢ₌₁ⁿ xᵢ when x is a list?</summary>sum(x) (and x₁ is x[0]).</details>
<details><summary>What does x̄ mean?</summary>The average of x.</details>
