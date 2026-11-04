---
title: The derivative: speed at one instant
xp: 50
---
# Zoom in until it's a straight line

> **Warm-up:** a speedometer shows your speed **right now**, not your average over the trip. How could you measure "right now" speed with only a stopwatch and distance markers?

**In one sentence:** the derivative is the slope of a curve at a single point: the average rate of change over a step that shrinks to zero.

## 🪜 Plain words

In lesson 01 we measured average speed between two moments. To get speed **at one moment**, make the two moments closer and closer together. 1 second apart, 0.1 seconds, 0.01... The answers settle on one number (a limit, lesson 02). That number is the **derivative**.

Picture it: zoom into a curve far enough and it looks like a straight line. The derivative is that line's slope. It answers: **"If I nudge the input a tiny bit, how much does the output move, and in which direction?"**

## 🪜 With numbers

f(x) = x² at x = 3 (so f(3) = 9). Take a step h and measure the slope:

| step h | f(3 + h) | change ÷ h |
|---|---|---|
| 1 | 16 | (16 − 9) / 1 = 7 |
| 0.1 | 9.61 | 0.61 / 0.1 = 6.1 |
| 0.01 | 9.0601 | 0.0601 / 0.01 = 6.01 |
| 0.001 | 9.006001 | 6.001 |

Heading to **6**. So the slope of x² at x = 3 is 6: nudge x up by a tiny bit, the output goes up about 6 times that bit.


<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="The curve y = x squared with its tangent line at x = 3, slope 6"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="204.0" x2="392" y2="204.0" stroke="currentColor" opacity=".45"/><line x1="36.0" y1="28" x2="36.0" y2="210" stroke="currentColor" opacity=".45"/><text x="113.3" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">1</text><text x="190.7" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">2</text><text x="268.0" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">3</text><text x="345.3" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">4</text><text x="30.0" y="166.0" font-size="11" fill="currentColor" text-anchor="end">4</text><text x="30.0" y="113.5" font-size="11" fill="currentColor" text-anchor="end">9</text><text x="30.0" y="40.0" font-size="11" fill="currentColor" text-anchor="end">16</text><text x="396.0" y="208.0" font-size="12" fill="currentColor" text-anchor="start">x</text><text x="42.0" y="24.0" font-size="12" fill="currentColor" text-anchor="start">y</text><polyline points="36.0,204.0 38.6,204.0 41.3,204.0 43.9,203.9 46.6,203.8 49.2,203.7 51.9,203.6 54.5,203.4 57.1,203.2 59.8,203.0 62.4,202.8 65.1,202.5 67.7,202.2 70.3,201.9 73.0,201.6 75.6,201.2 78.3,200.9 80.9,200.5 83.6,200.0 86.2,199.6 88.8,199.1 91.5,198.6 94.1,198.1 96.8,197.5 99.4,196.9 102.1,196.3 104.7,195.7 107.3,195.1 110.0,194.4 112.6,193.7 115.3,193.0 117.9,192.2 120.6,191.4 123.2,190.7 125.8,189.8 128.5,189.0 131.1,188.1 133.8,187.2 136.4,186.3 139.0,185.4 141.7,184.4 144.3,183.4 147.0,182.4 149.6,181.3 152.3,180.3 154.9,179.2 157.5,178.1 160.2,176.9 162.8,175.8 165.5,174.6 168.1,173.4 170.8,172.1 173.4,170.9 176.0,169.6 178.7,168.3 181.3,166.9 184.0,165.6 186.6,164.2 189.2,162.8 191.9,161.3 194.5,159.9 197.2,158.4 199.8,156.9 202.5,155.4 205.1,153.8 207.7,152.2 210.4,150.6 213.0,149.0 215.7,147.3 218.3,145.6 221.0,143.9 223.6,142.2 226.2,140.5 228.9,138.7 231.5,136.9 234.2,135.1 236.8,133.2 239.5,131.3 242.1,129.4 244.7,127.5 247.4,125.6 250.0,123.6 252.7,121.6 255.3,119.6 257.9,117.5 260.6,115.4 263.2,113.3 265.9,111.2 268.5,109.1 271.2,106.9 273.8,104.7 276.4,102.5 279.1,100.3 281.7,98.0 284.4,95.7 287.0,93.4 289.7,91.0 292.3,88.7 294.9,86.3 297.6,83.9 300.2,81.4 302.9,79.0 305.5,76.5 308.1,74.0 310.8,71.4 313.4,68.9 316.1,66.3 318.7,63.7 321.4,61.0 324.0,58.4 326.6,55.7 329.3,53.0 331.9,50.2 334.6,47.5 337.2,44.7 339.9,41.9 342.5,39.1 345.1,36.2 347.8,33.3 350.4,30.4 353.1,27.5" fill="none" stroke="#6c4cf5" stroke-width="2.5" stroke-linejoin="round"/><polyline points="159.7,197.7 161.5,196.3 163.2,194.9 165.0,193.4 166.7,192.0 168.4,190.6 170.2,189.2 171.9,187.8 173.7,186.4 175.4,184.9 177.1,183.5 178.9,182.1 180.6,180.7 182.4,179.3 184.1,177.9 185.8,176.4 187.6,175.0 189.3,173.6 191.1,172.2 192.8,170.8 194.5,169.4 196.3,167.9 198.0,166.5 199.8,165.1 201.5,163.7 203.2,162.3 205.0,160.8 206.7,159.4 208.5,158.0 210.2,156.6 211.9,155.2 213.7,153.8 215.4,152.3 217.2,150.9 218.9,149.5 220.6,148.1 222.4,146.7 224.1,145.3 225.9,143.8 227.6,142.4 229.3,141.0 231.1,139.6 232.8,138.2 234.6,136.7 236.3,135.3 238.0,133.9 239.8,132.5 241.5,131.1 243.3,129.7 245.0,128.2 246.7,126.8 248.5,125.4 250.2,124.0 252.0,122.6 253.7,121.2 255.4,119.7 257.2,118.3 258.9,116.9 260.7,115.5 262.4,114.1 264.1,112.6 265.9,111.2 267.6,109.8 269.4,108.4 271.1,107.0 272.8,105.6 274.6,104.1 276.3,102.7 278.1,101.3 279.8,99.9 281.5,98.5 283.3,97.1 285.0,95.6 286.8,94.2 288.5,92.8 290.2,91.4 292.0,90.0 293.7,88.6 295.5,87.1 297.2,85.7 298.9,84.3 300.7,82.9 302.4,81.5 304.2,80.0 305.9,78.6 307.6,77.2 309.4,75.8 311.1,74.4 312.9,73.0 314.6,71.5 316.3,70.1 318.1,68.7 319.8,67.3 321.6,65.9 323.3,64.5 325.0,63.0 326.8,61.6 328.5,60.2 330.3,58.8 332.0,57.4 333.7,55.9 335.5,54.5 337.2,53.1 339.0,51.7 340.7,50.3 342.4,48.9 344.2,47.4 345.9,46.0 347.7,44.6 349.4,43.2 351.1,41.8 352.9,40.4 354.6,38.9 356.4,37.5 358.1,36.1 359.8,34.7 361.6,33.3 363.3,31.9 365.1,30.4 366.8,29.0 368.5,27.6" fill="none" stroke="#e5484d" stroke-width="2" stroke-dasharray="6 4" stroke-linejoin="round"/><circle cx="268.0" cy="109.5" r="4.5" fill="#e5484d"/><text x="279.6" y="120.0" font-size="13" fill="#e5484d" text-anchor="start">slope 6 at x = 3</text><text x="113.3" y="170.4" font-size="13" fill="#6c4cf5" text-anchor="middle">x²</text></svg>

