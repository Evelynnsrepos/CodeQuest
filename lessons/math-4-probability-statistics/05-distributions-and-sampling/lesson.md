---
title: Distributions and how LLMs sample
xp: 55
---
# A table of every outcome and its chance

> **Warm-up:** an LLM thinks the next word is "cat" 50%, "dog" 30%, "fish" 20%. How could a computer pick one, using only a random number between 0 and 1?

**In one sentence:** a distribution lists every possible outcome with its probability (all adding to 1), and you sample from it by laying the probabilities end to end and seeing where a random number lands.

## 🪜 Plain words

A **random variable** is just "a number (or token) that comes out of a chance process": the face of a die, the next token.

Its **distribution** is the full table: outcome → probability.

**Sampling trick:** put the probabilities on a ruler from 0 to 1: cat takes 0 to 0.5, dog 0.5 to 0.8, fish 0.8 to 1.0. Draw a random number u. Wherever it lands, that's your pick. Bigger probability = bigger slice = picked more often.

The running total (0.5, 0.8, 1.0) is the **cumulative** distribution: P(outcome is this one or earlier).

## 🪜 With numbers

| token | P | running total |
|---|---|---|
| cat | 0.5 | 0.5 |
| dog | 0.3 | 0.8 |
| fish | 0.2 | 1.0 |

- u = 0.12 → **cat** (below 0.5)
- u = 0.65 → **dog** (between 0.5 and 0.8)
- u = 0.93 → **fish**

From data: rolls `[1, 3, 3, 6]` → P(1) = 0.25, P(3) = 0.5, P(6) = 0.25.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `X` | "X" (capital) | a random variable: the not-yet-known outcome | |
| `x` | "x" (small) | one particular value it could take | |
| `P(X = x)` or `p(x)` | "P of X equals x" | chance X comes out as x | `d[x]` |
| `X ∼ p` | "X is distributed as p" / "X follows p" | X is drawn from p | `sample(d, u)` |
| `F(x) = P(X ≤ x)` | "F of x" / "the CDF" | running total up to x | |
| `u ∼ U(0, 1)` | "u is uniform from 0 to 1" | every number in 0..1 equally likely | `random.random()` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">F(x)</span> = <span class="k2">P(X ≤ x)</span> = <span class="k3">Σ<sub>k ≤ x</sub></span> <span class="k4">p(k)</span></div>

| Piece | Say it | Means | F(dog) |
|---|---|---|---|
| <span class="k4">p(k)</span> | "p of k" | one outcome's probability | 0.5, 0.3 |
| <span class="k3">Σ<sub>k ≤ x</sub></span> | "sum over k up to x" | add all outcomes up to and including x | cat + dog |
| <span class="k2">P(X ≤ x)</span> | "P of X at most x" | chance of x or anything before it | |
| <span class="k1">F(x)</span> | "F of x" | the running total | 0.8 |

Sampling: pick the **first** outcome whose running total is **greater than** u.

## 🔀 What if it were different?

<div class="wrong"><b>Pick the first outcome whose own p is > u</b> (no running total): u = 0.65 → nothing is above 0.65 → crash, or always the biggest. Small slices would be chosen far too rarely.</div>
<div class="wrong"><b>Probabilities that add to 0.9</b>: u = 0.95 falls off the end of the ruler. Always check a distribution sums to 1 (softmax guarantees it).</div>
<div class="wrong"><b>Always pick the biggest</b> (greedy): "cat" every time. That's temperature 0 (LLMs 1): no variety at all.</div>
<div class="right">running totals 0.5, 0.8, 1.0; u = 0.65 → dog ✓</div>

## 🗣️ Say it out loud

`X ∼ p` → "X is drawn from p."

## 🤖 Where AI uses it

This **is** how LLM sampling works after softmax, temperature and top-p (LLMs 1): build the running total, draw u, pick. The seed decides u, which is why the same seed gives the same text.

## 🎯 Your quest

Distributions are dicts `{outcome: probability}` (keep the dict's order).

1. `from_samples(samples)`: count each outcome and divide by the number of samples.
2. `cdf(d, x)`: running total up to and including outcome `x` (in dict order).
3. `sample(d, u)`: the first outcome whose running total is > u.

**Remember:** a distribution adds to 1; sample with a running total and one random number.

## Review

<details><summary>P(sick | +) when the disease is rare?</summary>Usually small: most positives are false alarms.</details>
<details><summary>Name the parts of Bayes.</summary>Posterior = likelihood × prior / evidence.</details>
