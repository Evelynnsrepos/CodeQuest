---
title: Curvature and the biggest safe learning rate
xp: 55
---
# Why a learning rate can be "too big"

> **Warm-up:** in Math 3 lesson 10, learning rate 0.1 worked and 1.1 blew up on the loss (w − 3)². Where exactly is the border, and why?

**In one sentence:** the second derivative measures how sharply a loss curves, and gradient descent on a bowl is only stable when learning rate < 2 ÷ curvature.

## 🪜 Plain words

- The first derivative is the **slope** (Math 3).
- The **second derivative** is how fast the slope itself changes: the **curvature**. A narrow, steep valley has big curvature; a wide, gentle one has small curvature.
- A loss shaped like a bowl everywhere (curvature never negative) is **convex**: it has one bottom and no traps.

Each gradient step jumps by learning rate × slope. In a sharp valley the slope grows fast as you move, so a big step flies past the bottom and lands higher on the other side. The border is **2 ÷ curvature**: exactly at it, you bounce back and forth forever; above it, each bounce gets bigger.

## 🪜 With numbers

L(w) = (w − 3)². Slope 2(w − 3). Curvature **2** everywhere. Safe if η < 2/2 = **1**.

| η | first steps from w = 0 | result |
|---|---|---|
| 0.1 | 0.6, 1.08, 1.46… | slowly to 3 ✓ |
| 0.5 | 3 | lands exactly on the bottom in one step |
| 1.0 | 6, 0, 6, 0… | bounces forever |
| 1.1 | 6.6, −1.32, 8.18… | explodes |


<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="The bowl (w − 3) squared: small steps creep to the bottom, η = 1 bounces between 0 and 6, η = 1.1 flies out"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="204.0" x2="392" y2="204.0" stroke="currentColor" opacity=".45"/><line x1="105.6" y1="28" x2="105.6" y2="210" stroke="currentColor" opacity=".45"/><text x="105.6" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">0</text><text x="210.0" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">3</text><text x="314.4" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">6</text><text x="99.6" y="149.8" font-size="11" fill="currentColor" text-anchor="end">9</text><text x="396.0" y="208.0" font-size="12" fill="currentColor" text-anchor="start">w</text><text x="111.6" y="24.0" font-size="12" fill="currentColor" text-anchor="start">loss</text><polyline points="36.0,42.5 38.9,47.8 41.8,53.1 44.7,58.2 47.6,63.3 50.5,68.3 53.4,73.2 56.3,78.0 59.2,82.7 62.1,87.3 65.0,91.8 67.9,96.3 70.8,100.6 73.7,104.9 76.6,109.1 79.5,113.1 82.4,117.1 85.3,121.0 88.2,124.8 91.1,128.6 94.0,132.2 96.9,135.8 99.8,139.2 102.7,142.6 105.6,145.8 108.5,149.0 111.4,152.1 114.3,155.1 117.2,158.1 120.1,160.9 123.0,163.6 125.9,166.3 128.8,168.8 131.7,171.3 134.6,173.7 137.5,176.0 140.4,178.2 143.3,180.3 146.2,182.3 149.1,184.2 152.0,186.1 154.9,187.8 157.8,189.5 160.7,191.0 163.6,192.5 166.5,193.9 169.4,195.2 172.3,196.4 175.2,197.5 178.1,198.6 181.0,199.5 183.9,200.4 186.8,201.1 189.7,201.8 192.6,202.4 195.5,202.9 198.4,203.3 201.3,203.6 204.2,203.8 207.1,204.0 210.0,204.0 212.9,204.0 215.8,203.8 218.7,203.6 221.6,203.3 224.5,202.9 227.4,202.4 230.3,201.8 233.2,201.1 236.1,200.4 239.0,199.5 241.9,198.6 244.8,197.5 247.7,196.4 250.6,195.2 253.5,193.9 256.4,192.5 259.3,191.0 262.2,189.5 265.1,187.8 268.0,186.1 270.9,184.2 273.8,182.3 276.7,180.3 279.6,178.2 282.5,176.0 285.4,173.7 288.3,171.3 291.2,168.8 294.1,166.3 297.0,163.6 299.9,160.9 302.8,158.1 305.7,155.1 308.6,152.1 311.5,149.0 314.4,145.8 317.3,142.6 320.2,139.2 323.1,135.8 326.0,132.2 328.9,128.6 331.8,124.8 334.7,121.0 337.6,117.1 340.5,113.1 343.4,109.1 346.3,104.9 349.2,100.6 352.1,96.3 355.0,91.8 357.9,87.3 360.8,82.7 363.7,78.0 366.6,73.2 369.5,68.3 372.4,63.3 375.3,58.2 378.2,53.1 381.1,47.8 384.0,42.5" fill="none" stroke="#6c4cf5" stroke-width="2.5" stroke-linejoin="round"/><line x1="105.6" y1="145.8" x2="314.4" y2="145.8" stroke="#d97706" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ahd97706)" stroke-linecap="round"/><line x1="314.4" y1="145.8" x2="105.6" y2="145.8" stroke="#d97706" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ahd97706)" stroke-linecap="round"/><text x="210.0" y="161.4" font-size="13" fill="#d97706" text-anchor="middle">η = 1: bounces 0 ↔ 6</text><line x1="105.6" y1="145.8" x2="335.3" y2="120.3" stroke="#e5484d" stroke-width="2" marker-end="url(#ahe5484d)" stroke-linecap="round"/><line x1="335.3" y1="120.3" x2="59.7" y2="83.4" stroke="#e5484d" stroke-width="2" marker-end="url(#ahe5484d)" stroke-linecap="round"/><text x="70.8" y="68.3" font-size="13" fill="#e5484d" text-anchor="start">η = 1.1: explodes</text><line x1="105.6" y1="145.8" x2="126.5" y2="166.8" stroke="#30a46c" stroke-width="2" marker-end="url(#ah30a46c)" stroke-linecap="round"/><line x1="126.5" y1="166.8" x2="143.2" y2="180.2" stroke="#30a46c" stroke-width="2" marker-end="url(#ah30a46c)" stroke-linecap="round"/><line x1="143.2" y1="180.2" x2="156.5" y2="188.8" stroke="#30a46c" stroke-width="2" marker-end="url(#ah30a46c)" stroke-linecap="round"/><line x1="156.5" y1="188.8" x2="167.2" y2="194.2" stroke="#30a46c" stroke-width="2" marker-end="url(#ah30a46c)" stroke-linecap="round"/><text x="265.7" y="187.8" font-size="13" fill="#30a46c" text-anchor="start">η = 0.1 ✓</text></svg>

