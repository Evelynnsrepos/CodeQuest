---
title: e and exponential growth
xp: 40
---
# The most natural number

> **Warm-up:** your bank gives 100% interest a year. If it pays the interest in 2 halves, 12 months or every day, does your money keep growing without limit?

**In one sentence:** `e ≈ 2.718` is the number you get from growing continuously, and `eˣ` (exp) is the function that grows at a rate equal to itself.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `e` | "e" (Euler's number) | 2.71828… | `math.e` |
| `eˣ` or `exp(x)` | "e to the x" / "exp of x" | the exponential function | `math.exp(x)` |
| `ln(x)` | "natural log of x" | the inverse: `ln(eˣ) = x` | `math.log(x)` |
| `lim` | "the limit" | what a value gets closer and closer to | |
| `n → ∞` | "as n goes to infinity" | n getting bigger without end | big `n` |

## The idea

Paying interest more often helps, but less and less: `(1 + 1/n)ⁿ` with `n` = 1, 2, 12, 365, 1,000,000 gives 2, 2.25, 2.613, 2.7146, 2.71828… It approaches a limit, and that limit is **e**:

```
e = lim  (1 + 1/n)ⁿ
   n→∞
```

Key facts about `eˣ`:

- Always **positive**, even for negative x: `e⁻¹⁰ ≈ 0.0000454`.
- `e⁰ = 1`.
- **Turns sums into products**: `eᵃ⁺ᵇ = eᵃ · eᵇ`. (Logs do the reverse.)
- It's its own derivative (Math 3): it grows at a speed equal to its size.
- `eˣ` and `ln(x)` undo each other.

**Exponential decay** `e^(−kx)` shrinks by the same factor each step: half-lives, learning-rate decay.

## 🗣️ Say it out loud

`σ(z) = 1 / (1 + e^(−z))` → "sigma of z equals one over one plus e to the minus z".

## 🧮 Worked example

`σ(0) = 1 / (1 + e⁰) = 1 / (1 + 1) = 0.5`. For large z, `e^(−z)` is nearly 0, so σ ≈ 1. For very negative z, `e^(−z)` is huge, so σ ≈ 0. The sigmoid squeezes any number into 0..1.

## 🤖 Where AI uses it

**Softmax** uses `eᶻ` to turn any scores into positive numbers before dividing by their sum. The **sigmoid**. **Exponential moving averages** in Adam. The **Gaussian** bell curve `e^(−x²/2)`.

## 🎯 Your quest

1. `compound(n)`: `(1 + 1/n)ⁿ`.
2. `sigmoid(z)`: the formula above, with `math.exp`.
3. `decay(start, k, t)`: `start · e^(−k·t)`.

**Remember:** `eˣ` is always positive, and `ln` undoes it.

## Review

<details><summary>What does log(a · b) equal?</summary>log(a) + log(b).</details>
<details><summary>Why is the log of a probability negative?</summary>Because the probability is between 0 and 1, and log of numbers below 1 is negative.</details>
