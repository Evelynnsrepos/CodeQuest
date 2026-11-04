---
title: Practice: mixed review
xp: 60
---
# Five small problems from the whole course

> **Warm-up:** without scrolling up, which of these five problems feels easiest? Start there; the order doesn't matter.

Mixed practice makes ideas stick better than doing the same kind of problem ten times. Each problem below repeats its formula and what every sign means, so you never have to look back. Work out one example on paper first, then write the function.

## 🎯 The problems

**1. Surprise in bits** (lesson 01). `surprise = −log₂ p`: rare things carry more information.
Example: p = 1/8 → **3 bits**.
→ `bits(p)`

**2. Cross-entropy loss for one token** (lesson 03). `loss = −ln p(correct token)`. "ln" = the natural log (base e).
Example: the model gave the right token 0.25 → **1.386**.
→ `token_loss(p)`

**3. Perplexity from loss** (lesson 05). `perplexity = e^loss`: "as unsure as choosing among this many tokens".
Example: loss 1.386 → **4**.
→ `perplexity(loss)`

**4. KL divergence** (lesson 04). `KL(P ‖ Q) = Σ pᵢ · ln(pᵢ / qᵢ)`: the extra cost of using Q when the truth is P. Skip terms where pᵢ = 0.
Example: P = (0.5, 0.5), Q = (0.9, 0.1): 0.5 ln(0.5/0.9) + 0.5 ln(0.5/0.1) = **0.511**.
→ `kl(p, q)`

**5. Quantization step** (lesson 13). With `b` bits you have 2ᵇ levels. Spreading them evenly from −m to m gives a step of `2m / (2ᵇ − 1)`, and the worst rounding error is half a step.
Example: 4 bits, m = 1: step 2 / 15 = 0.133, worst error **0.0667**.
→ `worst_error(bits, m)`

**Remember:** loss, perplexity and bits are the same idea in different units.

## Review

<details><summary>Why is KL(P ‖ Q) not the same as KL(Q ‖ P)?</summary>Each weights the log ratio by a different distribution, so the sums differ; KL isn't symmetric.</details>
