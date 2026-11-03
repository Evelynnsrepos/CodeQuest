---
title: Numbers and the four operations
xp: 20
---
# Plus, minus, times, divided by

> **Warm-up:** you have 12 GB of memory and a model takes 5 GB. How much is left? If you run 2 copies, how much do they take? If you split 12 GB between 3 programs equally, how much does each get?

**In one sentence:** almost all math is built from four operations: add, subtract, multiply, divide, and each has its own sign.

## 🪜 Plain words

- **Adding** puts amounts together.
- **Subtracting** takes some away (or finds the difference).
- **Multiplying** is adding the same amount many times: "3 times 4" is 4 + 4 + 4.
- **Dividing** splits into equal parts, or asks "how many fit?".

Numbers with a point (**decimals**) like 2.5 are just "between" whole numbers: 2.5 is halfway between 2 and 3.

## 🪜 With numbers

- 12 GB minus 5 GB leaves 7 GB.
- 2 copies of 5 GB: 2 times 5 is 10 GB.
- 12 GB split 3 ways: 12 divided by 3 is 4 GB each.
- 7 divided by 2 is 3.5 (halfway between 3 and 4).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `+` | "plus" | add | `+` |
| `−` | "minus" | subtract | `-` |
| `×` or `·` | "times" | multiply. In formulas often **invisible**: `3x` = 3 times x | `*` |
| `÷` or `/` or a fraction bar | "divided by" / "over" | divide | `/` |
| `=` | "equals" | same value on both sides | `==` |
| `≠` | "is not equal to" | different values | `!=` |
| `<` `>` | "less than", "greater than" | the open side faces the bigger number | `<` `>` |
| `≤` `≥` | "less than or equal", "greater than or equal" | | `<=` `>=` |

## 🔬 Take the formula apart

How much memory is left after loading a model?

<div class="formula"><span class="k1">left</span> = <span class="k2">total</span> <span class="k3">−</span> <span class="k4">model</span></div>

| Piece | Say it | Means | In our example |
|---|---|---|---|
| <span class="k1">left</span> | "left" | the answer | 7 |
| `=` | "equals" | is the same as | |
| <span class="k2">total</span> | "total" | all the memory | 12 |
| <span class="k3">−</span> | "minus" | take away | |
| <span class="k4">model</span> | "model" | what the model uses | 5 |

And "does it fit?":

<div class="formula"><span class="k4">model</span> <span class="k5">≤</span> <span class="k2">total</span></div>

| Piece | Say it | Means | In our example |
|---|---|---|---|
| <span class="k4">model</span> | "model" | the model's size | 5 |
| <span class="k5">≤</span> | "is less than or equal to" | not bigger than | 5 ≤ 12 is **true** |
| <span class="k2">total</span> | "total" | the memory | 12 |

## 🔀 What if the formula were different?

<div class="wrong"><b>left = model − total</b> (swapped): 5 − 12 = −7 GB left. Negative memory doesn't exist; the order of a minus matters.</div>
<div class="wrong"><b>model &lt; total</b> (strictly less): a 12 GB model in 12 GB would count as "doesn't fit", even though it exactly fits. The little line under ≤ matters.</div>
<div class="right"><b>left = total − model</b>: 12 − 5 = 7 GB ✓</div>

## 🗣️ Say it out loud

`left = total − model` → "left equals total minus model."

## 🤖 Where AI uses it

Fitting models in VRAM (subtracting and comparing), counting tokens (adding), file sizes (multiplying parameters by bytes), averages (dividing).

## 🎯 Your quest

1. `left(total, model)`: memory left.
2. `fits(model, total)`: `True` if `model ≤ total`.
3. `per_program(total, n)`: total split equally into `n` parts.

**Remember:** in formulas, the times sign is often invisible.

## Review

<details><summary>What does 3x mean?</summary>3 times x.</details>
<details><summary>What is a formula, in one sentence?</summary>A recipe written in short math code.</details>
