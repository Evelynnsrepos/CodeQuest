---
title: Gradient descent: walking downhill
xp: 60
---
# Small steps against the gradient

> **Warm-up:** foggy hill again. You feel the slope, take a step downhill, feel again, step again. What could go wrong if your steps are giant? If they're tiny?

**In one sentence:** gradient descent repeats one move: new weights = old weights minus learning rate times gradient.

## 🪜 Plain words

1. Measure the gradient (which way is uphill).
2. Take a step the **other** way.
3. Make the step size = learning rate × steepness.
4. Repeat thousands of times.

The learning rate is the size of your stride. Too big: you leap over the valley and land higher on the other side, and it gets worse every step. Too small: you'll arrive next year.

## 🪜 With numbers

Loss L(w) = (w − 3)². The best w is 3. Start at w = 0, learning rate 0.1. The slope is 2(w − 3).

| step | w | slope 2(w − 3) | new w = w − 0.1 · slope | loss |
|---|---|---|---|---|
| 0 | 0 | −6 | 0 + 0.6 = 0.6 | 9 |
| 1 | 0.6 | −4.8 | 1.08 | 5.76 |
| 2 | 1.08 | −3.84 | 1.464 | 3.69 |

Each step closes 20% of the remaining gap. The loss shrinks steadily.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `θ` | "theta" | all the weights | `params` |
| `←` | "becomes" / "gets" | update: same as `=` in code (not "equals" in math!) | `w = w - lr * g` |
| `η` | "eta" (AY-tuh) | the learning rate (sometimes `α`, "alpha") | `lr` |
| `∇L(θ)` | "grad L at theta" | the uphill arrow at the current weights | `grads` |
| `θₜ` | "theta t" | the weights at step t | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">θ</span> ← <span class="k2">θ</span> <span class="k3">−</span> <span class="k4">η</span> · <span class="k5">∇L(θ)</span></div>

| Piece | Say it | Means | Step 0 above |
|---|---|---|---|
| <span class="k2">θ</span> (right side) | "theta" | where you are now | 0 |
| <span class="k5">∇L(θ)</span> | "grad L of theta" | uphill direction and steepness, here | −6 |
| <span class="k4">η</span> | "eta" | stride size | 0.1 |
| <span class="k3">−</span> | "minus" | go **against** uphill = downhill | |
| <span class="k1">θ</span> ← | "theta becomes" | the new position | 0 − 0.1 · (−6) = 0.6 |

## 🔀 What if it were different?

<div class="wrong"><b>Plus instead of minus</b>: w = 0 + 0.1 · (−6) = −0.6, loss 12.96 (was 9). Gradient <i>ascent</i>: every step makes the model worse.</div>
<div class="wrong"><b>η = 1.1 (too big)</b>: w = 0 + 1.1 · 6 = 6.6, loss 12.96. You overshoot the valley. Next step lands even further out: the loss explodes to inf/NaN.</div>
<div class="wrong"><b>η = 0.0001 (too small)</b>: w = 0.0006 after one step. Correct direction, but you'd need tens of thousands of steps to get close.</div>
<div class="right">θ ← θ − η∇L with η = 0.1: 0 → 0.6 → 1.08 → … → 3 ✓</div>

## 🗣️ Say it out loud

"Theta becomes theta minus eta times grad L of theta."

## 🤖 Where AI uses it

This **is** training. Every optimizer (SGD, Adam, Muon) is this line plus extras (Math 5). "Loss went NaN" in a run log almost always means η was too big for that moment, which is why runs use warmup (LLMs 8).

## 🎯 Your quest

1. `step(params, grads, lr)`: one update, returns a new list.
2. `minimize(grad_fn, start, lr, steps)`: repeat `step` using `grad_fn(params)` (which returns the gradient list); return the final params.
3. `fit_line(xs, ys, lr, steps)`: start at w = 0, b = 0 and use `grad_mse` (given) to fit a line; return `(w, b)`.

**Remember:** minus the gradient, times a sensible learning rate, many times.

## Review

<details><summary>Which way does ∇L point?</summary>Uphill: where the loss grows fastest.</details>
<details><summary>Why average the gradient over data points?</summary>So its size doesn't depend on how many points there are.</details>
