---
title: ∫: integrals as area
xp: 50
---
# Adding up infinitely thin strips

> **Warm-up:** you drive at 60 km/h for 2 hours. How far did you go? Now draw speed (up) against time (across). What shape is under the line, and what's its area?

**In one sentence:** the integral `∫` adds up a quantity over a range; on a graph it's the area under the curve, and you can get it by summing thin rectangles.

## 🪜 Plain words

Warm-up: 60 × 2 = 120 km. On the graph, that's a rectangle 2 wide and 60 tall: area 120. **Area under a speed curve = distance.**

If the speed changes, the shape isn't a rectangle. Trick: slice it into thin strips, treat each strip as a rectangle (height = curve value in the middle of the strip), and add them up. Thinner strips → closer to the true area. The limit of infinitely thin strips is the **integral**.

The integral is the **opposite** of the derivative: derivative = rate from amount, integral = amount from rate.

## 🪜 With numbers

f(x) = 2x from 0 to 3 (a triangle: ½ · 3 · 6 = **9**).

- 3 strips, width 1, middles at 0.5, 1.5, 2.5: heights 1, 3, 5. Sum: (1 + 3 + 5) · 1 = **9** ✓

f(x) = x² from 0 to 1 (true area **1/3 ≈ 0.333**):

- 2 strips of width 0.5, middles 0.25 and 0.75: (0.0625 + 0.5625) · 0.5 = 0.3125
- 1000 strips: 0.33333 ✓


<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="Area under y = 2x from 0 to 3, filled with three midpoint strips of heights 1, 3 and 5"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="204.0" x2="392" y2="204.0" stroke="currentColor" opacity=".45"/><line x1="36.0" y1="28" x2="36.0" y2="210" stroke="currentColor" opacity=".45"/><text x="138.4" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">1</text><text x="240.7" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">2</text><text x="343.1" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">3</text><text x="30.0" y="160.0" font-size="11" fill="currentColor" text-anchor="end">2</text><text x="30.0" y="112.0" font-size="11" fill="currentColor" text-anchor="end">4</text><text x="30.0" y="64.0" font-size="11" fill="currentColor" text-anchor="end">6</text><text x="396.0" y="208.0" font-size="12" fill="currentColor" text-anchor="start">x</text><text x="42.0" y="24.0" font-size="12" fill="currentColor" text-anchor="start">y</text><polygon points="36.0,204.0 36.0,204.0 39.8,202.2 43.7,200.4 47.5,198.6 51.4,196.8 55.2,195.0 59.0,193.2 62.9,191.4 66.7,189.6 70.5,187.8 74.4,186.0 78.2,184.2 82.1,182.4 85.9,180.6 89.7,178.8 93.6,177.0 97.4,175.2 101.2,173.4 105.1,171.6 108.9,169.8 112.8,168.0 116.6,166.2 120.4,164.4 124.3,162.6 128.1,160.8 132.0,159.0 135.8,157.2 139.6,155.4 143.5,153.6 147.3,151.8 151.1,150.0 155.0,148.2 158.8,146.4 162.7,144.6 166.5,142.8 170.3,141.0 174.2,139.2 178.0,137.4 181.9,135.6 185.7,133.8 189.5,132.0 193.4,130.2 197.2,128.4 201.0,126.6 204.9,124.8 208.7,123.0 212.6,121.2 216.4,119.4 220.2,117.6 224.1,115.8 227.9,114.0 231.8,112.2 235.6,110.4 239.4,108.6 243.3,106.8 247.1,105.0 250.9,103.2 254.8,101.4 258.6,99.6 262.5,97.8 266.3,96.0 270.1,94.2 274.0,92.4 277.8,90.6 281.6,88.8 285.5,87.0 289.3,85.2 293.2,83.4 297.0,81.6 300.8,79.8 304.7,78.0 308.5,76.2 312.4,74.4 316.2,72.6 320.0,70.8 323.9,69.0 327.7,67.2 331.5,65.4 335.4,63.6 339.2,61.8 343.1,60.0 343.1,204.0" fill="#6c4cf5" fill-opacity="0.12"/><rect x="36.0" y="180.0" width="102.4" height="24.0" fill="#d97706" fill-opacity="0.3" stroke="#d97706" stroke-width="1"/><text x="87.2" y="174.0" font-size="13" fill="#d97706" text-anchor="middle">1</text><rect x="138.4" y="132.0" width="102.4" height="72.0" fill="#d97706" fill-opacity="0.3" stroke="#d97706" stroke-width="1"/><text x="189.5" y="126.0" font-size="13" fill="#d97706" text-anchor="middle">3</text><rect x="240.7" y="84.0" width="102.4" height="120.0" fill="#d97706" fill-opacity="0.3" stroke="#d97706" stroke-width="1"/><text x="291.9" y="78.0" font-size="13" fill="#d97706" text-anchor="middle">5</text><polyline points="36.0,204.0 38.8,202.7 41.6,201.4 44.4,200.0 47.3,198.7 50.1,197.4 52.9,196.1 55.7,194.8 58.5,193.4 61.3,192.1 64.1,190.8 67.0,189.5 69.8,188.2 72.6,186.8 75.4,185.5 78.2,184.2 81.0,182.9 83.8,181.6 86.7,180.2 89.5,178.9 92.3,177.6 95.1,176.3 97.9,175.0 100.7,173.6 103.6,172.3 106.4,171.0 109.2,169.7 112.0,168.4 114.8,167.0 117.6,165.7 120.4,164.4 123.3,163.1 126.1,161.8 128.9,160.4 131.7,159.1 134.5,157.8 137.3,156.5 140.1,155.2 143.0,153.8 145.8,152.5 148.6,151.2 151.4,149.9 154.2,148.6 157.0,147.2 159.8,145.9 162.7,144.6 165.5,143.3 168.3,142.0 171.1,140.6 173.9,139.3 176.7,138.0 179.5,136.7 182.4,135.4 185.2,134.0 188.0,132.7 190.8,131.4 193.6,130.1 196.4,128.8 199.3,127.4 202.1,126.1 204.9,124.8 207.7,123.5 210.5,122.2 213.3,120.8 216.1,119.5 219.0,118.2 221.8,116.9 224.6,115.6 227.4,114.2 230.2,112.9 233.0,111.6 235.8,110.3 238.7,109.0 241.5,107.6 244.3,106.3 247.1,105.0 249.9,103.7 252.7,102.4 255.5,101.0 258.4,99.7 261.2,98.4 264.0,97.1 266.8,95.8 269.6,94.4 272.4,93.1 275.2,91.8 278.1,90.5 280.9,89.2 283.7,87.8 286.5,86.5 289.3,85.2 292.1,83.9 295.0,82.6 297.8,81.2 300.6,79.9 303.4,78.6 306.2,77.3 309.0,76.0 311.8,74.6 314.7,73.3 317.5,72.0 320.3,70.7 323.1,69.4 325.9,68.0 328.7,66.7 331.5,65.4 334.4,64.1 337.2,62.8 340.0,61.4 342.8,60.1 345.6,58.8 348.4,57.5 351.2,56.2 354.1,54.8 356.9,53.5 359.7,52.2 362.5,50.9 365.3,49.6 368.1,48.2 370.9,46.9 373.8,45.6" fill="none" stroke="#6c4cf5" stroke-width="2.5" stroke-linejoin="round"/><text x="158.8" y="69.6" font-size="13" fill="#6c4cf5" text-anchor="middle">area = 9</text></svg>

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `∫` | "the integral" | a stretched S, for **S**um | a loop that adds |
| `∫ₐᵇ` | "integral from a to b" | add up from a to b (small numbers bottom and top) | `range` from a to b |
| `f(x)` | "f of x" | the height of the curve | `f(x)` |
| `dx` | "d x" | the (infinitely thin) strip width: says "x is the thing we slice along" | `width = (b - a) / n` |
| `Δx` | "delta x" | a real, non-tiny strip width | `width` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">∫</span><sub><span class="k2">a</span></sub><sup><span class="k3">b</span></sup> <span class="k4">f(x)</span> <span class="k5">dx</span> ≈ <span class="k1">Σ</span> <span class="k4">f(middleᵢ)</span> · <span class="k5">Δx</span></div>

