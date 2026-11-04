---
title: KL divergence: distance between beliefs
xp: 60
---
# How much extra surprise do wrong beliefs cost?

> **Warm-up:** the truth is a fair coin. You believe it lands heads 90% of the time. You'll be wrong-footed a lot. Can we measure **how much** worse off you are than someone who knows the truth?

**In one sentence:** KL divergence is the extra average surprise you pay for using q when the truth is p: cross-entropy minus entropy. It's 0 only when q = p, and it is **not** symmetric.

## 🪜 Plain words

- Someone who knows the truth p has average surprise H(p) (lesson 02).
- You, believing q, have average surprise H(p, q) (lesson 03).
- The **difference** is the penalty for wrong beliefs: KL(p ‖ q).

It's never negative (wrong beliefs never help). It's not a true distance: "how wrong q is about p" is a different number from "how wrong p is about q".

## 🪜 With numbers

p = fair coin (0.5, 0.5), q = (0.9, 0.1). In nats:

- KL(p ‖ q) = 0.5 ln(0.5/0.9) + 0.5 ln(0.5/0.1) = −0.294 + 0.805 = **0.511**
- KL(q ‖ p) = 0.9 ln(0.9/0.5) + 0.1 ln(0.1/0.5) = 0.529 − 0.161 = **0.368**

Different! Order matters.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `KL(p ‖ q)` or `D_KL(p ‖ q)` | "K L of p from q" / "KL divergence of p and q" | extra surprise from using q when truth is p | `kl(p, q)` |
| `‖` | "double bar" | separates the two; **not** a norm here, and order matters | |
| `log(p/q)` | "log p over q" | = log p − log q | |
| `π_θ`, `π_ref` | "pi theta", "pi ref" | the model being trained, the frozen reference | |
| `β` | "beta" | how strong the KL penalty is | `beta` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">KL(p ‖ q)</span> = <span class="k2">Σ<sub>x</sub></span> <span class="k3">p(x)</span> · <span class="k4">log( p(x) / q(x) )</span> = <span class="k5">H(p, q)</span> − <span class="k6">H(p)</span></div>

| Piece | Say it | Means | fair vs 90/10 |
|---|---|---|---|
| <span class="k3">p(x)</span> | "p of x" | weight by the **truth** | 0.5, 0.5 |
| <span class="k4">log( p(x) / q(x) )</span> | "log of p over q" | how much less surprised the truth-knower is on x | −0.588, +1.609 |
| <span class="k2">Σ<sub>x</sub></span> | "sum over x" | add | |
| <span class="k5">H(p, q)</span> − <span class="k6">H(p)</span> | "cross-entropy minus entropy" | same thing | 1.204 − 0.693 = 0.511 |

## 🔀 What if it were different?

<div class="wrong"><b>Treat it as symmetric</b>: 0.511 vs 0.368. In RLHF, KL(π_θ ‖ π_ref) and KL(π_ref ‖ π_θ) push the model in different ways (one makes it pick a single safe mode, the other spreads it out).</div>
<div class="wrong"><b>Weight by q instead of p</b>: that's KL(q ‖ p) under a different name: the other number.</div>
<div class="wrong"><b>Flip the fraction, log(q/p)</b>: −0.511. A negative "distance" is a sign the fraction is upside down.</div>
<div class="right">KL(fair ‖ 90/10) = 0.511 nats, ≥ 0, and KL(p ‖ p) = 0 ✓</div>

## 🗣️ Say it out loud

"K L of p from q equals the sum over x of p of x times log p of x over q of x."

## 🤖 Where AI uses it

**RLHF / PPO / GRPO** (LLMs 8): reward − β · KL(π_θ ‖ π_ref) stops the model drifting into gibberish that fools the reward model. **Distillation** (lesson 15) minimises KL(teacher ‖ student). **VAEs** and diffusion training include KL terms. Training on one-hot data, minimising cross-entropy = minimising KL, because H(p) is fixed.

## 🎯 Your quest

1. `kl(p, q)`: in nats, skip terms where p is 0.
2. `kl_via_entropy(p, q)`: H(p, q) − H(p), to confirm they match.

**Remember:** KL = extra surprise for wrong beliefs; ≥ 0; order matters.

## Review

<details><summary>Cross-entropy loss for one correct token with q = 0.7?</summary>−ln 0.7 ≈ 0.357.</details>
<details><summary>Which goes inside the log in cross-entropy, truth or model?</summary>The model's q.</details>
