---
title: Negative numbers and absolute value
xp: 25
---
# Direction and distance

> **Warm-up:** your model predicted 7 and the answer was 10. Another time it predicted 13 and the answer was 10. Were both mistakes equally big?

**In one sentence:** the sign of a number says which direction; the absolute value says how far, ignoring direction.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `−x` | "minus x" / "negative x" | the opposite of x | `-x` |
| `\|x\|` | "the absolute value of x" | distance from 0, never negative: `\|−3\| = 3` | `abs(x)` |
| `\|a − b\|` | "the distance between a and b" | how far apart two numbers are | `abs(a - b)` |
| `ŷ` | "y hat" | a **predicted** value (the hat means "estimate") | `y_pred` |

## The idea

Picture a number line: negatives to the left of 0, positives to the right.

- **Minus a minus is a plus:** `5 − (−3) = 8`. Removing a debt makes you richer.
- **Two negatives multiplied are positive:** `(−2) · (−3) = 6`. One negative: negative.
- **Squaring kills the sign:** `(−3)² = 9`. Careful: `−3²` means `−(3²) = −9`, because the exponent goes first!
- **Absolute value:** drop the sign. `|4| = 4`, `|−4| = 4`.

## 🗣️ Say it out loud

`|y − ŷ|` → "the distance between the true y and the predicted y hat", in other words "how wrong was the guess".

## 🧮 Worked example

Errors for truth `[10, 10]`, predictions `[7, 13]`:

1. Raw differences: `10 − 7 = 3` and `10 − 13 = −3`. Averaged, they cancel to 0. Misleading!
2. Absolute: `|3| = 3`, `|−3| = 3`, average **3**. That's the **mean absolute error (MAE)**.

## 🤖 Where AI uses it

Error measures (MAE, and squared errors in Math 3), gradients being positive or negative (which direction to move a weight), and weights themselves being negative ("this input makes the output smaller").

## 🎯 Your quest

1. `distance(a, b)`: `|a − b|`.
2. `mae(ys, preds)`: the average of `|y − ŷ|` over all pairs.

**Remember:** absolute value means "how far, no matter which way".

## Review

<details><summary>What's the percent change from 4 to 3?</summary>−25%.</details>
<details><summary>What is −3² in math?</summary>−9: the square happens before the minus.</details>
