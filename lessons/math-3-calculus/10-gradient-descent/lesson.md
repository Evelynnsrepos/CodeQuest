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


<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="The loss bowl (w − 3) squared with gradient-descent steps from w = 0 moving toward the bottom at w = 3"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="204.0" x2="392" y2="204.0" stroke="currentColor" opacity=".45"/><line x1="60.9" y1="28" x2="60.9" y2="210" stroke="currentColor" opacity=".45"/><text x="60.9" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">0</text><text x="110.6" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">1</text><text x="160.3" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">2</text><text x="210.0" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">3</text><text x="259.7" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">4</text><text x="309.4" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">5</text><text x="359.1" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">6</text><text x="54.9" y="160.0" font-size="11" fill="currentColor" text-anchor="end">3</text><text x="54.9" y="112.0" font-size="11" fill="currentColor" text-anchor="end">6</text><text x="54.9" y="64.0" font-size="11" fill="currentColor" text-anchor="end">9</text><text x="396.0" y="208.0" font-size="12" fill="currentColor" text-anchor="start">w</text><text x="66.9" y="24.0" font-size="12" fill="currentColor" text-anchor="start">loss</text><polyline points="45.9,29.8 48.7,35.5 51.4,41.2 54.1,46.7 56.9,52.2 59.6,57.6 62.3,62.9 65.1,68.0 67.8,73.1 70.6,78.1 73.3,83.0 76.0,87.8 78.8,92.5 81.5,97.1 84.2,101.6 87.0,106.0 89.7,110.3 92.4,114.5 95.2,118.6 97.9,122.6 100.6,126.6 103.4,130.4 106.1,134.1 108.8,137.7 111.6,141.3 114.3,144.7 117.0,148.0 119.8,151.3 122.5,154.4 125.2,157.5 128.0,160.4 130.7,163.3 133.4,166.1 136.2,168.7 138.9,171.3 141.6,173.8 144.4,176.1 147.1,178.4 149.8,180.6 152.6,182.7 155.3,184.6 158.0,186.5 160.8,188.3 163.5,190.0 166.3,191.6 169.0,193.1 171.7,194.5 174.5,195.8 177.2,197.0 179.9,198.1 182.7,199.2 185.4,200.1 188.1,200.9 190.9,201.6 193.6,202.3 196.3,202.8 199.1,203.2 201.8,203.6 204.5,203.8 207.3,204.0 210.0,204.0 212.7,204.0 215.5,203.8 218.2,203.6 220.9,203.2 223.7,202.8 226.4,202.3 229.1,201.6 231.9,200.9 234.6,200.1 237.3,199.2 240.1,198.1 242.8,197.0 245.5,195.8 248.3,194.5 251.0,193.1 253.7,191.6 256.5,190.0 259.2,188.3 262.0,186.5 264.7,184.6 267.4,182.7 270.2,180.6 272.9,178.4 275.6,176.1 278.4,173.8 281.1,171.3 283.8,168.7 286.6,166.1 289.3,163.3 292.0,160.4 294.8,157.5 297.5,154.4 300.2,151.3 303.0,148.0 305.7,144.7 308.4,141.3 311.2,137.7 313.9,134.1 316.6,130.4 319.4,126.6 322.1,122.6 324.8,118.6 327.6,114.5 330.3,110.3 333.0,106.0 335.8,101.6 338.5,97.1 341.2,92.5 344.0,87.8 346.7,83.0 349.4,78.1 352.2,73.1 354.9,68.0 357.7,62.9 360.4,57.6 363.1,52.2 365.9,46.7 368.6,41.2 371.3,35.5 374.1,29.8" fill="none" stroke="#6c4cf5" stroke-width="2.5" stroke-linejoin="round"/><circle cx="60.9" cy="60.0" r="4" fill="#e5484d"/><line x1="60.9" y1="60.0" x2="90.7" y2="111.8" stroke="#e5484d" stroke-width="1.5" stroke-linecap="round"/><circle cx="90.7" cy="111.8" r="4" fill="#e5484d"/><line x1="90.7" y1="111.8" x2="114.5" y2="145.0" stroke="#e5484d" stroke-width="1.5" stroke-linecap="round"/><circle cx="114.5" cy="145.0" r="4" fill="#e5484d"/><line x1="114.5" y1="145.0" x2="133.6" y2="166.3" stroke="#e5484d" stroke-width="1.5" stroke-linecap="round"/><circle cx="133.6" cy="166.3" r="4" fill="#e5484d"/><line x1="133.6" y1="166.3" x2="148.9" y2="179.8" stroke="#e5484d" stroke-width="1.5" stroke-linecap="round"/><circle cx="148.9" cy="179.8" r="4" fill="#e5484d"/><line x1="148.9" y1="179.8" x2="161.1" y2="188.5" stroke="#e5484d" stroke-width="1.5" stroke-linecap="round"/><circle cx="161.1" cy="188.5" r="4" fill="#e5484d"/><line x1="161.1" y1="188.5" x2="170.9" y2="194.1" stroke="#e5484d" stroke-width="1.5" stroke-linecap="round"/><circle cx="210.0" cy="204.0" r="5" fill="#30a46c"/><text x="210.0" y="189.6" font-size="13" fill="#30a46c" text-anchor="middle">best w = 3</text><text x="68.3" y="50.4" font-size="13" fill="#e5484d" text-anchor="start">start</text></svg>

<div class="explore" data-widget="gradient-descent"></div>

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
