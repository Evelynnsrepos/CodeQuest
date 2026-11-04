---
title: Hypothesis tests and p-values
xp: 60
---
# Could this just be luck?

> **Warm-up:** a coin you think is fair lands heads 15 times out of 20. Suspicious? How would you decide?

**In one sentence:** a p-value is the probability of seeing a result at least this extreme **if nothing special were going on**; a small p-value means "luck alone rarely does this".

## 🪜 Plain words

1. Assume the boring explanation: the **null hypothesis** (the coin is fair; the new model is no better).
2. Ask: if that were true, how often would I see something **this extreme or more**?
3. If that's rare (usually below 5%), reject the boring explanation: the result is **statistically significant**.

The p-value is **not** "the chance the boring explanation is true". It's "how surprising my data would be if it were".

## 🪜 With numbers

**Coin:** 20 fair flips, P(15 or more heads) = **0.021**. Only 2% of fair coins do this. Significant at 5%.

**Model:** preferred in 60 of 100 comparisons. If it were really 50/50, P(60 or more) = **0.028**. Significant at 5% (just).

**Many tests:** test 20 prompts that are all secretly useless, each at the 5% level: P(at least one looks "significant") = 1 − 0.95²⁰ = **0.64** (lesson 02!). Try enough things and something will look like a win.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `H₀` | "H nought" / "the null hypothesis" | the boring explanation | |
| `H₁` | "H one" / "the alternative" | something real is happening | |
| `α` | "alpha" | the cut-off, usually 0.05 | `alpha=0.05` |
| `p` | "the p-value" | P(this extreme or more \| H₀) | |
| `C(n, k)` or `(n k)` | "n choose k" | number of ways to pick k of n (Math 1) | `math.comb(n, k)` |
| `≥` | "at least" | | `>=` |

## 🔬 Take the formula apart

<div class="formula">P(X = <span class="k1">k</span>) = <span class="k2">C(n, k)</span> · <span class="k3">p<sup>k</sup></span> · <span class="k4">(1 − p)<sup>n − k</sup></span></div>

| Piece | Say it | Means | 15 heads in 20, p = 0.5 |
|---|---|---|---|
| <span class="k1">k</span> | "k" | number of successes | 15 |
| <span class="k2">C(n, k)</span> | "n choose k" | how many orders could give k successes | 15504 |
| <span class="k3">p<sup>k</sup></span> | "p to the k" | k successes (AND = multiply) | 0.5¹⁵ |
| <span class="k4">(1 − p)<sup>n − k</sup></span> | "one minus p to the n minus k" | the rest are failures | 0.5⁵ |

<div class="formula"><span class="k5">p-value</span> = <span class="k6">Σ<sub>j = k</sub><sup>n</sup></span> P(X = j)</div>

| Piece | Means | Example |
|---|---|---|
| <span class="k6">Σ<sub>j = k</sub><sup>n</sup></span> | add up k, k + 1, …, n: "this extreme **or more**" | 15..20 |
| <span class="k5">p-value</span> | total chance under H₀ | 0.021 |

## 🔀 What if it were different?

<div class="wrong"><b>Only P(X = 15)</b>, not "or more": 0.015. Any single exact outcome is rare (even exactly 10 heads is only 18%), so this would call everything suspicious.</div>
<div class="wrong"><b>"p = 0.028 means a 2.8% chance the model isn't better"</b>: no. It's the chance of data this good <i>if</i> it weren't better. Those are different (Bayes, lesson 04).</div>
<div class="wrong"><b>Test 20 things, report the one with p &lt; 0.05</b>: 64% chance of a fake win. Fix: fewer, planned tests, or a stricter α (e.g. 0.05 / 20).</div>
<div class="right">p = 0.021 for 15/20 heads, 0.028 for 60/100 wins ✓</div>

## 🗣️ Say it out loud

"The p-value is the probability, under H nought, of a result at least this extreme."

## 🤖 Where AI uses it

A/B tests of models and prompts, "is this eval improvement real?", and spotting benchmark contamination (a model scoring far above chance on questions it should not know).

## 🎯 Your quest

1. `binom_pmf(k, n, p)`.
2. `p_value_at_least(k, n, p)`: P(X ≥ k).
3. `significant(p_value, alpha=0.05)`: `True` if below alpha.

**Remember:** small p = "luck rarely does this", not "probably true".

## Review

<details><summary>95% CI for 60 wins of 100?</summary>About 0.504 to 0.696.</details>
<details><summary>Why n − 1 in the sample σ?</summary>The sample's own mean sits closer to the data, so dividing by n would underestimate σ.</details>
