---
title: The p − y gradient
xp: 60
---
# The most beautiful gradient in deep learning

> **Warm-up:** logits (2, 1, 0) become probabilities (0.665, 0.245, 0.090). The correct answer is the first one. Which way should each logit move to lower the loss?

**In one sentence:** for softmax followed by cross-entropy, the gradient of the loss with respect to each logit is just "predicted probability minus target": p − y.

## 🪜 Plain words

Combine softmax (logits → probabilities) and cross-entropy (−log p of the correct one), take the derivative (Math 3) with the chain and quotient rules, and almost everything cancels. What's left is shockingly simple:

- For the **correct** answer: p − 1 (negative → push its logit **up**).
- For **every wrong** answer: p − 0 = p (positive → push its logit **down**, more for the ones it wrongly liked more).

When the model is already perfect (p = y), the gradient is 0: nothing to fix.

## 🪜 With numbers

Logits (2, 1, 0), p = (0.665, 0.245, 0.090), correct = index 0, so y = (1, 0, 0).

Gradient = p − y = (0.665 − 1, 0.245, 0.090) = **(−0.335, 0.245, 0.090)**.

Gradient descent (θ − η · grad) raises logit 0 and lowers 1 and 2. The entries add up to 0: probability mass just moves around.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `z` | "z" | the logits (raw scores) | `logits` |
| `p = softmax(z)` | "p equals softmax of z" | probabilities | `softmax(z)` |
| `y` | "y" | one-hot target | `[1, 0, 0]` |
| `∂L/∂zᵢ` | "partial L partial z i" | how the loss changes if logit i moves (Math 3 lesson 08) | `grad[i]` |
| `1[i = t]` | "one if i is t" | 1 for the target, else 0 (an "indicator") | `int(i == t)` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">∂L / ∂zᵢ</span> = <span class="k2">pᵢ</span> − <span class="k3">yᵢ</span></div>

| Piece | Say it | Means | (2, 1, 0), target 0 |
|---|---|---|---|
| <span class="k2">pᵢ</span> | "p i" | the model's probability for i | 0.665, 0.245, 0.090 |
| <span class="k3">yᵢ</span> | "y i" | 1 for the correct answer, 0 otherwise | 1, 0, 0 |
| <span class="k1">∂L/∂zᵢ</span> | "partial L partial z i" | the gradient for logit i | −0.335, 0.245, 0.090 |

## 🔀 What if it were different?

<div class="wrong"><b>y − p</b> (flipped): (0.335, −0.245, −0.090). Gradient descent would lower the correct logit and raise the wrong ones: the model gets worse every step.</div>
<div class="wrong"><b>Only update the correct logit</b> (−0.335, 0, 0): the wrong answers never get pushed down directly, so learning is slower and less balanced.</div>
<div class="wrong"><b>Apply the gradient to the probabilities instead of the logits</b>: p would stop adding to 1. The gradient belongs to z; softmax fixes p afterwards.</div>
<div class="right">p − y = (−0.335, 0.245, 0.090), sums to 0 ✓</div>

## 🗣️ Say it out loud

"Partial L partial z i equals p i minus y i."

## 🤖 Where AI uses it

The very first step of backprop in every LLM training step, for every token, over the whole vocabulary. It also explains **label smoothing** (y like (0.9, 0.05, 0.05) means the gradient never quite reaches 0, so the model doesn't grow infinitely confident) and **distillation** (lesson 15: y becomes the teacher's p).

## 🎯 Your quest

`softmax` is given.

1. `ce_from_logits(z, target)`: −log softmax(z)[target].
2. `ce_grad(z, target)`: the list p − y.

The check compares your gradient with a numeric one (Math 3 lesson 08).

**Remember:** predicted minus target. That's the whole gradient.

## Review

<details><summary>Why subtract the max in softmax?</summary>So eˣ never overflows; the result is identical.</details>
<details><summary>log softmax(x)ᵢ?</summary>xᵢ − logsumexp(x).</details>
