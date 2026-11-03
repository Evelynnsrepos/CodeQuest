---
title: Functions: f(x)
xp: 35
---
# A machine with an input slot

> **Warm-up:** you already write Python functions. What do you think `f(g(x))` means?

**In one sentence:** a math function is a rule that turns each input into exactly one output, just like a Python function with no side effects.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `f(x)` | "f of x" | the output of function f for input x | `f(x)` |
| `f(x) = x² + 1` | "f of x equals x squared plus one" | defines f | `def f(x): return x**2 + 1` |
| `f(g(x))` | "f of g of x" | **composition**: do g first, then f on the result | `f(g(x))` |
| `(f ∘ g)(x)` | "f after g of x" | the same composition, as one new function | `lambda x: f(g(x))` |
| `f: ℝ → ℝ` | "f maps reals to reals" | f takes a real number and gives a real number | type hints `float -> float` |
| `y = f(x)` | "y equals f of x" | y is the name for the output | `y = f(x)` |

## The idea

- `f(x)` is **not** "f times x". The brackets after a function name mean "feed in".
- Function names are usually single letters: `f`, `g`, `h`, `σ` (sigma, the sigmoid).
- **Composition** reads **inside-out**: in `f(g(x))`, the innermost thing (`g(x)`) happens first. Like nested Python calls.
- The arrow `ℝ → ℝ` describes input and output types. `ℝ` is the set of all real numbers (Math 1, lesson 12); `ℝⁿ` is a list of n real numbers. So `f: ℝⁿ → ℝ` takes a vector and returns one number (like a loss).

## 🗣️ Say it out loud

`y = σ(w·x + b)` → "y equals sigma of w times x plus b" → "compute w times x plus b, then put that through sigma."

## 🧮 Worked example

`f(x) = x²`, `g(x) = x + 3`, find `f(g(2))`:

1. Inside first: `g(2) = 2 + 3 = 5`
2. Then outside: `f(5) = 25`

The other order is different: `g(f(2)) = g(4) = 7`. Order matters!

## 🤖 Where AI uses it

A neural network **is** a composition: `output = layer₃(layer₂(layer₁(x)))`. The chain rule (Math 3) is how you take the derivative of such a composition, which is all of backpropagation.

## 🎯 Your quest

1. `compose(f, g)`: return a **new function** that computes `f(g(x))`.
2. `pipeline(fs, x)`: apply the functions in the list `fs` to `x` in order (first `fs[0]`, then `fs[1]`, …) and return the result.

**Remember:** read nested functions from the inside out.

## Review

<details><summary>Write 3e-4 as a decimal.</summary>0.0003.</details>
<details><summary>How big is a 7B model at 0.5 bytes per weight?</summary>3.5 GB.</details>
