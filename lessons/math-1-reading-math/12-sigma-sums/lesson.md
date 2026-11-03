---
title: Σ: the summation sign
xp: 40
---
# A for loop that adds things up

> **Warm-up:** the big `Σ` shows up in almost every AI paper. If you had to guess from its shape (a Greek capital S), what might it stand for?

**In one sentence:** `Σ` means "add up", and it's exactly a `for` loop that keeps a running total.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `Σ` | "sigma" / "the sum of" | add up everything after it | `sum(...)` or a loop |
| `xᵢ` or `x_i` | "x sub i" / "x i" | item number `i` of a list x (subscript = index) | `x[i]` |
| `Σᵢ₌₁ⁿ xᵢ` | "the sum from i equals 1 to n of x i" | `x₁ + x₂ + … + xₙ` | `sum(x)` |
| `n` | "n" | how many items there are | `len(x)` |
| `x̄` | "x bar" | the mean (average) of x | `sum(x) / len(x)` |
| `…` | "and so on" | the pattern continues | |

## The idea

Read the sum in three parts:

```
   n          ← where i stops (top)
   Σ   xᵢ²    ← what to add each time (right side)
  i=1         ← the counter's name and where it starts (bottom)
```

As Python:

```python
total = 0
for i in range(1, n + 1):      # bottom to top, top INCLUDED
    total += x[i] ** 2
```

**Watch out:** math usually counts from **1**, Python from **0**. `x₁` in a paper is `x[0]` in Python. When the bounds are obvious, papers drop them and write just `Σᵢ xᵢ`, meaning "over all i".

## 🗣️ Say it out loud

`x̄ = (1/n) Σᵢ₌₁ⁿ xᵢ` → "x bar equals one over n times the sum of all x i" → "add them all up and divide by how many there are": the average.

## 🧮 Worked example

`Σᵢ₌₁³ i²`:

1. i = 1: `1² = 1`
2. i = 2: `2² = 4`
3. i = 3: `3² = 9`
4. Total: `1 + 4 + 9 = 14`

## 🤖 Where AI uses it

Everywhere: the dot product `Σᵢ aᵢbᵢ` (Math 2), the mean squared error `(1/n) Σ (yᵢ − ŷᵢ)²`, the softmax denominator `Σⱼ e^(zⱼ)`, the total loss over a dataset.

## 🎯 Your quest

1. `sigma(f, start, end)`: return `f(start) + f(start + 1) + … + f(end)` (**end included**).
2. `mean(xs)`: `(1/n) Σ xᵢ`.
3. `mse(ys, preds)`: `(1/n) Σᵢ (yᵢ − ŷᵢ)²`.

**Remember:** `Σ` is a loop with a running total, and the top number is included.

## Review

<details><summary>In f(g(x)), which function runs first?</summary>g, the inner one.</details>
<details><summary>Write 2.5 · 10⁻³ in Python.</summary>2.5e-3</details>
