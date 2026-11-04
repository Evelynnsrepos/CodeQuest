---
title: Practice: mixed review
xp: 60
---
# Five small problems from the whole course

> **Warm-up:** without scrolling up, which of these five problems feels easiest? Start there; the order doesn't matter.

Mixed practice makes ideas stick better than doing the same kind of problem ten times. Each problem below repeats its formula and what every sign means, so you never have to look back. Work out one example on paper first, then write the function.

## 🎯 The problems

**1. Slope from a tiny step** (lesson 03). `f′(x) ≈ (f(x + h) − f(x − h)) / (2h)` with a tiny h. "f′(x)" ("f prime of x") = the slope of f at x.
Example: f(x) = x³ at x = 2: ≈ **12** (the rule says 3x² = 12).
→ `slope_at(f, x)` with `h = 1e-5`

**2. The power rule** (lesson 04). The slope of `c · xⁿ` is `c · n · xⁿ⁻¹`: bring the power down front, lower it by one.
Example: 5x³ at x = 2: 5 · 3 · 2² = **60**.
→ `power_rule(c, n, x)`

**3. Chain rule** (lesson 06). For `(a·x + b)²` the slope is `2 · (a·x + b) · a`: "slope of the outside, times slope of the inside".
Example: (3x + 1)² at x = 1: 2 · 4 · 3 = **24**.
→ `chain_square(a, b, x)`

**4. ReLU's slope** (lessons 05, 11). `ReLU(x) = max(0, x)`. Its slope is **1** where x > 0 and **0** where x < 0 (at exactly 0, frameworks use 0).
→ `relu_slope(x)`

**5. One gradient-descent step** (lesson 10). `w_new = w − η · slope`. "η" ("eta") = the learning rate.
Example: w = 0, slope −6, η = 0.1 → **0.6**.
→ `gd_step(w, slope, lr)`

**Remember:** slope of the outside times slope of the inside.

## Review

<details><summary>What does f′(x) mean?</summary>The derivative: the slope of f at the point x.</details>
