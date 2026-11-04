---
title: Confidence intervals: score ± error bars
xp: 55
---
# 60% ± how much?

> **Warm-up:** in a blind test, people preferred your fine-tuned model in 60 of 100 comparisons. Is it really better than 50/50, or could that be luck?

**In one sentence:** a 95% confidence interval is "estimate ± 1.96 standard errors", a range built so that 95% of the time it contains the true value.

## 🪜 Plain words

Any measured number is a guess with wobble. Instead of reporting just "60%", report a **range**: "somewhere between 50.4% and 69.6%".

How wide? About **2 standard errors** each way (exactly 1.96 for 95%, because 95% of a normal curve lies within 1.96σ, lesson 08).

If the whole range is above 50%, you have decent evidence the model really is preferred.

## 🪜 With numbers

**Win rate:** 60 wins of 100.
- p̂ = 0.6, σ of one comparison = √(0.6 · 0.4) = 0.49
- SE = 0.49 / √100 = **0.049**
- 95% CI = 0.6 ± 1.96 · 0.049 = **0.504 to 0.696**: just above 0.5.

**Average score** of 5 runs: 70, 72, 68, 75, 65.
- mean 70, sample σ = 3.81 (dividing by n − 1 = 4, see below)
- SE = 3.81 / √5 = 1.70
- 95% CI = 70 ± 3.34 = **66.7 to 73.3**

Why **n − 1** for a sample? Your sample's own mean sits a bit closer to the data than the true mean does, so dividing by n slightly underestimates σ. Dividing by n − 1 corrects that (statistics calls it "Bessel's correction").

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `p̂` | "p hat" | the measured proportion (hat = estimate) | `wins / n` |
| `±` | "plus or minus" | the range from minus to plus | `(m - e, m + e)` |
| `1.96` | "one point nine six" | how many SEs for 95% | |
| `s` | "s" | the **sample** standard deviation (divide by n − 1) | `statistics.stdev` |
| `CI` | "confidence interval" | the range | |
| `[a, b]` | "from a to b" | an interval (Math 1) | `(a, b)` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">CI</span> = <span class="k2">p̂</span> <span class="k3">±</span> <span class="k4">1.96</span> · <span class="k5">√( p̂ (1 − p̂) / n )</span></div>

| Piece | Say it | Means | 60 of 100 |
|---|---|---|---|
| <span class="k2">p̂</span> | "p hat" | measured win rate | 0.6 |
| <span class="k5">√( p̂ (1 − p̂) / n )</span> | "root of p hat times one minus p hat, over n" | standard error of a proportion | 0.049 |
| <span class="k4">1.96</span> | "one ninety-six" | 95% width | |
| <span class="k3">±</span> | "plus or minus" | go that far down **and** up | ± 0.096 |
| <span class="k1">CI</span> | "confidence interval" | the range | 0.504 to 0.696 |

For an average: <span class="k2">x̄</span> ± <span class="k4">1.96</span> · <span class="k5">s / √n</span>.

## 🔀 What if it were different?

<div class="wrong"><b>Forget √n</b>: 0.6 ± 1.96 · 0.49 = −0.36 to 1.56. A range wider than 0..1: meaningless. For the scores: 70 ± 7.46.</div>
<div class="wrong"><b>Use 1 instead of 1.96</b>: 0.551 to 0.649. Looks tighter, but it only catches the truth 68% of the time. You'd be wrong about 1 time in 3.</div>
<div class="wrong"><b>Report "60%" with no interval</b>: with 10 comparisons (6 wins) the interval is 0.30 to 0.90. Same 60%, almost no information.</div>
<div class="right">0.504 to 0.696 for 60/100; 66.7 to 73.3 for the scores ✓</div>

## 🗣️ Say it out loud

"p hat plus or minus one point nine six times the standard error."

## 🤖 Where AI uses it

Every serious leaderboard (LMArena shows CIs), every A/B test of a prompt or model, LLMs 7's blind eval. Rule of thumb: if two models' intervals overlap a lot, you can't call a winner yet.

## 🎯 Your quest

1. `proportion_ci(wins, n)`: `(low, high)`.
2. `sample_std(xs)`: σ dividing by n − 1.
3. `mean_ci(xs)`: `(low, high)` using `sample_std` and 1.96.

**Remember:** a number without ± is half a result.

## Review

<details><summary>What does argmax return?</summary>The setting that gives the biggest value, not the value.</details>
<details><summary>Why sum logs instead of multiplying probabilities?</summary>Products of many small numbers underflow to 0.</details>
