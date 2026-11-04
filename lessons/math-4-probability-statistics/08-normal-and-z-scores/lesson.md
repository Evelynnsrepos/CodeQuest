---
title: The normal curve and z-scores
xp: 55
---
# The bell curve, and "how unusual is this?"

> **Warm-up:** adults average 170 cm, give or take about 10 cm. Is 185 cm unusual? Is 210 cm? How would you put a number on "unusual"?

**In one sentence:** the normal distribution is the bell-shaped curve that shows up whenever many small random effects add up, and a z-score says how many standard deviations a value is from the mean.

## 🪜 Plain words

Lots of things cluster around an average, with fewer and fewer cases further out: heights, measurement errors, the sum of many dice. That shape is the **bell curve**, or **normal distribution**. It is fully described by two numbers: its middle (μ) and its width (σ).

A **z-score** converts any value into "how many σ's away from the middle". That lets you compare things on different scales.

The famous rule: about **68%** of values fall within 1σ, **95%** within 2σ, **99.7%** within 3σ.

## 🪜 With numbers

Heights: μ = 170, σ = 10.

- 185 cm: (185 − 170) / 10 = **z = 1.5**. Tall, not rare (about 7% are taller).
- 210 cm: (210 − 170) / 10 = **z = 4**. Extremely rare (about 3 in 100,000).
- 160 cm: **z = −1**. Negative z = below average.

Standardising a whole list (subtract the mean, divide by σ): `[2, 4, 4, 4, 5, 5, 7, 9]` (μ = 5, σ = 2) → `[−1.5, −0.5, −0.5, −0.5, 0, 0, 1, 2]`.