<div class="quiz" data-answer="1" data-why="(16 − 9) ÷ 1 = 7. A big step overshoots the true slope 6. Shrink h in the drawing below and watch it head to 6."><p><b>Predict first:</b> f(x) = x². With a step h = 1 from x = 3, what slope do you get?</p><button>6</button><button>7</button><button>9</button></div>

<div class="explore" data-widget="derivative"></div>

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f'(x)` | "f prime of x" | the derivative of f, at x (the ' is a tiny tick mark) | `central_diff(f, x)` |
| `df/dx` | "d f d x" | the same thing, another notation: "tiny change in f over tiny change in x". **Not** a fraction you can cancel d's in! | |
| `d/dx` | "d by d x" | "take the derivative of what follows" | |
| `h` | "h" | the step size | `h = 1e-5` |
| `lim h→0` | "the limit as h goes to 0" | let the step shrink to nothing (lesson 02) | tiny `h` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">f'(x)</span> = <span class="k2">lim<sub>h→0</sub></span> ( <span class="k3">f(x + h)</span> − <span class="k4">f(x)</span> ) / <span class="k5">h</span></div>

| Piece | Say it | Means | x² at x = 3, h = 0.01 |
|---|---|---|---|
| <span class="k1">f'(x)</span> | "f prime of x" | the slope at x | → 6 |
| <span class="k4">f(x)</span> | "f of x" | where you are now | 9 |
| <span class="k3">f(x + h)</span> | "f of x plus h" | where you are after a small step | 9.0601 |
| <span class="k3">f(x + h)</span> − <span class="k4">f(x)</span> | "the difference" | Δy: how much the output moved | 0.0601 |
| / <span class="k5">h</span> | "over h" | per unit of step: Δy ÷ Δx | 6.01 |
| <span class="k2">lim<sub>h→0</sub></span> | "as h goes to zero" | let the step shrink | 6.01 → 6.001 → 6 |

It's lesson 01's `Δy / Δx` with `Δx = h`, made tiny.

## 🔀 What if it were different?

<div class="wrong"><b>Divide by x instead of h</b>: 0.0601 / 3 = 0.02. Nonsense: the slope would depend on where zero happens to be.</div>
<div class="wrong"><b>Forget the limit, use h = 1</b>: 7 instead of 6. A big step measures an average over a stretch, not the slope at the point.</div>
<div class="wrong"><b>h = 1e-15 in a computer</b>: (f(3 + 1e-15) − 9) / 1e-15 = 5.33. Floats only keep about 16 digits, so a too-tiny step drowns in rounding noise.</div>
<div class="right">a small but sensible h (like 1e-5), and even better the <b>central</b> version: ( f(x + h) − f(x − h) ) / 2h → 6.0000000 ✓</div>

## 🗣️ Say it out loud

`f'(3) = 6` → "f prime of 3 is 6" → "at x = 3, the output changes 6 times as fast as the input."

## 🤖 Where AI uses it

Everywhere in training. For every weight, the model asks: "If I nudge this weight, does the loss go up or down, and how much?" That's a derivative. Engineers also use the central difference to **check** that a hand-written gradient is correct ("gradient checking").

## 🎯 Your quest

1. `forward_diff(f, x, h)`: `(f(x + h) − f(x)) / h`.
2. `central_diff(f, x, h=1e-5)`: `(f(x + h) − f(x − h)) / (2h)`.
3. `tangent(f, x)`: the straight line touching f at x as `(m, b)`: `m = central_diff(f, x)`, `b = f(x) − m·x`.

**Remember:** derivative = slope at one point = how much the output moves per tiny nudge.

## Review

<details><summary>Limit of (x² − 1)/(x − 1) as x → 1?</summary>2.</details>
<details><summary>When does a limit not exist?</summary>When the left side and the right side head to different numbers.</details>
