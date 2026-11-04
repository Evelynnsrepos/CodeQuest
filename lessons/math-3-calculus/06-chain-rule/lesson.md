---
title: The chain rule: machines in a row
xp: 60
---
# Multiply the slopes along the chain

> **Warm-up:** gear A turns 3 times for each turn of gear B. Gear B turns 14 times for each turn of gear C. How many times does A turn for each turn of C?

**In one sentence:** when one function feeds into another, the overall slope is the **product** of each machine's slope, each measured at the point where it actually is.

## 🪜 Plain words

Answer to the warm-up: 3 × 14 = 42. Speeds along a chain **multiply**.

A neural network is machines in a row (Math 1 lesson 11): weights → layer → activation → loss. To find how a weight affects the loss, you multiply the slopes of every machine along the way. That's the **chain rule**, and **backpropagation** is just the chain rule done efficiently.

The one trap: each machine's slope must be measured **where that machine is working**, i.e. at its own input, not at the very first x.

## 🪜 With numbers

h(x) = (3x + 1)², at x = 2. Two machines: inner g(x) = 3x + 1, outer f(u) = u².

1. Run forward: g(2) = 7, f(7) = 49.
2. Inner slope: g'(x) = **3** (a line 3x + 1 always has slope 3).
3. Outer slope, **at u = 7**: f'(u) = 2u = **14**.
4. Multiply: 14 × 3 = **42**.

Check numerically: (3·2.00001 + 1)² − (3·1.99999 + 1)², divided by 0.00002 → 42.000 ✓.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f(g(x))` | "f of g of x" | g first, then f (Math 1) | `f(g(x))` |
| `g'(x)` | "g prime of x" | slope of the inner machine | |
| `f'(g(x))` | "f prime **at** g of x" | slope of the outer machine, measured at the inner's output | `df(g(x))` |
| `·` | "times" | multiply | `*` |
| `dy/dx = dy/du · du/dx` | "d y d x equals d y d u times d u d x" | the same rule in d-notation | |

## 🔬 Take the formula apart

<div class="formula">( <span class="k1">f</span>( <span class="k2">g(x)</span> ) )' = <span class="k3">f'</span>( <span class="k2">g(x)</span> ) · <span class="k4">g'(x)</span></div>

| Piece | Say it | Means | (3x + 1)² at x = 2 |
|---|---|---|---|
| <span class="k2">g(x)</span> | "g of x" | the inner machine's output | 7 |
| <span class="k1">f</span>( … ) | "f of" | the outer machine | u² → 49 |
| <span class="k3">f'</span>( <span class="k2">g(x)</span> ) | "f prime at g of x" | outer slope, measured **at 7** | 2 · 7 = 14 |
| <span class="k4">g'(x)</span> | "g prime of x" | inner slope | 3 |
| · | "times" | multiply them | 14 · 3 = 42 |

## 🔀 What if it were different?

<div class="wrong"><b>f'(x) · g'(x)</b> (outer slope at x instead of at g(x)): 2·2 · 3 = 12 instead of 42. The outer machine never sees 2, it sees 7.</div>
<div class="wrong"><b>Forget g'(x)</b>: just 14. Ignores that the inner machine triples every nudge.</div>
<div class="wrong"><b>f'(g(x)) + g'(x)</b> (adding instead of multiplying): 17. Gears multiply, they don't add.</div>
<div class="right">f'(g(x)) · g'(x) = 14 · 3 = 42 ✓</div>

## 🗣️ Say it out loud

"The derivative of f of g of x is f prime at g of x, times g prime of x." Short version: "outside slope times inside slope."

## 🤖 Where AI uses it

**Backpropagation.** For a 100-layer network, the slope of the loss with respect to a weight in layer 1 is a product of ~100 local slopes. If they're mostly below 1 the product vanishes; above 1 it explodes. Residual connections (LLMs 8) fix this by adding a "+1" path through every layer.

## 🎯 Your quest

`sigmoid` is given.

1. `d_square_of_linear(a, b, x)`: slope of (ax + b)² at x.
2. `d_sigmoid_of_linear(w, b, x)`: slope of σ(wx + b) with respect to x.
3. `chain(slopes)`: multiply a list of local slopes together (empty list → 1).

**Remember:** outside slope (at the inside's value) times inside slope.

## Review

<details><summary>σ'(x)?</summary>σ(x) · (1 − σ(x)).</details>
<details><summary>Why is a flat sigmoid a problem?</summary>Its slope is near 0, so almost no learning signal passes through (vanishing gradients).</details>
