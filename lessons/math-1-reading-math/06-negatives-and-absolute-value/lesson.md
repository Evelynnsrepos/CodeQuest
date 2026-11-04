---
title: Negative numbers and absolute value
xp: 25
---
# Direction and distance

> **Warm-up:** your model guessed 7 when the answer was 10. Another time it guessed 13 when the answer was 10. Which mistake was bigger?

**In one sentence:** a minus sign says "the other direction", and the absolute value says "how far", ignoring the direction.

## 🪜 Plain words

Think of a thermometer. Above zero is warm, below zero is cold: −5 °C is 5 degrees **below** zero. Negative numbers are just "the other side of zero".

Sometimes you only care **how far** something is, not which side. "I'm 3 km from home" is true whether you went north or south. That "how far" is the **absolute value**.

## 🪜 With numbers

- Guessed 7, answer 10: the guess was 3 **too low**. Answer minus guess = 10 − 7 = 3.
- Guessed 13, answer 10: the guess was 3 **too high**. 10 − 13 = −3.
- Both mistakes are **3 big**. If you average 3 and −3 you get 0, which wrongly says "no mistakes at all"! So we drop the signs first: 3 and 3, average **3**.

Rules for minus signs:

- Taking away a negative is adding: 5 − (−3) = 8 (removing a debt makes you richer).
- Negative times negative is positive: (−2) · (−3) = 6. Negative times positive is negative: (−2) · 3 = −6.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `−x` | "minus x" / "negative x" | the opposite of x | `-x` |
| `\|x\|` | "the absolute value of x" | x without its sign: `\|−3\| = 3`, `\|3\| = 3` | `abs(x)` |
| `ŷ` | "y hat" | a **guess** or **prediction** of y (the hat means "estimated") | `y_pred` |

## 🔬 Take the formula apart

The **mean absolute error** (how wrong a model is on average):

<div class="formula"><span class="k1">MAE</span> = <span class="k2">average of</span> <span class="k3">|</span><span class="k4">y</span> <span class="k5">− ŷ</span><span class="k3">|</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k1">MAE</span> | "M A E" | the answer: mean absolute error | 3 |
| <span class="k4">y</span> | "y" | the true answer | 10 and 10 |
| <span class="k5">− ŷ</span> | "minus y hat" | minus the model's guess | 10 − 7 = 3, 10 − 13 = −3 |
| <span class="k3">\| … \|</span> | "the absolute value of …" | drop the sign: how far off | 3 and 3 |
| <span class="k2">average of</span> | "the average of" | add them all, divide by how many (written with Σ in lesson 12) | (3 + 3) / 2 = 3 |

## 🔀 What if the formula were different?

<div class="wrong"><b>average of (y − ŷ)</b> (no absolute value): (3 + (−3)) / 2 = 0. "Perfect model!" It's not: the errors just cancelled.</div>
<div class="wrong"><b>|average of (y − ŷ)|</b> (absolute value outside): |0| = 0. Same problem: the signs cancel <i>before</i> they're removed.</div>
<div class="right"><b>average of |y − ŷ|</b>: 3. The model is off by 3 on average ✓</div>

Careful with powers: `(−3)²` = 9, but `−3²` means −(3²) = −9, because the power happens before the minus.

## 🗣️ Say it out loud

`|y − ŷ|` → "the absolute value of y minus y hat" → "how far the guess was from the truth".

## 🤖 Where AI uses it

Measuring error (MAE here, squared errors later), and gradients that are positive or negative tell training which **direction** to change each weight.

## 🎯 Your quest

1. `distance(a, b)`: `|a − b|`.
2. `mae(ys, preds)`: the average of `|y − ŷ|` over all pairs.

**Remember:** absolute value = how far, no matter which way.

## Review

<details><summary>What's the percent change from 4 to 3?</summary>−25%.</details>
<details><summary>Solve 2x − 4 = 6.</summary>x = 5.</details>
