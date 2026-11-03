---
title: Graphs and coordinates
xp: 30
---
# Drawing numbers as pictures

> **Warm-up:** you write down your training loss after every 100 steps. How could you *see* at a glance whether it's going down?

**In one sentence:** a graph turns pairs of numbers into dots on a grid, so patterns become pictures.

## 🪜 Plain words

Take squared paper. Draw a line going right (the **x-axis**) and a line going up (the **y-axis**). They cross at the **origin**, the zero point. Any pair of numbers is now a spot: "go right this much, then up this much".

If you put a dot for every training step (step to the right, loss upwards), the dots form a curve. A curve going **down** to the right means the loss is falling: training works.

## 🪜 With numbers

The pair (3, 2) means: 3 to the right, 2 up. The pair (−1, 4): 1 to the **left** (negative), 4 up.

Loss log: step 0 → 2.5, step 100 → 1.8, step 200 → 1.4. As dots: (0, 2.5), (100, 1.8), (200, 1.4).

A **function's graph** is all the dots (x, f(x)). For f(x) = 2x: (0, 0), (1, 2), (2, 4), (3, 6): a straight line.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `(x, y)` | "the point x comma y" | x across, y up. **Order matters**: across first | `(x, y)` tuple |
| x-axis | "the x axis" | the horizontal line (inputs) | |
| y-axis | "the y axis" | the vertical line (outputs) | |
| `(0, 0)` | "the origin" | where the axes cross | |
| `y = f(x)` | "y equals f of x" | the y of each dot is f of its x | |

## 🔬 Take the formula apart

A point is on the graph of f exactly when:

<div class="formula"><span class="k1">y</span> = <span class="k2">f</span>(<span class="k3">x</span>)</div>

| Piece | Say it | Means | Point (3, 6) with f(x) = 2x |
|---|---|---|---|
| <span class="k1">y</span> | "y" | the point's height (second number) | 6 |
| <span class="k2">f</span> | "f" | the rule (function) | doubles |
| (<span class="k3">x</span>) | "of x" | the point's across position (first number) goes **into** f | f(3) = 6 |
| `=` | "equals" | the height must match what f gives | 6 = 6 ✓ on the graph |

## 🔀 What if the formula were different?

<div class="wrong"><b>Reading (3, 6) as "3 up, 6 across"</b>: you'd put the dot at (6, 3). For f(x) = 2x, f(6) = 12 ≠ 3, so you'd wrongly say the point isn't on the line.</div>
<div class="wrong"><b>x = f(y)</b> (swapped): you'd be drawing a different curve, the mirror image across the diagonal.</div>
<div class="right"><b>y = f(x)</b> with (across, up): (3, 6) is on the graph of 2x ✓</div>

## 🗣️ Say it out loud

"The point three comma six is on the graph of f, because f of three is six."

## 🤖 Where AI uses it

Loss curves (step, loss), learning-rate schedules, scaling-law plots, the ReLU and sigmoid shapes, and in Math 3, slopes of graphs tell training which way is downhill.

## 🎯 Your quest

1. `points(f, xs)`: return the list of `(x, f(x))` for each x.
2. `on_graph(f, point)`: `True` if `point[1]` equals `f(point[0])` (within `1e-9`).
3. `is_falling(points)`: `True` if every point's y is lower than the one before (points are in order of x).

**Remember:** (across, up). Always across first.

## Review

<details><summary>Write 0.00001 in Python's e-notation.</summary>1e-5.</details>
<details><summary>What is (−3)²?</summary>9.</details>
