---
title: Entropy: average surprise
xp: 50
---
# How unpredictable is it, on average?

> **Warm-up:** a fair coin and a coin that lands heads 90% of the time. Which one is easier to predict? Which one teaches you more per flip?

**In one sentence:** entropy is the expected surprise of a distribution: how uncertain it is, on average, in bits or nats.

## 🪜 Plain words

Lesson 01 measured surprise for **one** outcome. Entropy asks: if I keep drawing from this distribution, how surprised am I **on average**? That's an expected value (Math 4 lesson 06): weight each outcome's surprise by its probability, then add.

- All outcomes equally likely → maximum uncertainty → **highest** entropy.
- One outcome almost certain → you're rarely surprised → **low** entropy.
- One outcome certain → entropy **0**.

## 🪜 With numbers

- Fair coin: 0.5 · 1 + 0.5 · 1 = **1 bit**.
- 90/10 coin: 0.9 · 0.152 + 0.1 · 3.32 = **0.469 bits**.
- Fair die: **2.58 bits**.
- An LLM 99% sure of the next token: entropy near 0. An LLM spreading over 1000 tokens evenly: log₂ 1000 ≈ 10 bits.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `H(p)` | "H of p" / "the entropy of p" | average surprise | `entropy(ps)` |
| `Σₓ` | "sum over x" | every outcome | `for p in ps` |
| `p(x)` | "p of x" | outcome's probability (the weight) | |
| `−log p(x)` | "minus log p of x" | outcome's surprise (lesson 01) | |
| `0 log 0` | | counted as 0 (impossible outcomes add nothing) | skip p = 0 |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">H(p)</span> = <span class="k2">Σ<sub>x</sub></span> <span class="k3">p(x)</span> · ( <span class="k4">− log p(x)</span> )</div>

| Piece | Say it | Means | 90/10 coin |
|---|---|---|---|
| <span class="k4">− log p(x)</span> | "minus log p of x" | surprise of x | 0.152, 3.32 bits |
| <span class="k3">p(x)</span> · | "p of x times" | weight by how often it happens | 0.9 · 0.152, 0.1 · 3.32 |
| <span class="k2">Σ<sub>x</sub></span> | "sum over x" | add for all outcomes | |
| <span class="k1">H(p)</span> | "H of p" | average surprise | 0.469 bits |

Usually written compactly as H(p) = −Σ p(x) log p(x).

## 🔀 What if it were different?

<div class="wrong"><b>Plain average of surprises (no p weighting)</b>: (0.152 + 3.32) / 2 = 1.74 bits for the 90/10 coin: more than a fair coin! The rare tails gets as much weight as the common heads.</div>
<div class="wrong"><b>Forget the minus</b>: −0.469. Entropy is never negative.</div>
<div class="wrong"><b>Include p = 0 as 0 · log 0 in Python</b>: <code>math.log(0)</code> raises an error. Skip zero-probability outcomes: they're never seen, so they add no surprise.</div>
<div class="right">fair coin 1 bit, 90/10 coin 0.469 bits ✓</div>

## 🗣️ Say it out loud

"H of p equals minus the sum over x of p of x log p of x."

## 🤖 Where AI uses it

Entropy of the next-token distribution shows how unsure an LLM is (used to detect hallucination risk and to decide when to "think longer"). RL training adds an entropy bonus to keep exploration alive. Low-temperature sampling lowers entropy.

## 🎯 Your quest

1. `entropy(ps, base=2)`: skip zeros; `base` 2 = bits, `math.e` = nats.
2. `max_entropy(n, base=2)`: entropy of n equally likely outcomes (log n).

**Remember:** entropy = average surprise = how unpredictable.

## Review

<details><summary>Surprise of p = 0.25?</summary>2 bits.</details>
<details><summary>Do surprises of independent events add or multiply?</summary>Add.</details>