<div class="quiz" data-answer="1" data-why="The slope at 0 is 2·(0 − 3) = −6, so w = 0 − 0.5 × (−6) = 3: the bottom in one step. Try other η below."><p><b>Predict first:</b> L(w) = (w − 3)², η = 0.5, start at w = 0. Where is w after one step?</p><button>1.5</button><button>3</button><button>6</button></div>

<div class="explore" data-widget="gradient-descent"></div>

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f''(x)` | "f double prime of x" | second derivative: the slope of the slope | `second_derivative(f, x)` |
| `d²f/dx²` | "d two f, d x squared" | same thing | |
| `η` | "eta" | learning rate (Math 3) | `lr` |
| `<` | "less than" | | `<` |
| convex | | bowl-shaped: f'' ≥ 0 everywhere | |
| `H` | "the Hessian" | all second derivatives of a many-input function (a matrix) | |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">f''(x)</span> ≈ ( <span class="k2">f(x + h)</span> − <span class="k3">2 f(x)</span> + <span class="k4">f(x − h)</span> ) / <span class="k5">h²</span></div>

| Piece | Say it | Means | (w − 3)² at w = 0, h = 1 |
|---|---|---|---|
| <span class="k2">f(x + h)</span> | "f of x plus h" | one step right | 4 |
| <span class="k3">2 f(x)</span> | "two f of x" | twice the middle | 18 |
| <span class="k4">f(x − h)</span> | "f of x minus h" | one step left | 16 |
| / <span class="k5">h²</span> | "over h squared" | per step, squared (two derivatives deep) | (4 − 18 + 16)/1 = 2 |

<div class="formula"><span class="k6">η</span> &lt; 2 / <span class="k1">curvature</span></div>

## 🔀 What if it were different?

<div class="wrong"><b>η &lt; 1 / curvature as the limit</b>: too cautious by half. Safe, but up to 2× slower than needed.</div>
<div class="wrong"><b>η &lt; 2 / slope</b> (first derivative): the slope is 0 at the bottom, so the "limit" would be infinite exactly where overshooting happens.</div>
<div class="wrong"><b>Second difference with + 2f(x)</b>: (4 + 18 + 16)/1 = 38. Nonsense curvature.</div>
<div class="right">curvature 2 → η must be below 1 ✓</div>

## 🗣️ Say it out loud

"f double prime of x is about f of x plus h, minus two f of x, plus f of x minus h, all over h squared."

## 🤖 Where AI uses it

Neural network losses are **not** convex, but near a good point they look like bowls with very different curvatures in different directions. The sharpest direction sets the safe learning rate: that's why warmup and learning-rate schedules exist (LLMs 8), and why Adam (lesson 10) rescales each weight separately.

## 🎯 Your quest

1. `second_derivative(f, x, h=1e-4)`.
2. `max_stable_lr(curvature)`: 2 / curvature.
3. `is_convex(f, xs)`: `True` if the second derivative is ≥ −1e-6 at every x in `xs`.

**Remember:** sharper bowl → smaller safe steps; limit 2 ÷ curvature.

## Review

<details><summary>Gradient of softmax + cross-entropy?</summary>p − y.</details>
<details><summary>Sum of that gradient's entries?</summary>0.</details>
