---
title: P(A): what probability means
xp: 35
---
# How likely, as a number from 0 to 1

> **Warm-up:** you roll a normal six-sided die. How likely is a 6? How likely is "not a 6"? Say it as a fraction.

**In one sentence:** a probability is a number from 0 (never) to 1 (always) that says how likely something is, and "fair" cases are counted as good outcomes ÷ all outcomes.

## 🪜 Plain words

- 0 = impossible. 1 = certain. 0.5 = half the time.
- If all outcomes are equally likely: count the outcomes you want, divide by all outcomes.
- "Not happening" is everything that's left: 1 minus the chance it happens.
- Probabilities are often written as percentages: 0.25 = 25%.

## 🪜 With numbers

A die has 6 equally likely faces.

- P(6) = 1 ÷ 6 ≈ **0.167**
- P(even) = 3 ÷ 6 = **0.5** (2, 4, 6)
- P(not 6) = 1 − 1/6 = 5/6 ≈ **0.833**

An LLM gives "Paris" a probability of 0.92 as the next token. P(not "Paris") = **0.08**: all other tokens share 8%.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `P(A)` | "P of A" / "probability of A" | how likely event A is | `p_a` |
| `A` | "A" | an **event**: something that may or may not happen | |
| `Aᶜ` or `¬A` or `Ā` | "not A" / "A complement" | A does **not** happen | `not a` |
| `\|A\|` | "size of A" | number of outcomes in A (here bars = count, not absolute value!) | `len(A)` |
| `Ω` | "omega" | all possible outcomes | `[1, 2, 3, 4, 5, 6]` |
| `∈ [0, 1]` | "is in zero to one" | between 0 and 1, both included (Math 1) | `0 <= p <= 1` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">P(A)</span> = <span class="k2">|A|</span> / <span class="k3">|Ω|</span> &nbsp;&nbsp;&nbsp; <span class="k4">P(Aᶜ)</span> = <span class="k5">1</span> − <span class="k1">P(A)</span></div>

| Piece | Say it | Means | P(even) on a die |
|---|---|---|---|
| <span class="k2">\|A\|</span> | "size of A" | how many outcomes you want | 3 |
| <span class="k3">\|Ω\|</span> | "size of omega" | how many outcomes exist | 6 |
| <span class="k1">P(A)</span> | "P of A" | wanted ÷ all | 0.5 |
| <span class="k5">1</span> | "one" | certain: something happens | |
| <span class="k4">P(Aᶜ)</span> | "P of not A" | what's left | 0.5 |

## 🔀 What if it were different?

<div class="wrong"><b>|Ω| / |A| (upside down)</b>: 6 / 1 = 6 for rolling a 6. A probability can never be above 1: if you see one, the fraction is flipped.</div>
<div class="wrong"><b>P(not A) = P(A)</b>: you'd say "not a 6" is 1/6 too. Together they'd add to 1/3, but "6 or not 6" is certain: they must add to 1.</div>
<div class="wrong"><b>Counting outcomes that aren't equally likely</b>: "I either win the lottery or I don't: 2 outcomes, so 50%". Counting only works when every outcome is equally likely.</div>
<div class="right">P(6) = 1/6, P(not 6) = 5/6, sum 1 ✓</div>

## 🗣️ Say it out loud

`P(Aᶜ) = 1 − P(A)` → "the probability of not A is one minus the probability of A."

## 🤖 Where AI uses it

Every LLM output is a probability for each possible next token (LLMs 1). They must all be between 0 and 1 and add to 1; softmax makes sure of that.

## 🎯 Your quest

1. `prob(wanted, total)`: wanted ÷ total.
2. `complement(p)`: 1 − p.
3. `is_valid(p)`: `True` if 0 ≤ p ≤ 1.

**Remember:** probabilities live between 0 and 1; "not" is 1 minus.

## Review

<details><summary>What does ∫ₐᵇ f(x) dx mean?</summary>The area under f from a to b.</details>
<details><summary>Gradient descent update?</summary>θ ← θ − η∇L(θ).</details>
