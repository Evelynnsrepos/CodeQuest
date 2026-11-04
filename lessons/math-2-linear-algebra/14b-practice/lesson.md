---
title: Practice: mixed review
xp: 60
---
# Five small problems from the whole course

> **Warm-up:** without scrolling up, which of these five problems feels easiest? Start there; the order doesn't matter.

Mixed practice makes ideas stick better than doing the same kind of problem ten times. Each problem below repeats its formula and what every sign means, so you never have to look back. Work out one example on paper first, then write the function.

## 🎯 The problems

**1. Angle between two vectors** (lessons 03–05). `cos θ = (a · b) / (‖a‖ ‖b‖)`, then `θ = arccos(cos θ)`. "a · b" = multiply matching numbers and add; "‖a‖" = length = √(sum of squares); θ ("theta") is the angle.
Example: (1, 0) and (1, 1): cos θ = 1 / (1 · 1.414) = 0.707 → θ = **45°**.
→ `angle_deg(a, b)` (use `math.acos` and `math.degrees`)

**2. Matrix times vector** (lesson 07). Each output number = one row of the matrix dotted with the vector.
Example: [[1, 2], [3, 4]] · (1, 1) = (1 + 2, 3 + 4) = **(3, 7)**.
→ `matvec(M, v)`

**3. Distance** (lesson 04). `‖a − b‖ = √(Σ (aᵢ − bᵢ)²)`: subtract, square each, add, square root.
Example: (1, 2) to (4, 6): √(9 + 16) = **5**.
→ `distance(a, b)`

**4. Perpendicular?** (lesson 03). Two vectors are perpendicular ("⊥", at a right angle) exactly when `a · b = 0`.
Example: (2, 1) · (−1, 2) = −2 + 2 = 0 → **yes**.
→ `perpendicular(a, b)` (allow a tiny rounding error: `abs(dot) < 1e-9`)

**5. Parameters of a layer** (lesson 10). A layer from n inputs to m outputs has an m × n weight matrix plus m biases: `m · n + m` numbers.
Example: 768 → 3072: 768 · 3072 + 3072 = **2,362,368**.
→ `layer_params(n_in, n_out)`

**Remember:** a matrix row dotted with the vector gives one output number.

## Review

<details><summary>What does ‖a‖ mean?</summary>The length of vector a: the square root of the sum of its squared numbers.</details>
