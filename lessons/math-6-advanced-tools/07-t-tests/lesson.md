---
title: t-tests: is model A really better?
xp: 60
---
# Two averages, a lot of wobble

> **Warm-up:** model A scored 72, 75, 70, 74, 69 over five runs; model B scored 68, 70, 66, 71, 65. A wins on average by 4 points. Luck?

**In one sentence:** a t-test divides the difference between two averages by its standard error; if that ratio t is bigger than the cut-off from the t-table, the difference is unlikely to be luck.

## 🪜 Plain words

Math 4 lesson 12 tested a win rate against 50%. Here we compare **two averages**, each with its own wobble:

1. The **difference** of the means: how far apart they are.
2. The **standard error** of that difference: how much it would wobble by chance. Both groups' wobbles add up (their squares do, like Pythagoras).
3. **t** = difference ÷ standard error. "How many wobbles apart are they?"
4. Compare with the **t-value** for 95% (Math 4 lesson 11) at the right **degrees of freedom**. Bigger → significant.

This version (**Welch's t-test**) doesn't assume both groups wobble equally. Its degrees of freedom come from a formula given in the starter; you just compute it.

## 🪜 With numbers

- Means: A = 72, B = 68 → difference **4**.
- Sample variances (Math 4 lesson 07, ÷ (n − 1)): both **6.5**.
- SE = √(6.5/5 + 6.5/5) = √2.6 = **1.612**.
- t = 4 / 1.612 = **2.48**; degrees of freedom = **8**; t-table at 8: **2.306**.
- 2.48 > 2.306 → **significant** at 5% (two-sided). But only just: with these few runs, a 4-point gap is at the edge.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `x̄_A` | "x bar A" | mean of group A | `statistics.mean(a)` |
| `s²_A` | "s squared A" | sample variance of A | `statistics.variance(a)` |
| `n_A` | "n A" | runs in group A | `len(a)` |
| `t` | "t" | the test statistic | |
| `df` | "degrees of freedom" | picks the row of the t-table | |
| `t*` | "t star" | the 95% cut-off | `T95[int(df)]` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">t</span> = ( <span class="k2">x̄_A − x̄_B</span> ) / <span class="k3">√( s²_A / n_A + s²_B / n_B )</span> &nbsp; significant if <span class="k4">|t| > t*</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k2">x̄_A − x̄_B</span> | "x bar A minus x bar B" | the gap | 4 |
| <span class="k3">s²_A / n_A</span> | "s squared A over n A" | A's mean wobble, squared | 1.3 |
| <span class="k3">√( … + … )</span> | "root of the sum" | the gap's standard error | 1.612 |
| <span class="k1">t</span> | "t" | gap in wobbles | 2.48 |
| <span class="k4">\|t\| > t*</span> | "absolute t greater than t star" | the verdict (either direction) | 2.48 > 2.306 ✓ |

## 🔀 What if it were different?

<div class="wrong"><b>Use 1.96 instead of the t-table</b>: with 8 degrees of freedom you'd call results significant too often (true error rate about 9%, not 5%). Small samples need the bigger t*.</div>
<div class="wrong"><b>Forget to divide by n</b>: SE = √(6.5 + 6.5) = 3.61, t = 1.11: you'd miss a real difference.</div>
<div class="wrong"><b>Run 20 comparisons and report the one that's significant</b>: the 64% fake-win problem of Math 4 lesson 12 again.</div>
<div class="right">t = 4 / 1.612 = 2.48 > 2.306: significant at 5% ✓</div>

## 🗣️ Say it out loud

"t is x bar A minus x bar B over the square root of s squared A over n A plus s squared B over n B."

## 🤖 Where AI uses it

Comparing two models or prompts over several random seeds, A/B tests of product changes, and reading papers ("improves by 1.2 ± 0.8, p = 0.04"). If a paper reports a gain from a single run, you now know to be suspicious.

## 🎯 Your quest

`T95` (95%, two-sided) is in the starter.

1. `welch(a, b)`: return `(t, df)`, with `df` from the formula in the starter's comment.
2. `significant(a, b)`: `True` if `abs(t) > t*`, where `t* = T95[int(df)]` (rounded **down**, the safer choice), or 1.96 if `int(df)` is above 30.

**Remember:** gap ÷ wobble, compared with the t-table.

## Review

<details><summary>Which way round is the chain rule for Jacobians?</summary>J of g after f = J_g(f(x)) · J_f(x): the last function on the left.</details>
