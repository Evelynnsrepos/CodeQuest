---
title: Δ: how much something changed
xp: 35
---
# Before and after

> **Warm-up:** your training loss was 2.5 at step 100 and 1.9 at step 400. Is training going well? How fast is the loss falling?

**In one sentence:** `Δ` ("delta") means "how much it changed", and change divided by change tells you how fast something is changing.

## 🪜 Plain words

Calculus is the math of **change**. Everything starts with two simple questions:

1. How much did it change? (after minus before)
2. How fast did it change? (how much it changed, divided by how long it took)

That second one is a speed. A car that drove 120 km in 2 hours went 60 km **per** hour. A loss that dropped 0.6 in 300 steps dropped 0.002 **per** step.

## 🪜 With numbers

- Loss before: 2.5. Loss after: 1.9. Change: 1.9 − 2.5 = **−0.6** (negative = it went down, good!).
- Steps before: 100. Steps after: 400. Change: 400 − 100 = **300**.
- Speed: −0.6 ÷ 300 = **−0.002 per step**.

Always **after minus before**. That way "went down" comes out negative and "went up" comes out positive.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Δ` | "delta" | "the change in" (Greek capital D, for **D**ifference) | `after - before` |
| `Δy` | "delta y" | how much y changed | `y2 - y1` |
| `Δx` | "delta x" | how much x changed | `x2 - x1` |
| `f(a)` | "f of a" | the output of f when a goes in (Math 1) | `f(a)` |
| `/` or a fraction bar | "divided by" / "over" | share out | `/` |

## 🔬 Take the formula apart

<div class="formula">average rate = ( <span class="k1">f(b)</span> − <span class="k2">f(a)</span> ) / ( <span class="k3">b</span> − <span class="k4">a</span> ) = <span class="k5">Δy</span> / <span class="k6">Δx</span></div>

| Piece | Say it | Means | Loss example |
|---|---|---|---|
| <span class="k4">a</span> | "a" | the **start** point (input) | step 100 |
| <span class="k3">b</span> | "b" | the **end** point (input) | step 400 |
| <span class="k2">f(a)</span> | "f of a" | value at the start | 2.5 |
| <span class="k1">f(b)</span> | "f of b" | value at the end | 1.9 |
| <span class="k5">Δy</span> = <span class="k1">f(b)</span> − <span class="k2">f(a)</span> | "delta y" | how much the **output** changed | −0.6 |
| <span class="k6">Δx</span> = <span class="k3">b</span> − <span class="k4">a</span> | "delta x" | how much the **input** changed | 300 |
| <span class="k5">Δy</span> / <span class="k6">Δx</span> | "delta y over delta x" | change **per** one step of input | −0.002 |

This is the same as the **slope** from Math 1 lesson 10: rise over run.

## 🔀 What if the formula were different?

<div class="wrong"><b>( f(a) − f(b) ) / ( b − a )</b> (before minus after on top): 0.6 / 300 = <b>+0.002</b>. It says the loss is <i>rising</i>. You'd stop a training run that was actually going well.</div>
<div class="wrong"><b>( f(b) − f(a) ) / b</b> (dividing by the end point instead of the change): −0.6 / 400 = −0.0015. Too slow by a quarter; the answer would change just by where you started counting.</div>
<div class="wrong"><b>f(b) − f(a)</b> only (no dividing): −0.6. Is that fast? Over 10 steps it's amazing, over 1 million steps it's nothing. Without "per", you can't compare.</div>
<div class="right"><b>( f(b) − f(a) ) / ( b − a )</b> = −0.002 per step ✓</div>

## 🗣️ Say it out loud

`Δy / Δx` → "delta y over delta x" → "how much y changed for each 1 that x changed."

## 🤖 Where AI uses it

Reading training curves ("is loss still falling?"), tokens per second, learning-rate schedules. And it's the first step toward the **derivative** (lesson 03), the thing that makes training possible.

## 🎯 Your quest

1. `delta(before, after)`: the change.
2. `avg_rate(f, a, b)`: average rate of change of function `f` from `a` to `b`.
3. `deltas(values)`: list of changes between each value and the next one (`[2, 5, 4]` → `[3, -1]`).

**Remember:** Δ = after minus before; rate = Δy ÷ Δx.

## Review

<details><summary>What does Σ mean?</summary>Add up a list of things (a for loop with a running total).</details>
<details><summary>Slope from (1, 5) to (2, 7)?</summary>(7 − 5) / (2 − 1) = 2.</details>