<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="Bell curve with the middle band between −1 and 1 standard deviations (68%) and between −2 and 2 (95%) shaded"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="204.0" x2="392" y2="204.0" stroke="currentColor" opacity=".45"/><line x1="210.0" y1="28" x2="210.0" y2="210" stroke="currentColor" opacity=".45"/><text x="79.5" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">-3</text><text x="123.0" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">-2</text><text x="166.5" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">-1</text><text x="210.0" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">0</text><text x="253.5" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">1</text><text x="297.0" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">2</text><text x="340.5" y="220.0" font-size="11" fill="currentColor" text-anchor="middle">3</text><text x="396.0" y="208.0" font-size="12" fill="currentColor" text-anchor="start">z</text><text x="216.0" y="24.0" font-size="12" fill="currentColor" text-anchor="start"></text><polygon points="123.0,204.0 123.0,183.8 125.2,181.8 127.4,179.5 129.5,177.1 131.7,174.5 133.9,171.8 136.1,168.9 138.2,165.8 140.4,162.6 142.6,159.2 144.8,155.6 146.9,151.9 149.1,148.1 151.3,144.1 153.4,140.0 155.6,135.8 157.8,131.5 160.0,127.1 162.1,122.7 164.3,118.2 166.5,113.7 168.7,109.2 170.8,104.7 173.0,100.2 175.2,95.8 177.4,91.6 179.5,87.4 181.7,83.4 183.9,79.6 186.1,76.0 188.2,72.6 190.4,69.4 192.6,66.5 194.8,63.9 197.0,61.6 199.1,59.6 201.3,58.0 203.5,56.7 205.7,55.8 207.8,55.2 210.0,55.1 212.2,55.2 214.3,55.8 216.5,56.7 218.7,58.0 220.9,59.6 223.0,61.6 225.2,63.9 227.4,66.5 229.6,69.4 231.8,72.6 233.9,76.0 236.1,79.6 238.3,83.4 240.5,87.4 242.6,91.6 244.8,95.8 247.0,100.2 249.2,104.7 251.3,109.2 253.5,113.7 255.7,118.2 257.9,122.7 260.0,127.1 262.2,131.5 264.4,135.8 266.5,140.0 268.7,144.1 270.9,148.1 273.1,151.9 275.2,155.6 277.4,159.2 279.6,162.6 281.8,165.8 284.0,168.9 286.1,171.8 288.3,174.5 290.5,177.1 292.7,179.5 294.8,181.8 297.0,183.8 297.0,204.0" fill="#6c4cf5" fill-opacity="0.15"/><polygon points="166.5,204.0 166.5,113.7 167.6,111.4 168.7,109.2 169.8,106.9 170.8,104.7 171.9,102.4 173.0,100.2 174.1,98.0 175.2,95.8 176.3,93.7 177.4,91.6 178.5,89.5 179.5,87.4 180.6,85.4 181.7,83.4 182.8,81.5 183.9,79.6 185.0,77.8 186.1,76.0 187.2,74.2 188.2,72.6 189.3,71.0 190.4,69.4 191.5,67.9 192.6,66.5 193.7,65.2 194.8,63.9 195.9,62.7 197.0,61.6 198.0,60.6 199.1,59.6 200.2,58.8 201.3,58.0 202.4,57.3 203.5,56.7 204.6,56.2 205.7,55.8 206.7,55.5 207.8,55.2 208.9,55.1 210.0,55.1 211.1,55.1 212.2,55.2 213.3,55.5 214.3,55.8 215.4,56.2 216.5,56.7 217.6,57.3 218.7,58.0 219.8,58.8 220.9,59.6 222.0,60.6 223.0,61.6 224.1,62.7 225.2,63.9 226.3,65.2 227.4,66.5 228.5,67.9 229.6,69.4 230.7,71.0 231.8,72.6 232.8,74.2 233.9,76.0 235.0,77.8 236.1,79.6 237.2,81.5 238.3,83.4 239.4,85.4 240.5,87.4 241.5,89.5 242.6,91.6 243.7,93.7 244.8,95.8 245.9,98.0 247.0,100.2 248.1,102.4 249.2,104.7 250.2,106.9 251.3,109.2 252.4,111.4 253.5,113.7 253.5,204.0" fill="#6c4cf5" fill-opacity="0.25"/><polyline points="36.0,204.0 38.9,203.9 41.8,203.9 44.7,203.9 47.6,203.9 50.5,203.8 53.4,203.8 56.3,203.7 59.2,203.6 62.1,203.5 65.0,203.4 67.9,203.3 70.8,203.1 73.7,202.9 76.6,202.6 79.5,202.3 82.4,202.0 85.3,201.6 88.2,201.0 91.1,200.4 94.0,199.7 96.9,198.9 99.8,198.0 102.7,196.9 105.6,195.6 108.5,194.2 111.4,192.6 114.3,190.8 117.2,188.7 120.1,186.4 123.0,183.8 125.9,181.0 128.8,177.9 131.7,174.5 134.6,170.8 137.5,166.9 140.4,162.6 143.3,158.0 146.2,153.2 149.1,148.1 152.0,142.8 154.9,137.2 157.8,131.5 160.7,125.6 163.6,119.7 166.5,113.7 169.4,107.7 172.3,101.7 175.2,95.8 178.1,90.2 181.0,84.7 183.9,79.6 186.8,74.8 189.7,70.4 192.6,66.5 195.5,63.1 198.4,60.3 201.3,58.0 204.2,56.4 207.1,55.4 210.0,55.1 212.9,55.4 215.8,56.4 218.7,58.0 221.6,60.3 224.5,63.1 227.4,66.5 230.3,70.4 233.2,74.8 236.1,79.6 239.0,84.7 241.9,90.2 244.8,95.8 247.7,101.7 250.6,107.7 253.5,113.7 256.4,119.7 259.3,125.6 262.2,131.5 265.1,137.2 268.0,142.8 270.9,148.1 273.8,153.2 276.7,158.0 279.6,162.6 282.5,166.9 285.4,170.8 288.3,174.5 291.2,177.9 294.1,181.0 297.0,183.8 299.9,186.4 302.8,188.7 305.7,190.8 308.6,192.6 311.5,194.2 314.4,195.6 317.3,196.9 320.2,198.0 323.1,198.9 326.0,199.7 328.9,200.4 331.8,201.0 334.7,201.6 337.6,202.0 340.5,202.3 343.4,202.6 346.3,202.9 349.2,203.1 352.1,203.3 355.0,203.4 357.9,203.5 360.8,203.6 363.7,203.7 366.6,203.8 369.5,203.8 372.4,203.9 375.3,203.9 378.2,203.9 381.1,203.9 384.0,204.0" fill="none" stroke="#6c4cf5" stroke-width="2.5" stroke-linejoin="round"/><text x="210.0" y="140.5" font-size="13" fill="#6c4cf5" text-anchor="middle">68%</text><text x="144.8" y="185.3" font-size="12" fill="#6c4cf5" text-anchor="middle">95%</text><text x="275.2" y="185.3" font-size="12" fill="#6c4cf5" text-anchor="middle">95%</text><text x="336.2" y="174.1" font-size="12" fill="#e5484d" text-anchor="middle">z = 1.5</text><line x1="275.2" y1="204.0" x2="275.2" y2="155.6" stroke="#e5484d" stroke-width="2" stroke-linecap="round"/></svg>

