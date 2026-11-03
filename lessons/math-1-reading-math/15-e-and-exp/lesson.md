---
title: e and exponential growth
xp: 40
---
# The number that growth is made of

> **Warm-up:** a bank gives you 100% interest per year. Is it better if they pay it once a year, or in tiny pieces every day (each piece also earning interest)? Does it grow forever?

**In one sentence:** `e ≈ 2.718` is what you get from growing smoothly all the time, and `eˣ` ("exp") is the growth function that AI uses to turn any number into a positive one.

## 🪜 Plain words

Paying interest more often helps a little, because earlier interest starts earning interest too. But the gain gets smaller and smaller and settles at a limit. Starting with 1 euro, that limit is about **2.718 euros**. This number is so natural that it got a name: **e**.

`e` multiplied by itself x times is written `eˣ`. It has a few magic properties:

- It's **always positive**, even for negative x (then it's just very small).
- It grows faster and faster as x grows.
- Its "reverse" is the natural log `ln` from the last lesson: `ln(eˣ) = x`.

## 🪜 With numbers

Interest paid 1, 2, 12, 365, 1,000,000 times a year: 2, 2.25, 2.613, 2.7146, 2.71828… → it settles at e.

- e¹ ≈ 2.718, e² ≈ 7.39, e⁰ = 1, e⁻¹ ≈ 0.368, e⁻¹⁰ ≈ 0.0000454 (tiny but still positive).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `e` | "e" | 2.71828… | `math.e` |
| `eˣ` or `exp(x)` | "e to the x" / "exp of x" | e multiplied by itself x times | `math.exp(x)` |
| `ln(x)` | "natural log of x" | undoes exp | `math.log(x)` |
| `lim` | "the limit" | the value something settles at | |
| `n → ∞` | "as n goes to infinity" | as n gets bigger and bigger without end | |
| `e^(−z)` | "e to the minus z" | 1 / eᶻ | `math.exp(-z)` |

## 🔬 Take the formula apart

The **sigmoid**, which squeezes any number into 0..1:

<div class="formula"><span class="k1">σ(z)</span> = <span class="k2">1</span> / (<span class="k3">1</span> + <span class="k4">e</span><sup><span class="k5">−z</span></sup>)</div>

| Piece | Say it | Means | z = 0 | z = 5 | z = −5 |
|---|---|---|---|---|---|
| <span class="k1">σ(z)</span> | "sigma of z" | the output | 0.5 | 0.993 | 0.007 |
| <span class="k2">1</span> / | "one over" | divide 1 by the bottom | | | |
| (<span class="k3">1</span> + | "one plus" | the bottom always starts at 1… | | | |
| <span class="k4">e</span><sup><span class="k5">−z</span></sup>) | "e to the minus z" | …plus a positive number: big when z is negative, tiny when z is positive | 1 | 0.0067 | 148 |

So: bottom = 1 + something positive → always more than 1 → σ is always **between 0 and 1**. Big z → bottom ≈ 1 → σ ≈ 1. Very negative z → bottom huge → σ ≈ 0.

## 🔀 What if the formula were different?

<div class="wrong"><b>1 / (1 + e^z)</b> (lost the minus): σ(5) = 0.007. The curve is flipped: big inputs give small outputs.</div>
<div class="wrong"><b>1 / e^(−z)</b> (no "1 +"): that's just eᶻ: σ(5) = 148. No longer squeezed below 1, not a probability.</div>
<div class="wrong"><b>1 / (1 − e^(−z))</b> (minus instead of plus): at z = 0 the bottom is 0: division by zero, crash.</div>
<div class="right"><b>1 / (1 + e^(−z))</b>: 0.5, 0.993, 0.007 ✓</div>

## 🗣️ Say it out loud

`σ(z) = 1 / (1 + e^(−z))` → "sigma of z equals one over one plus e to the minus z".

## 🤖 Where AI uses it

**Softmax** uses `eᶻ` to make every score positive before turning them into probabilities. The **sigmoid** in gates and classifiers. **Exponential decay** `start · e^(−kt)` for learning rates.

## 🎯 Your quest

1. `compound(n)`: `(1 + 1/n)ⁿ`.
2. `sigmoid(z)`: the formula above with `math.exp`.
3. `decay(start, k, t)`: `start · e^(−k·t)`.

**Remember:** `eˣ` is always positive, and `ln` undoes it.

## Review

<details><summary>log(a · b) = ?</summary>log(a) + log(b).</details>
<details><summary>Why are log-probabilities negative?</summary>Probabilities are below 1, and logs of numbers below 1 are negative.</details>
