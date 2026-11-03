---
title: Derivatives as slope
xp: 35
---
# Which way is downhill?

> **Warm-up:** you're standing on a hillside in thick fog and want to get down. You can only feel the ground right under your feet. What do you do?

You feel which way the ground slopes and step that way. Training does exactly that, and the slope is the **derivative**.

The derivative `f'(x)` is how fast `f` changes when `x` changes a tiny bit:

```
f'(x) ≈ (f(x + h) − f(x − h)) / (2h)       for a tiny h, like 0.00001
```

This **central difference** is a numerical estimate. It's how you *check* derivatives in practice (gradient checking), but it's far too slow to train with: one model has billions of weights.

Calculus gives exact formulas instead. The ones you need most:

| f(x) | f'(x) |
|---|---|
| `c` (a constant) | `0` |
| `xⁿ` | `n·xⁿ⁻¹` (so `x²` → `2x`) |
| `eˣ` | `eˣ` |
| `ln x` | `1/x` |
| `a·f(x) + b·g(x)` | `a·f'(x) + b·g'(x)` |
| `f(x)·g(x)` | `f'(x)·g(x) + f(x)·g'(x)` (product rule) |

Reading a derivative: `f'(x) > 0` means "increasing `x` increases `f`", so to make `f` *smaller* you move `x` the other way. `f'(x) = 0` means flat: a minimum, maximum or saddle.

Watch 3Blue1Brown's *Essence of Calculus*, chapters 1–4, alongside this.

## Your quest

1. `numeric_derivative(f, x)`: the central difference with `h = 1e-5`.
2. `df(x)`: the **exact** derivative of `f(x) = 3x² − 4x + 7`, using the rules above.
3. `minimum_x`: set it to the `x` where `f` is smallest (where `df(x) = 0`). Solve it by hand.

The program compares your exact derivative with the numerical one.

## Review

<details><summary>Roughly how many FLOPs does training take?</summary>About 6 × parameters × training tokens.</details>
<details><summary>What does the Chinchilla rule say?</summary>For a fixed compute budget, the best model uses about 20 training tokens per parameter.</details>
