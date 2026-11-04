---
title: Cross-entropy: the loss LLMs train on
xp: 60
---
# Surprise measured with the wrong beliefs

> **Warm-up:** the true next word is "cat". Model A gave "cat" 70%, model B gave it 10%. Which model should be punished more, and by how much more?

**In one sentence:** cross-entropy is your average surprise when reality follows p but you **believed** q; with one correct answer it's simply −log of the probability you gave that answer.

## 🪜 Plain words

Entropy (lesson 02) uses the **true** probabilities for both the weights and the surprise. Cross-entropy keeps the true weights but measures surprise with the **model's** probabilities.

In LLM training the "truth" for each position is simple: the real next token has probability 1, everything else 0 (a **one-hot** vector). Then all terms vanish except one: **loss = −log q(correct token)**.

- Model gave the right answer 70% → loss 0.357.
- Model gave it 10% → loss 2.30. About 6.5× more punishment.
- Model gave it 0.1% → loss 6.9. Confidently wrong is punished hardest.

## 🪜 With numbers

Vocabulary: cat, dog, fish. True next token: cat → p = (1, 0, 0).

Model q = (0.7, 0.2, 0.1): H(p, q) = −(1 · ln 0.7 + 0 · ln 0.2 + 0 · ln 0.1) = **0.357 nats**.

Soft truth (e.g. label smoothing) p = (0.9, 0.05, 0.05): −(0.9 ln 0.7 + 0.05 ln 0.2 + 0.05 ln 0.1) = 0.321 + 0.080 + 0.115 = **0.516 nats**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `H(p, q)` | "the cross-entropy of p and q" | surprise under q, weighted by p | `cross_entropy(p, q)` |
| `p` | "p" | the truth (data) | `p` |
| `q` or `p_θ` | "q" / "p theta" | the model's prediction | `q` |
| one-hot | | all 0 except a single 1 | `[1, 0, 0]` |
| `y` | "y" | index of the correct answer | `target` |
| `q_y` | "q sub y" | the model's probability for the correct answer | `q[y]` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">H(p, q)</span> = − <span class="k2">Σ<sub>x</sub></span> <span class="k3">p(x)</span> · <span class="k4">log q(x)</span> &nbsp; → (one-hot) → &nbsp; <span class="k5">L</span> = − <span class="k4">log q<sub>y</sub></span></div>

| Piece | Say it | Means | cat example |
|---|---|---|---|
| <span class="k3">p(x)</span> | "p of x" | the **truth**'s weight | 1, 0, 0 |
| <span class="k4">log q(x)</span> | "log q of x" | the **model**'s log-probability | −0.357, −1.61, −2.30 |
| <span class="k2">Σ<sub>x</sub></span> | "sum over x" | add for all outcomes | only the 1 survives |
| <span class="k5">L</span> = − <span class="k4">log q<sub>y</sub></span> | "minus log q y" | loss for one token | 0.357 |

Average this over all tokens in the batch: that's the number in the training log.

## 🔀 What if it were different?

<div class="wrong"><b>Swap p and q, H(q, p)</b>: −(0.7 ln 1 + 0.2 ln 0 + 0.1 ln 0) = ∞. Truth has zeros; the log of 0 explodes. Order matters: <b>truth weights, model inside the log</b>.</div>
<div class="wrong"><b>Loss = 1 − q<sub>y</sub></b>: 0.3 for model A, 0.9 for model B, 0.999 for the 0.1% model. Confidently wrong is barely punished more than slightly wrong, and its gradient doesn't blow up the way it should: training gets slow.</div>
<div class="wrong"><b>Use the model's top-1 guess instead of q<sub>y</sub></b>: you'd score how confident the model is, not whether it was right.</div>
<div class="right">L = −ln 0.7 = 0.357 for one-hot "cat" ✓</div>

## 🗣️ Say it out loud

"H of p, q equals minus the sum over x of p of x log q of x." For one-hot: "minus log q y."

## 🤖 Where AI uses it

**Every** LLM pre-training and fine-tuning step, every classifier. `torch.nn.functional.cross_entropy(logits, targets)`. It equals the negative log-likelihood from Math 4 lesson 10.

## 🎯 Your quest

1. `cross_entropy(p, q)`: in nats; skip terms where p is 0.
2. `ce_loss(q, target)`: −ln q[target].
3. `batch_loss(qs, targets)`: average `ce_loss` over a batch.

**Remember:** truth outside the log, model inside; for one answer, loss = −log q(correct).

## Review

<details><summary>Entropy of a fair coin?</summary>1 bit.</details>
<details><summary>Entropy in words?</summary>The average surprise of a distribution.</details>
