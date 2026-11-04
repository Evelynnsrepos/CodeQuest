---
title: Practice: mixed review
xp: 60
---
# Five small problems from the whole course

> **Warm-up:** without scrolling up, which of these five problems feels easiest? Start there; the order doesn't matter.

Mixed practice makes ideas stick better than doing the same kind of problem ten times. Each problem below repeats its formula and what every sign means, so you never have to look back. Work out one example on paper first, then write the function.

## 🎯 The problems

**1. At least once** (lesson 02). `P(at least once in n tries) = 1 − (1 − p)ⁿ`: one minus "it never happens".
Example: a 5% chance per test, 20 tests: 1 − 0.95²⁰ = **0.64**.
→ `at_least_once(p, n)`

**2. Bayes** (lesson 04). `P(A | B) = P(B | A) · P(A) / P(B)`, with `P(B) = P(B | A) P(A) + P(B | not A) P(not A)`. "P(A | B)" = "probability of A, given that B happened".
Example: 1% have it, the test finds 90% of them and false-alarms on 5%: 0.9 · 0.01 / (0.9 · 0.01 + 0.05 · 0.99) = **0.154**.
→ `bayes(prior, hit_rate, false_alarm)`

**3. Expected value** (lesson 06). `E[X] = Σ xᵢ · pᵢ`: each outcome times its probability, added up.
Example: win 10 € with 0.2, lose 2 € with 0.8: 2 − 1.6 = **0.4 €**.
→ `expected(values, probs)`

**4. z-score** (lesson 08). `z = (x − μ) / σ`. μ ("mu") = the mean, σ ("sigma") = the standard deviation. "How many σ away from the mean?"
Example: 185 with μ = 170, σ = 10: **1.5**.
→ `z(x, mu, sigma)`

**5. Standard error** (lesson 09). `SE = σ / √n`: averages of n things wobble √n times less.
Example: σ = 2, n = 100: **0.2**.
→ `standard_error(sigma, n)`

**Remember:** "given" means you only look at the cases where B happened.

## Review

<details><summary>What does P(A | B) mean?</summary>The probability of A among only the cases where B happened.</details>