<div class="quiz" data-answer="0" data-why="(150 − 170) ÷ 10 = −2: two standard deviations below average."><p><b>Predict first:</b> heights have μ = 170 and σ = 10. What is the z-score of 150 cm?</p><button>−2</button><button>2</button><button>−20</button></div>

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `N(μ, σ²)` | "normal with mean mu and variance sigma squared" | the bell curve with that centre and width (note: the 2nd number is σ², not σ!) | `random.gauss(mu, sigma)` |
| `X ∼ N(0, 1)` | "X is standard normal" | centre 0, width 1 | |
| `z` | "z" / "z-score" | distance from the mean in σ's | `(x - mu) / sigma` |
| `p(x)` | "the density at x" | height of the curve (not a probability by itself; area is, Math 3 lesson 12) | |
| `π` | "pi" (here really 3.14159…) | | `math.pi` |
| `exp(…)` | "e to the" | (Math 1) | `math.exp` |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">z</span> = ( <span class="k2">x</span> − <span class="k3">μ</span> ) / <span class="k4">σ</span></div>

| Piece | Say it | Means | 185 cm |
|---|---|---|---|
| <span class="k2">x</span> | "x" | the value | 185 |
| − <span class="k3">μ</span> | "minus mu" | distance from the middle | 15 |
| / <span class="k4">σ</span> | "over sigma" | measured in standard deviations | 1.5 |

<div class="formula"><span class="k5">p(x)</span> = <span class="k6">1 / (σ√(2π))</span> · exp( <span class="k5">−</span> <span class="k1">z²</span> / 2 )</div>

| Piece | Means | At x = μ (z = 0), σ = 1 |
|---|---|---|
| <span class="k1">z²</span> | squared distance in σ's: the further out, the bigger | 0 |
| exp( <span class="k5">−</span> … / 2 ) | turns distance into height: e⁰ = 1 in the middle, tiny far out | 1 |
| <span class="k6">1 / (σ√(2π))</span> | scaling so the total area is exactly 1 | 0.399 |

## 🔀 What if it were different?

<div class="wrong"><b>Divide by σ² (variance) instead of σ</b>: (185 − 170) / 100 = 0.15. Everyone looks perfectly average.</div>
<div class="wrong"><b>Forget to subtract μ</b>: 185 / 10 = 18.5. Every height looks impossibly extreme.</div>
<div class="wrong"><b>exp(+z²/2)</b> (no minus): the curve grows instead of shrinking away from the middle; the area becomes infinite.</div>
<div class="wrong"><b>Read N(0, 4) as σ = 4</b>: it's σ² = 4, so σ = 2. You'd think it's twice as wide as it is.</div>
<div class="right">z = 1.5 for 185 cm; p(0) = 0.399 for N(0, 1) ✓</div>

## 🗣️ Say it out loud

"z equals x minus mu, over sigma."

## 🤖 Where AI uses it

**LayerNorm** is literally a z-score of each token's vector (then scaled). Weights are initialised from N(0, σ²). **Diffusion** models add normal noise, then learn to remove it (AI beyond LLMs). Anomaly detection flags |z| > 3.

## 🎯 Your quest

1. `z_score(x, mu, sigma)`.
2. `normal_pdf(x, mu, sigma)`.
3. `standardize(xs)`: z-score every value using the list's own mean and σ (divide by n).

**Remember:** z = how many σ's from the mean; 68/95/99.7.

## Review

<details><summary>Variance in words?</summary>The average squared distance from the mean.</details>
<details><summary>Why square the distances?</summary>So distances above and below don't cancel to 0.</details>
