---
title: The derivative: speed at one instant
xp: 50
---
# Zoom in until it's a straight line

> **Warm-up:** a speedometer shows your speed **right now**, not your average over the trip. How could you measure "right now" speed with only a stopwatch and distance markers?

**In one sentence:** the derivative is the slope of a curve at a single point: the average rate of change over a step that shrinks to zero.

## 🪜 Plain words

In lesson 01 we measured average speed between two moments. To get speed **at one moment**, make the two moments closer and closer together. 1 second apart, 0.1 seconds, 0.01... The answers settle on one number (a limit, lesson 02). That number is the **derivative**.

Picture it: zoom into a curve far enough and it looks like a straight line. The derivative is that line's slope. It answers: **"If I nudge the input a tiny bit, how much does the output move, and in which direction?"**

## 🪜 With numbers

f(x) = x² at x = 3 (so f(3) = 9). Take a step h and measure the slope:

| step h | f(3 + h) | change ÷ h |
|---|---|---|
| 1 | 16 | (16 − 9) / 1 = 7 |
| 0.1 | 9.61 | 0.61 / 0.1 = 6.1 |
| 0.01 | 9.0601 | 0.0601 / 0.01 = 6.01 |
| 0.001 | 9.006001 | 6.001 |

Heading to **6**. So the slope of x² at x = 3 is 6: nudge x up by a tiny bit, the output goes up about 6 times that bit.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f'(x)` | "f prime of x" | the derivative of f, at x (the ' is a tiny tick mark) | `central_diff(f, x)` |
| `df/dx` | "d f d x" | the same thing, another notation: "tiny change in f over tiny change in x". **Not** a fraction you can cancel d's in! | |
| `d/dx` | "d by d x" | "take the derivative of what follows" | |
| `h` | "h" | the step size | `h = 1e-5` |
| `lim h→0` | "the limit as h goes to 0" | let the step shrink to nothing (lesson 02) | tiny `h` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">f'(x)</span> = <span class="k2">lim<sub>h→0</sub></span> ( <span class="k3">f(x + h)</span> − <span class="k4">f(x)</span> ) / <span class="k5">h</span></div>

| Piece | Say it | Means | x² at x = 3, h = 0.01 |
|---|---|---|---|
| <span class="k1">f'(x)</span> | "f prime of x" | the slope at x | → 6 |
| <span class="k4">f(x)</span> | "f of x" | where you are now | 9 |
| <span class="k3">f(x + h)</span> | "f of x plus h" | where you are after a small step | 9.0601 |
| <span class="k3">f(x + h)</span> − <span class="k4">f(x)</span> | "the difference" | Δy: how much the output moved | 0.0601 |
| / <span class="k5">h</span> | "over h" | per unit of step: Δy ÷ Δx | 6.01 |
| <span class="k2">lim<sub>h→0</sub></span> | "as h goes to zero" | let the step shrink | 6.01 → 6.001 → 6 |

It's lesson 01's `Δy / Δx` with `Δx = h`, made tiny.

## 🔀 What if it were different?

<div class="wrong"><b>Divide by x instead of h</b>: 0.0601 / 3 = 0.02. Nonsense: the slope would depend on where zero happens to be.</div>
<div class="wrong"><b>Forget the limit, use h = 1</b>: 7 instead of 6. A big step measures an average over a stretch, not the slope at the point.</div>
<div class="wrong"><b>h = 1e-15 in a computer</b>: (f(3 + 1e-15) − 9) / 1e-15 = 5.33. Floats only keep about 16 digits, so a too-tiny step drowns in rounding noise.</div>
<div class="right">a small but sensible h (like 1e-5), and even better the <b>central</b> version: ( f(x + h) − f(x − h) ) / 2h → 6.0000000 ✓</div>

## 🗣️ Say it out loud

`f'(3) = 6` → "f prime of 3 is 6" → "at x = 3, the output changes 6 times as fast as the input."

## 🤖 Where AI uses it

Everywhere in training. For every weight, the model asks: "If I nudge this weight, does the loss go up or down, and how much?" That's a derivative. Engineers also use the central difference to **check** that a hand-written gradient is correct ("gradient checking").

## 🎯 Your quest

1. `forward_diff(f, x, h)`: `(f(x + h) − f(x)) / h`.
2. `central_diff(f, x, h=1e-5)`: `(f(x + h) − f(x − h)) / (2h)`.
3. `tangent(f, x)`: the straight line touching f at x as `(m, b)`: `m = central_diff(f, x)`, `b = f(x) − m·x`.

**Remember:** derivative = slope at one point = how much the output moves per tiny nudge.

## Review

<details><summary>Limit of (x² − 1)/(x − 1) as x → 1?</summary>2.</details>
<details><summary>When does a limit not exist?</summary>When the left side and the right side head to different numbers.</details>
