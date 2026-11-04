---
title: Speculative decoding: guess, then check
xp: 60
---
# A small model drafts, the big one verifies

> **Warm-up:** the big model needs one slow pass per token. Checking 5 tokens at once costs about the same as generating 1. How could you use that?

**In one sentence:** a tiny draft model guesses k tokens, the big model checks them all in one pass and keeps the ones it agrees with, so you get several tokens per big-model pass.

## 🪜 Plain words

1. The draft model (fast, say 20× cheaper) writes k tokens.
2. The big model runs **once** over all k and accepts them from the start until the first one it disagrees with. It then adds one token of its own (the correction, or the next token if all k were accepted).
3. The output is exactly what the big model would have produced (the acceptance rule is designed for that), just faster.

How much faster depends on α, the chance each guess is accepted. Guesses must be accepted **in a row**, so long drafts pay off only when α is high.

## 🪜 With numbers

α = 0.8, k = 4, draft cost c = 0.05 of a big pass:

- Expected tokens per big pass: (1 − 0.8⁵) / (1 − 0.8) = (1 − 0.328) / 0.2 = **3.36**
- Cost per round: 1 big pass + 4 draft steps × 0.05 = **1.2**
- Speed-up: 3.36 / 1.2 = **2.8×**

With α = 0.5: (1 − 0.5⁵) / 0.5 = 1.94 tokens → 1.94 / 1.2 = **1.6×**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `α` | "alpha" | chance one draft token is accepted | `alpha` |
| `k` | "k" | draft length | `k` |
| `αᵏ⁺¹` | "alpha to the k plus one" | (the formula's tail term) | `alpha ** (k + 1)` |
| `c` | "c" | draft step cost relative to one big pass | `c` |
| `E[tokens]` | "expected tokens" | average tokens per big pass (Math 4) | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">E[tokens]</span> = ( <span class="k2">1</span> − <span class="k3">α<sup>k+1</sup></span> ) / ( <span class="k2">1</span> − <span class="k4">α</span> ) &nbsp;&nbsp;&nbsp; <span class="k5">speed-up</span> = <span class="k1">E[tokens]</span> / ( <span class="k2">1</span> + <span class="k6">k·c</span> )</div>

| Piece | Means | α = 0.8, k = 4 |
|---|---|---|
| <span class="k4">α</span> | accept chance per token | 0.8 |
| <span class="k3">α<sup>k+1</sup></span> | the part of the sum that's cut off at k | 0.328 |
| ( 1 − … ) / ( 1 − α ) | 1 + α + α² + … + αᵏ: chance of getting 1, 2, … tokens accepted, added up | 3.36 |
| <span class="k6">k·c</span> | the draft's cost | 0.2 |
| <span class="k5">speed-up</span> | tokens per unit of time vs 1 | 2.8 |

## 🔀 What if it were different?

<div class="wrong"><b>Assume all k always get accepted</b>: 5 tokens per pass → "4.2× faster". Real: 2.8×. Guesses fail in a row, not independently.</div>
<div class="wrong"><b>k = 20 with α = 0.5</b>: tokens ≈ 2, but cost = 1 + 20·0.05 = 2 → speed-up ≈ 1: no gain, extra complexity.</div>
<div class="wrong"><b>Ignore the draft's cost</b>: overestimates every speed-up, most for big k.</div>
<div class="right">(1 − α^(k+1)) / (1 − α) ÷ (1 + kc) ✓</div>

## 🤖 Where AI uses it

llama.cpp `--model-draft`, vLLM and most API providers use it (the guide: 1.5–2× typical). Variants: Medusa, EAGLE, and multi-token prediction heads (DeepSeek V3).

## 🎯 Your quest

1. `expected_tokens(alpha, k)` (when α = 1 the answer is k + 1).
2. `speedup(alpha, k, c)`.
3. `best_k(alpha, c, max_k=16)`: the k from 1 to max_k with the biggest speed-up.

**Remember:** accepted guesses must come in a row; long drafts only pay when α is high.

## Review

<details><summary>Cron for "every weekday at 7:30"?</summary>30 7 * * 1-5.</details>
