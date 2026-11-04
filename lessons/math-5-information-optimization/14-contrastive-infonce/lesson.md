---
title: Contrastive learning: InfoNCE
xp: 60
---
# Find your partner in the crowd

> **Warm-up:** you have a photo of a dog and four captions. One says "a dog on a beach". How could you train a model so the matching caption scores highest, without ever labelling "dog"?

**In one sentence:** InfoNCE treats "which item is my true partner?" as a classification problem: softmax over similarity scores divided by a temperature τ, and cross-entropy on the correct partner.

## 🪜 Plain words

- Turn each item (image, text) into a vector (an embedding).
- Similarity = cosine of the two vectors (Math 2 lesson 05).
- For each anchor, there is one **positive** (true partner) and many **negatives** (everything else in the batch).
- Loss: cross-entropy (lesson 03) where the "correct class" is the positive.

So the model is pushed to make the positive **more** similar and the negatives **less** similar, at the same time. Without negatives it could cheat by mapping everything to the same vector.

**Temperature τ** (tau) sharpens the scores. Cosines live in −1..1, which is too flat for softmax; dividing by τ = 0.07 stretches them.

## 🪜 With numbers

Similarities to the anchor: positive 0.9, negatives 0.1 and 0.2.

- τ = 1: logits 0.9, 0.1, 0.2 → p(positive) = 0.51 → loss **0.666**.
- τ = 0.1: logits 9, 1, 2 → p(positive) ≈ 0.9988 → loss **0.00125**.

Same embeddings, very different signal: τ controls how hard the model must separate pairs.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `sim(a, b)` | "sim of a and b" | cosine similarity | `cosine(a, b)` |
| `a`, `p` | "anchor", "positive" | item and its true partner | |
| `kₙ` | "k n" | the n-th candidate (positive or negative) | |
| `τ` | "tau" | temperature | `tau` |
| `exp` | "e to the" | as in softmax | `math.exp` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">L</span> = − log &nbsp; <span class="k2">exp( sim(a, p) / τ )</span> &nbsp;/&nbsp; <span class="k3">Σₙ exp( sim(a, kₙ) / τ )</span></div>

| Piece | Say it | Means | τ = 0.1 |
|---|---|---|---|
| <span class="k2">exp( sim(a, p) / τ )</span> | "e to the sim of a and p over tau" | score of the true partner | e⁹ |
| <span class="k3">Σₙ exp( sim(a, kₙ) / τ )</span> | "sum over all candidates" | scores of everyone, partner included | e⁹ + e¹ + e² |
| fraction | | softmax probability of the partner | 0.9988 |
| <span class="k1">L</span> = − log | "minus log" | cross-entropy | 0.00125 |

**CLIP** does this both ways: for each image pick its caption (rows), and for each caption pick its image (columns), then averages.

## 🔀 What if it were different?

<div class="wrong"><b>Loss = −sim(a, p) only</b> (no negatives): the easiest solution is mapping every input to the same vector: similarity 1 for everything. "Collapse": useless embeddings.</div>
<div class="alt"><b>Leave the positive out of the bottom sum</b>: the fraction can now exceed 1, so the loss can go below 0. It can't fall forever, though: cosine similarity is capped at 1 and −1, so the loss has a floor. This variant ("decoupled contrastive learning") is used in research and can train faster with small batches. It's just a different number from the standard InfoNCE that CLIP uses, which is what the check expects.</div>
<div class="wrong"><b>τ = 1</b> with cosines: loss stays around 0.67 even when the pair is clearly best; the signal is too weak to sharpen embeddings.</div>
<div class="right">−log softmax(sims / τ)[positive]: 0.666 at τ = 1, 0.00125 at τ = 0.1 ✓</div>

## 🗣️ Say it out loud

"L is minus log of e to the sim of a, p over tau, divided by the sum over n of e to the sim of a, k n over tau."

## 🤖 Where AI uses it

**CLIP** (image ↔ text, AI beyond LLMs), **embedding models** for RAG (LLMs 4: query ↔ relevant passage), SimCLR for images. A larger batch = more negatives = better embeddings.

## 🎯 Your quest

1. `info_nce(sims, pos, tau)`: sims to every candidate, `pos` = index of the positive. Use a safe log-sum-exp (lesson 06).
2. `clip_loss(S, tau)`: S is a square matrix, S[i][j] = sim(image i, text j); true pairs are on the diagonal. Average of all row losses and all column losses.

**Remember:** contrastive = cross-entropy where the right answer is your partner.

## Review

<details><summary>Quantization scale?</summary>max |w| / q_max.</details>
<details><summary>Why per-block scales?</summary>So one outlier doesn't ruin every other weight's precision.</details>
