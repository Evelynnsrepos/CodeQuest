---
title: E[X]: the expected value
xp: 55
---
# The long-run average

> **Warm-up:** a game: roll a die, win that many euros. If you played 1000 times, how much would you win per game on average?

**In one sentence:** the expected value `E[X]` is the probability-weighted average of all outcomes: what you'd get per try in the long run.

## 🪜 Plain words

Multiply each outcome by how likely it is, then add everything up. Likely outcomes count a lot, rare ones count a little.

It doesn't have to be a possible outcome: the expected die roll is 3.5, though you can never roll 3.5. It's the **centre of balance** of the distribution.

## 🪜 With numbers

Die: (1 + 2 + 3 + 4 + 5 + 6) × 1/6 = **3.5** euros per game.

A model's answer gets reward 1 if right, 0 if wrong. It's right 70% of the time: E[reward] = 1 · 0.7 + 0 · 0.3 = **0.7**.

A lottery ticket costs 2 €: 1 in 1000 wins 1000 €. E[profit] = 0.001 · 998 + 0.999 · (−2) = 0.998 − 1.998 = **−1 €** per ticket.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `E[X]` | "E of X" / "the expected value of X" | weighted average of X | `expected(d)` |
| `μ` | "mu" (myoo) | another name for the mean / expected value | `mu` |
| `E[f(X)]` | "E of f of X" | average of f applied to the outcomes | `expected_f(d, f)` |
| `E_{x∼p}[ … ]` | "E over x drawn from p of …" | average, with x drawn from p (the small text says **which** distribution) | |
| `π` | "pi" (in RL: the **policy**, not 3.14!) | the model's distribution over actions/answers | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">E[X]</span> = <span class="k2">Σ<sub>x</sub></span> <span class="k3">x</span> · <span class="k4">p(x)</span></div>

| Piece | Say it | Means | Die |
|---|---|---|---|
| <span class="k2">Σ<sub>x</sub></span> | "sum over all x" | for every outcome | 1..6 |
| <span class="k3">x</span> | "x" | the outcome's value | 1, 2, … |
| <span class="k4">p(x)</span> | "p of x" | its probability: the weight | 1/6 each |
| <span class="k1">E[X]</span> | "E of X" | the weighted total | 3.5 |

The RL notation you'll see in papers (LLMs 8):

<div class="formula">J(θ) = <span class="k1">E</span><sub><span class="k5">y ∼ π<sub>θ</sub>(· | x)</span></sub> [ <span class="k6">r(x, y)</span> ]</div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k5">y ∼ π<sub>θ</sub>(· \| x)</span> | "y drawn from pi theta given x" | the model's answers y to prompt x (the · is "any answer") |
| <span class="k6">r(x, y)</span> | "r of x, y" | reward for that answer |
| <span class="k1">E</span>[ … ] | "expected" | average reward the model would get. Training pushes this up. |

## 🔀 What if it were different?

<div class="wrong"><b>Plain average of outcomes, ignoring p</b>: lottery: (998 + (−2)) / 2 = +498 €. Looks like a great deal. It ignores that winning is 1000× rarer than losing.</div>
<div class="wrong"><b>Σ p(x) only</b>: always 1. That's just checking the distribution adds up.</div>
<div class="wrong"><b>E[f(X)] = f(E[X])</b>: for f(x) = x² on a die: E[X²] = 15.17, but (E[X])² = 12.25. Only equal when f is a straight line.</div>
<div class="right">E[X] = Σ x · p(x): die 3.5, lottery −1 € ✓</div>

## 🗣️ Say it out loud

"E of X is the sum over x of x times p of x."

## 🤖 Where AI uses it

Every loss is an expected value over the data: L = E_{(x,y)∼data}[loss]. RLHF and GRPO maximise expected reward. Mini-batch averages are **estimates** of these expectations (lesson 09).

## 🎯 Your quest

Distributions are dicts `{value: probability}`.

1. `expected(d)`: E[X].
2. `expected_f(d, f)`: E[f(X)].
3. `expected_reward(policy, rewards)`: `policy` maps answers to probabilities, `rewards` maps answers to rewards.

**Remember:** weight each outcome by its probability, then add.

## Review

<details><summary>How do you sample with u = 0.65 from cat 0.5, dog 0.3, fish 0.2?</summary>Running totals 0.5, 0.8, 1.0 → first above 0.65 is dog.</details>
<details><summary>What does X ∼ p mean?</summary>X is drawn from distribution p.</details>
