---
title: Entropy, cross-entropy and KL divergence
xp: 45
---
# Measuring surprise

> **Warm-up:** which is more surprising: a fair coin landing heads, or rolling a 6 on a die? Can you put a number on "surprise"?

Information theory (Claude Shannon, 1948) measures surprise as `−log p`: certain events (p = 1) carry 0 surprise, rare ones a lot. Averaging surprise over a distribution gives three quantities that run all of machine learning:

```
entropy        H(p)    = −Σ pᵢ log pᵢ          how uncertain p itself is
cross-entropy  H(p, q) = −Σ pᵢ log qᵢ          average surprise when reality follows p
                                               but you predicted q
KL divergence  KL(p‖q) = H(p, q) − H(p)        the *extra* surprise caused by predicting
                       = Σ pᵢ log (pᵢ / qᵢ)    q instead of the truth p (always ≥ 0)
```

With natural logs the unit is **nats**; with log base 2 it's **bits**. A fair coin has 1 bit of entropy.

Why you care:

- **The LLM loss *is* cross-entropy.** The "truth" for one position is one-hot (the actual next token), so `H(p, q) = −log q_true`, exactly the loss from LLMs 1. Training minimizes it, which is the same as minimizing KL from the data to the model.
- **Perplexity** = `e^(cross-entropy)`.
- **KL appears in fine-tuning**: RLHF and DPO (Module 6) keep the tuned model close to the original by penalizing `KL(tuned ‖ reference)`, so it learns preferences without forgetting how to talk. **Distillation** trains a small model to minimize KL to a big model's full distributions.
- **Sampling**: temperature raises or lowers the entropy of the next-token distribution.

`0 · log 0` is treated as 0 (outcomes that can't happen contribute nothing).

## Your quest

Write `entropy(p)`, `cross_entropy(p, q)` and `kl(p, q)`, with natural logs, skipping terms where `pᵢ = 0`.

## Review

<details><summary>How does inverse transform sampling pick a token?</summary>Draw r uniformly in [0, 1) and walk the cumulative probabilities until the running total exceeds r.</details>
<details><summary>What does the law of large numbers say?</summary>The average over many samples approaches the expected value.</details>
<details><summary>What is a language model, in terms of conditional probability?</summary>A model of P(next token | all previous tokens).</details>
