---
title: Samples, the law of large numbers, standard error
xp: 55
---
# How many tests until you can trust the score?

> **Warm-up:** you test a model on 10 questions and it gets 7 right. Someone else tests it on 1000 and gets 700. Both say "70%". Whose 70% do you trust more, and why?

**In one sentence:** the average of a sample gets closer to the true average as the sample grows (law of large numbers), and its typical error is σ / √n (the standard error).

## 🪜 Plain words

You can rarely measure **everything** (every possible question, every user). You take a **sample** and average it.

- Small sample: the average jumps around a lot from sample to sample.
- Big sample: the average settles close to the truth. That's the **law of large numbers**.

How close? The **standard error** says: the spread of the sample average = the spread of single values ÷ √(sample size).

The catch is the square root: to halve the error you need **4×** the data. 10× smaller error needs 100× the data.

## 🪜 With numbers

One die roll: σ ≈ 1.71.

- Average of 100 rolls: SE = 1.71 / √100 = **0.17**. Usually between about 3.33 and 3.67.
- Average of 10,000 rolls: SE = 1.71 / 100 = **0.017**.
- For SE 0.05 you need n = (1.71 / 0.05)² = 1169.6, rounded up to **1170** rolls.

Benchmark: accuracy 70% on 100 questions. Each question is right/wrong, σ = √(0.7 · 0.3) = 0.458. SE = 0.458 / 10 = **4.6 percentage points**. A 2-point "improvement" is well inside the noise.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `n` | "n" | sample size | `len(xs)` |
| `x̄` | "x bar" | the sample average (the bar on top = "average of") | `sum(xs) / n` |
| `μ` | "mu" | the **true** average we're trying to learn | |
| `SE` | "standard error" | typical error of x̄ | `sigma / math.sqrt(n)` |
| `→` | "goes to" / "approaches" | (Math 3) | |
| `⌈ ⌉` | "ceiling" | round **up** to a whole number | `math.ceil` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">SE</span> = <span class="k2">σ</span> / <span class="k3">√n</span> &nbsp;&nbsp;&nbsp; <span class="k4">x̄</span> → <span class="k5">μ</span> as n → ∞</div>

| Piece | Say it | Means | 100 die rolls |
|---|---|---|---|
| <span class="k2">σ</span> | "sigma" | spread of **one** value | 1.71 |
| <span class="k3">√n</span> | "root n" | square root of the sample size | 10 |
| <span class="k1">SE</span> | "standard error" | spread of the **average** | 0.171 |
| <span class="k4">x̄</span> → <span class="k5">μ</span> | "x bar goes to mu" | the sample average approaches the truth as n grows | 3.5 |

Turned around: <span class="k3">n</span> = ( <span class="k2">σ</span> / target SE )², rounded **up**.

## 🔀 What if it were different?

<div class="wrong"><b>SE = σ / n</b>: 100 rolls → 0.017, ten times too confident. You'd announce "model B is better!" from pure noise.</div>
<div class="wrong"><b>SE = σ</b> (forgetting the sample size): averaging 10,000 rolls would seem no better than 1. Then why collect data?</div>
<div class="wrong"><b>Rounding n down</b>: 1169 rolls gives an SE just above your target. When you need "at least", round up.</div>
<div class="right">SE = σ / √n = 0.171; n for SE 0.05 = 1170 ✓</div>

## 🗣️ Say it out loud

"The standard error is sigma over root n."

## 🤖 Where AI uses it

Every benchmark comparison (LLMs 7's blind eval). Mini-batch gradients are sample averages of the true gradient: batch size 4× bigger → gradient noise 2× smaller, which is why bigger batches allow bigger learning rates.

## 🎯 Your quest

1. `simulate_mean(seed, n)`: roll `n` dice with `random.Random(seed).randint(1, 6)` and return the average.
2. `standard_error(sigma, n)`.
3. `n_needed(sigma, target_se)`: smallest whole n so that SE ≤ target.

**Remember:** errors shrink with √n: 4× the data for half the error.

## Review

<details><summary>z-score formula?</summary>z = (x − μ) / σ.</details>
<details><summary>What fraction of a normal distribution is within 2σ?</summary>About 95%.</details>
