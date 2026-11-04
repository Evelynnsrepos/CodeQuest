---
title: Log-sum-exp: softmax without overflow
xp: 55
---
# When eˣ is too big for the computer

> **Warm-up:** run `math.exp(1000)` in Python. What happens? Logits of 1000 can really occur. How could softmax still work?

**In one sentence:** subtracting the biggest value before taking eˣ gives the exact same softmax and log-sum-exp, without ever overflowing.

## 🪜 Plain words

e¹⁰⁰⁰ is far bigger than the largest number a float can hold (about 1.8 × 10³⁰⁸). Python raises `OverflowError`; numpy/GPU code gives `inf`, then `inf / inf = NaN`, and training dies.

The fix: softmax only cares about **differences** between the scores. Shifting all scores down by the same amount doesn't change the result. Shift so the biggest becomes 0: now the biggest eˣ is e⁰ = 1, and nothing can overflow.

## 🪜 With numbers

Scores (1000, 1000).

- Naive: e¹⁰⁰⁰ + e¹⁰⁰⁰ → overflow.
- Shifted by m = 1000: e⁰ + e⁰ = 2. log 2 = 0.693. Add m back: **1000.693**.
- Softmax: (1, 1) / 2 = **(0.5, 0.5)**, exactly right.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `LSE(x)` or `logsumexp(x)` | "log-sum-exp of x" | log( Σ eˣⁱ ) | `logsumexp(xs)` |
| `m = max(x)` | "m is the max of x" | the biggest score | `max(xs)` |
| `xᵢ − m` | "x i minus m" | shifted score, always ≤ 0 | `x - m` |
| `log softmax` | | log of softmax = xᵢ − LSE(x) | `log_softmax(xs)` |
| `inf`, `NaN` | "infinity", "not a number" | what broken float math produces | `float("inf")` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">LSE(x)</span> = <span class="k2">m</span> + log Σᵢ e<sup><span class="k3">xᵢ − m</span></sup> &nbsp;&nbsp;&nbsp; <span class="k4">log softmax(x)ᵢ</span> = <span class="k5">xᵢ</span> − <span class="k1">LSE(x)</span></div>

| Piece | Say it | Means | (1000, 1000) |
|---|---|---|---|
| <span class="k2">m</span> | "m" | the biggest score | 1000 |
| <span class="k3">xᵢ − m</span> | "x i minus m" | shifted: biggest becomes 0 | 0, 0 |
| log Σ e<sup>…</sup> | "log sum e to the" | safe now: every term ≤ 1 | log 2 = 0.693 |
| <span class="k2">m</span> + | "plus m" | undo the shift | 1000.693 |
| <span class="k5">xᵢ</span> − <span class="k1">LSE</span> | "x i minus log-sum-exp" | log-probability of i | −0.693 → p = 0.5 |

Why it's exact: e^(x − m) = eˣ / eᵐ, so the sum is divided by eᵐ, and log of that subtracts m, which we add back.

## 🔀 What if it were different?

<div class="wrong"><b>No shift</b>: overflow → inf → NaN loss → the whole run is ruined.</div>
<div class="wrong"><b>Shift by m but forget to add it back</b>: LSE = 0.693 instead of 1000.693. Softmax would still be right (it cancels), but the loss value would be wrong.</div>
<div class="wrong"><b>Shift by the smallest value</b>: scores (1000, 0) → shift by 0 → e¹⁰⁰⁰ still overflows. Use the max.</div>
<div class="wrong"><b>log(softmax(x)) computed as two steps</b>: for very unlikely tokens softmax underflows to 0.0, then log(0) = −inf. x − LSE stays finite (e.g. −1000).</div>
<div class="right">LSE(1000, 1000) = 1000.693; log softmax = (−0.693, −0.693) ✓</div>

## 🗣️ Say it out loud

"Log-sum-exp of x equals m plus log of the sum of e to the x i minus m."

## 🤖 Where AI uses it

Inside every `cross_entropy` and `log_softmax` in PyTorch. **FlashAttention** uses a running version of this trick to compute softmax block by block. Bad LSE handling is a classic cause of NaN losses in mixed precision (lesson 12).

## 🎯 Your quest

1. `logsumexp(xs)`: the safe version.
2. `log_softmax(xs)`: list of `x − LSE`.
3. `softmax(xs)`: safe softmax (shift by max first).

**Remember:** subtract the max before eˣ; it changes nothing except that it works.

## Review

<details><summary>Loss 2.1 → perplexity?</summary>e^2.1 ≈ 8.2.</details>
<details><summary>Can you compare perplexity across different tokenizers?</summary>No.</details>
