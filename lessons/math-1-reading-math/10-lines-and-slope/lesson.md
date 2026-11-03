---
title: Straight lines and slope
xp: 40
---
# How steep is it?

> **Warm-up:** a taxi costs 3 euros to get in, then 2 euros per km. Draw (in your head) the price against the distance. What shape is it?

**In one sentence:** a straight line is described by where it starts and how steep it is, and steepness (slope) is "how much it goes up for each step to the right".

## 🪜 Plain words

The taxi price starts at 3 euros (at 0 km) and goes up by the **same amount** for every km. Same increase every step = a straight line. The bigger the increase per step, the **steeper** the line.

Steepness is called the **slope**. To measure it between two spots on a line: "how much did it go up, divided by how far did it go across". Going **down** to the right gives a **negative** slope. A flat line has slope 0.

## 🪜 With numbers

- Taxi: 0 km → 3 €, 1 km → 5 €, 2 km → 7 €, 10 km → 23 €.
- Slope between (1, 5) and (2, 7): up 7 − 5 = 2, across 2 − 1 = 1, so 2 / 1 = **2 euros per km**.
- Loss going from 2.5 at step 0 to 1.5 at step 100: up −1.0, across 100 → slope −0.01 per step (falling).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `m` | "m" | the **slope** (steepness) | `m` |
| `b` | "b" | the **intercept**: where the line crosses the y-axis (the value at x = 0) | `b` |
| `Δ` | "delta" | "the change in": Δy = new y − old y | `y2 - y1` |
| `Δy / Δx` | "delta y over delta x" | rise over run: the slope | `(y2 - y1) / (x2 - x1)` |
| `(x₁, y₁)` | "x one, y one" | the first point (small 1 = "number one", not a power) | `(x1, y1)` |

## 🔬 Take the formula apart

The line:

<div class="formula"><span class="k1">y</span> = <span class="k2">m</span><span class="k3">x</span> <span class="k4">+ b</span></div>

| Piece | Say it | Means | Taxi |
|---|---|---|---|
| <span class="k1">y</span> | "y" | the output (height) | price |
| <span class="k2">m</span> | "m" | slope: change in y per 1 step of x | 2 €/km |
| <span class="k3">x</span> | "x" | the input | km |
| <span class="k2">m</span><span class="k3">x</span> | "m x" | m **times** x (invisible times!) | 2 · 10 = 20 |
| <span class="k4">+ b</span> | "plus b" | the starting value at x = 0 | + 3 → 23 € |

The slope from two points:

<div class="formula"><span class="k2">m</span> = <span class="k5">(y₂ − y₁)</span> / <span class="k6">(x₂ − x₁)</span></div>

| Piece | Say it | Means | (1, 5) and (2, 7) |
|---|---|---|---|
| <span class="k5">(y₂ − y₁)</span> | "y two minus y one" | how much it went **up** (rise, Δy) | 7 − 5 = 2 |
| `/` | "divided by" | per | |
| <span class="k6">(x₂ − x₁)</span> | "x two minus x one" | how far it went **across** (run, Δx) | 2 − 1 = 1 |
| <span class="k2">m</span> | "m" | the slope | 2 / 1 = 2 |

## 🔀 What if the formula were different?

<div class="wrong"><b>m = (x₂ − x₁) / (y₂ − y₁)</b> (upside down): 1 / 2 = 0.5. You'd say the taxi costs 50 cents per km.</div>
<div class="wrong"><b>m = (y₂ − y₁) / (x₁ − x₂)</b> (mixed order): 2 / (−1) = −2. The taxi gets <i>cheaper</i> the further you go! Both differences must go the same way (2 minus 1, 2 minus 1).</div>
<div class="wrong"><b>y = mx</b> (forgot + b): 10 km costs 20 € instead of 23 €; the line is forced through 0.</div>
<div class="right"><b>y = mx + b</b> with m = 2, b = 3: 23 € for 10 km ✓</div>

## 🗣️ Say it out loud

`y = mx + b` → "y equals m x plus b" → "start at b, and go up m for every step of x."

## 🤖 Where AI uses it

A single neuron **is** `y = wx + b` (w for weight instead of m). And in Math 3, the slope becomes the **derivative**: training reads the slope of the loss to know which way is downhill.

## 🎯 Your quest

1. `slope(p1, p2)`: points are `(x, y)` tuples.
2. `line_through(p1, p2)`: return `(m, b)`. (Find m, then solve `y₁ = m·x₁ + b` for b.)
3. `predict(m, b, x)`.

**Remember:** slope = rise / run = Δy / Δx.

## Review

<details><summary>Is the point (2, 5) on the graph of f(x) = 2x + 1?</summary>Yes: f(2) = 5.</details>
<details><summary>Solve 2x + 3 = 11.</summary>x = 4.</details>
