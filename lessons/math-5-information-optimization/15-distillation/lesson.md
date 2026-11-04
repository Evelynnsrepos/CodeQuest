---
title: Distillation: a big model teaching a small one
xp: 60
---
# Learn from the teacher's doubts, not just its answers

> **Warm-up:** a teacher model says the next token is "cat" 94%, "kitten" 5%, "car" 1%. The real data just says "cat". Which tells a student model more?

**In one sentence:** distillation trains a small student to match a big teacher's softened probabilities (softmax at temperature T), using KL divergence multiplied by T².

## 🪜 Plain words

The one-hot label "cat" only says what's right. The teacher's full distribution also says "kitten is a close second, car is far off". That extra knowledge ("dark knowledge") helps a small model learn faster and better.

Raising the **temperature** (LLMs 1) before softmax spreads the probabilities out, so those small second-choice signals become visible. The student matches them using **KL divergence** (lesson 04).

Because dividing logits by T shrinks the gradients by about T², we multiply the loss by T² to keep the learning signal the same size whatever T is.

## 🪜 With numbers

Teacher logits (4, 1, 0):

- T = 1: (0.936, 0.047, 0.017). The second choice is barely visible.
- T = 4: logits (1, 0.25, 0) → (0.543, 0.257, 0.200). Much more to learn from.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `z_T`, `z_S` | "z teacher", "z student" | logits | `zt`, `zs` |
| `T` | "T" (capital) | temperature (not "transpose" here, and not time t!) | `T` |
| `softmax(z / T)` | "softmax of z over T" | softened probabilities | `soft_targets(z, T)` |
| `p_T^(T)` | "p teacher at temperature T" | | |
| `KL(p ‖ q)` | "KL of p from q" | lesson 04: truth (teacher) first | `kl(p, q)` |
| `T²` | "T squared" | gradient-size correction | `T * T` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">L</span> = <span class="k2">T²</span> · <span class="k3">KL</span>( <span class="k4">softmax(z_T / T)</span> ‖ <span class="k5">softmax(z_S / T)</span> )</div>

| Piece | Say it | Means | T = 4 |
|---|---|---|---|
| <span class="k4">softmax(z_T / T)</span> | "softmax of teacher logits over T" | the soft targets: the "truth" | (0.543, 0.257, 0.200) |
| <span class="k5">softmax(z_S / T)</span> | "softmax of student logits over T" | the student, softened the same way | |
| <span class="k3">KL</span>( … ‖ … ) | "KL of teacher from student" | extra surprise of the student's beliefs | |
| <span class="k2">T²</span> | "T squared" | keeps gradients the same size for any T | × 16 |

In practice it's often mixed with the ordinary hard-label loss: α · distill + (1 − α) · cross-entropy.

## 🔀 What if it were different?

<div class="wrong"><b>Forget T²</b>: at T = 4 the gradients are about 16× smaller; the distillation part barely trains, and changing T secretly changes the effective learning rate.</div>
<div class="wrong"><b>Soften only the teacher</b> (student at T = 1): the student is told to match a flat distribution with sharp logits; it learns to be underconfident.</div>
<div class="wrong"><b>KL(student ‖ teacher)</b> (order swapped): a different objective that lets the student ignore the teacher's second choices (lesson 04: KL isn't symmetric).</div>
<div class="right">T² · KL(soft teacher ‖ soft student), both at the same T ✓</div>

## 🗣️ Say it out loud

"L is T squared times the KL of softmax of z teacher over T, from softmax of z student over T."

## 🤖 Where AI uses it

Small models like DistilBERT, Gemma and Llama's smaller sizes are trained partly on bigger models' outputs; "distilled" reasoning models learn from a big model's step-by-step answers. Gradient: ∂L/∂z_S = T · (p_S − p_T), the p − y gradient (lesson 07) scaled by T.

## 🎯 Your quest

1. `soft_targets(z, T)`: softmax of z / T (shift by max).
2. `distill_loss(zt, zs, T)`: T² · KL(soft teacher ‖ soft student), in nats.

The check also verifies the gradient is T · (p_S − p_T).

**Remember:** soften both with T, match with KL, multiply by T².

## Review

<details><summary>Why does contrastive learning need negatives?</summary>Without them every input could map to the same vector (collapse).</details>
<details><summary>What does τ do?</summary>Sharpens the similarity scores before softmax.</details>
