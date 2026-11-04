---
title: Checkpoint: is the new model really better?
xp: 80
---
# Write the evaluation report

> **Warm-up:** your fine-tuned model won 60 of 100 blind comparisons against the base model. What three numbers belong in your report?

(The win rate, its 95% interval, and the p-value against 50/50.)

## 🪜 The plan

Combine this course into one honest verdict:

1. **Win rate** p̂ = wins / n (lesson 01).
2. **95% CI** = p̂ ± 1.96 · √(p̂(1 − p̂)/n) (lesson 11).
3. **p-value** = P(X ≥ wins) if the true rate were 0.5 (lesson 12). This is **one-sided**: we only ask "is the new model *better*?". (Two-sided, "better or worse?", would give 0.057 for 60/100 and not pass.)
4. **Verdict:** "better" only if p < 0.05 **and** the whole CI is above 0.5.

## 🔬 The formulas, one more time

<div class="formula"><span class="k1">p̂</span> <span class="k2">± 1.96 √( p̂(1 − p̂) / n )</span> &nbsp;&nbsp; <span class="k3">p</span> = <span class="k4">Σ<sub>j ≥ wins</sub></span> <span class="k5">C(n, j) 0.5ⁿ</span></div>

| Piece | Means |
|---|---|
| <span class="k1">p̂</span> | measured win rate |
| <span class="k2">± 1.96 √(…)</span> | 95% error bars |
| <span class="k3">p</span> | p-value |
| <span class="k4">Σ<sub>j ≥ wins</sub></span> | this many wins **or more** |
| <span class="k5">C(n, j) 0.5ⁿ</span> | chance of exactly j wins if it's a coin flip (with p = 0.5, pʲ(1 − p)ⁿ⁻ʲ = 0.5ⁿ) |

## 🔀 What if it were different?

<div class="wrong"><b>Verdict from the win rate alone</b>: 6 of 10 = 60% → "better!". The CI is 0.30 to 0.90 and p = 0.38: no evidence at all.</div>
<div class="right">60 of 100: CI 0.504–0.696, p = 0.028 → better (barely). 600 of 1000: CI 0.570–0.630 → clearly better ✓</div>

## 🎯 Your quest

1. `report(wins, n)`: return a dict with keys `"rate"`, `"low"`, `"high"`, `"p_value"`, `"better"`.

Next: Math 5, information theory and optimization: entropy, cross-entropy, KL, and how Adam trains models.

## Review

<details><summary>p-value in one sentence?</summary>The chance, if nothing special were happening, of a result at least this extreme.</details>
<details><summary>Bayes' rule?</summary>P(A | B) = P(B | A) P(A) / P(B).</details>
<details><summary>E[X] formula?</summary>Σ x · p(x).</details>
