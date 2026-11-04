---
title: Bayes' rule: flipping the question
xp: 60
---
# The test is 90% accurate. Are you 90% likely sick?

> **Warm-up:** a disease affects 1% of people. A test catches 90% of sick people, but also wrongly says "positive" for 9% of healthy people. You test positive. How likely are you to be sick? Guess a number before reading.

**In one sentence:** Bayes' rule turns P(evidence | cause) into P(cause | evidence) by weighing in how common the cause was to begin with.

## 🪜 Plain words

Imagine **1000 people**.

- 1% are sick: **10 people**. The test catches 90% of them: **9 true positives**.
- 990 are healthy. 9% get a false alarm: about **89 false positives**.
- Positives in total: 9 + 89 = **98**. Of those, only 9 are sick.

So a positive means about 9 ÷ 98 ≈ **9%** chance of being sick. Not 90%! Because healthy people vastly outnumber sick people, their small error rate produces most of the positives.

## 🪜 With numbers

- P(sick) = 0.01 (the **prior**: belief before the test)
- P(+ | sick) = 0.9, P(+ | healthy) = 0.09
- P(+) = 0.9 · 0.01 + 0.09 · 0.99 = 0.009 + 0.0891 = **0.0981**
- P(sick | +) = 0.009 ÷ 0.0981 = **0.0917** (the **posterior**: belief after)

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `P(A \| B)` | "P of A given B" | chance of A, knowing B (lesson 03) | |
| `P(A)` | "the prior" | belief **before** the evidence | `p_a` |
| `P(B \| A)` | "the likelihood" | how well A explains the evidence | `p_b_given_a` |
| `P(A \| B)` | "the posterior" | belief **after** the evidence | |
| `¬A` | "not A" | | `1 - p_a` |
| `∝` | "is proportional to" | equal up to a fixed scaling | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">P(A | B)</span> = <span class="k2">P(B | A)</span> · <span class="k3">P(A)</span> / <span class="k4">P(B)</span></div>

<div class="formula"><span class="k4">P(B)</span> = <span class="k2">P(B | A)</span> · <span class="k3">P(A)</span> + <span class="k5">P(B | ¬A)</span> · <span class="k6">P(¬A)</span></div>

| Piece | Say it | Means | Test example |
|---|---|---|---|
| <span class="k1">P(A \| B)</span> | "P of sick given positive" | the answer we want | 0.0917 |
| <span class="k2">P(B \| A)</span> | "P of positive given sick" | test catches sick people | 0.9 |
| <span class="k3">P(A)</span> | "P of sick" | how common it is (prior) | 0.01 |
| <span class="k5">P(B \| ¬A)</span> | "P of positive given healthy" | false alarm rate | 0.09 |
| <span class="k6">P(¬A)</span> | "P of healthy" | 1 − prior | 0.99 |
| <span class="k4">P(B)</span> | "P of positive" | all ways to get a positive | 0.0981 |

## 🔀 What if it were different?

<div class="wrong"><b>P(sick | +) = P(+ | sick)</b>: 0.9. Ten times too scary. This "flipped conditional" error appears in courtrooms, medicine and AI evaluation.</div>
<div class="wrong"><b>Forget the prior P(A)</b>: 0.9 / 0.0981 = 9.17. A probability above 1: impossible, so something's missing.</div>
<div class="wrong"><b>P(B) = P(B | A) only</b> (forgetting false positives from healthy people): 0.009 / 0.9 = 0.01. You'd say a positive test tells you nothing.</div>
<div class="right">P(sick | +) = 0.009 / 0.0981 ≈ 0.092 ✓</div>

## 🗣️ Say it out loud

"Posterior equals likelihood times prior, over evidence."

## 🤖 Where AI uses it

Spam filters (naive Bayes), evaluating AI detectors and safety classifiers (a 99%-accurate detector on rare events still gives mostly false alarms), and the whole idea of updating beliefs with data. RLHF's KL penalty (Math 5) can be read as "keep the prior model, update it with reward evidence".

## 🎯 Your quest

1. `total_prob(p_b_given_a, p_a, p_b_given_not_a)`: P(B).
2. `bayes(p_b_given_a, p_a, p_b_given_not_a)`: P(A | B).

**Remember:** a positive from a rare thing is usually a false alarm, unless the test is extremely good.

## Review

<details><summary>P(A | B)?</summary>P(A ∩ B) / P(B).</details>
<details><summary>How does an LLM score a sentence?</summary>Multiply P(each token | all tokens before it).</details>