| Piece | Say it | Means | 2x from 0 to 3, 3 strips |
|---|---|---|---|
| <span class="k1">∫</span> / <span class="k1">Σ</span> | "integral" / "sum" | add up the strips | |
| <span class="k2">a</span> | "from a" | start | 0 |
| <span class="k3">b</span> | "to b" | end | 3 |
| <span class="k4">f(x)</span> | "f of x" | strip height | 1, 3, 5 |
| <span class="k5">dx</span> / <span class="k5">Δx</span> | "d x" / "delta x" | strip width = (b − a) / n | 1 |
| total | | area | 9 |

## 🔀 What if it were different?

<div class="wrong"><b>Swap a and b</b> (∫ from 3 to 0): −9. Going backwards flips the sign.</div>
<div class="wrong"><b>Forget the width</b> (just add heights): with 6 strips of width 0.5 the heights add to 18. That counts each strip as 1 wide: double the true area.</div>
<div class="wrong"><b>Use left edges with 2 strips on x²</b>: (0 + 0.25) · 0.5 = 0.125 instead of ~0.333. Bad heights make a coarse sum badly wrong; middles are much better.</div>
<div class="right">Σ f(middle) · Δx → 9 for 2x, → 0.3333 for x² ✓</div>

## 🗣️ Say it out loud

`∫₀³ 2x dx = 9` → "the integral from 0 to 3 of 2x d x is 9."

## 🤖 Where AI uses it

**Probability** (Math 4): for continuous values, the probability of landing between a and b is the area under the density curve, and the total area must be 1. **AUC** (area under the ROC curve) scores classifiers: 1.0 perfect, 0.5 coin flip. Diffusion models (AI beyond LLMs) integrate a noise process over time.

## 🎯 Your quest

1. `riemann(f, a, b, n)`: midpoint sum with `n` strips.
2. `prob_between(density, a, b)`: `riemann(density, a, b, 1000)`.
3. `auc(points)`: area under a polyline given as sorted `(x, y)` points, using trapezoids: each piece is `(x₂ − x₁) · (y₁ + y₂) / 2`.

**Remember:** ∫ = sum of height × width, over thinner and thinner strips.

## Review

<details><summary>Backprop in five words?</summary>Forward and remember, backward multiply.</details>
<details><summary>∂a/∂z for a sigmoid?</summary>a(1 − a).</details>
