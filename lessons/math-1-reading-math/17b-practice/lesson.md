---
title: Practice: mixed review
xp: 60
---
# Five small problems from the whole course

> **Warm-up:** without scrolling up, which of these five problems feels easiest? Start there; the order doesn't matter.

Mixed practice makes ideas stick better than doing the same kind of problem ten times. Each problem below repeats its formula and what every sign means, so you never have to look back. Work out one example on paper first, then write the function.

## 🎯 The problems

**1. Percent change** (lesson 05). `change % = (new − old) / old · 100`. "/" = divided by, "·" = times.
Example: a model's loss falls from 2.0 to 1.5: (1.5 − 2.0) / 2.0 · 100 = **−25%**.
→ `percent_change(old, new)`

**2. Slope** (lesson 10). `slope = (y₂ − y₁) / (x₂ − x₁)`: "how much up, for each step across". The small numbers ₁ and ₂ just mean "first point" and "second point".
Example: (0, 3) and (2, 7): (7 − 3) / (2 − 0) = **2**.
→ `slope(p1, p2)` where each point is a pair `(x, y)`

**3. A sum with Σ** (lesson 12). `Σᵢ₌ₐᵇ f(i)` = "add up f(i) for every whole number i from a to b, both included".
Example: Σᵢ₌₁³ i² = 1 + 4 + 9 = **14**.
→ `sigma(f, a, b)`

**4. Halving with logs** (lesson 14). How many times can you halve n until you reach 1 or less? That's `log₂ n`, rounded **up**. "log₂ n" = "which power of 2 gives n".
Example: 1000 → log₂ 1000 ≈ 9.97 → **10** halvings. (This is why binary search is so fast.)
→ `halvings(n)` (use `math.ceil(math.log2(n))`)

**5. Intervals** (lesson 16). `[a, b]` includes both ends, `(a, b)` excludes both, `[a, b)` includes a but not b. A square bracket "hugs" its number; a round one keeps it out.
Example: is 1 in [0, 1)? **No**.
→ `in_interval(x, a, b, left_closed, right_closed)`

**Remember:** say each formula out loud before you code it.

## Review

<details><summary>What does the small ₁ in y₁ mean?</summary>Just a label: "the y of the first point". It's not a multiplication or a power.</details>
