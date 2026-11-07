---
title: Speculative decoding: guess, then check
minutes: 40
xp: 60
hint: expected_tokens: if alpha == 1: return k + 1. Then return (1 - alpha ** (k + 1)) / (1 - alpha)
hint: speedup: return expected_tokens(alpha, k) / (1 + k * c)
hint: best_k: best = 1 and best_s = speedup(alpha, 1, c), then for k in range(2, max_k + 1): and keep k when its speed-up is bigger
---
# A small model drafts, the big one verifies

⏱️ About 40 minutes

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

## 🔬 The formula, one small step at a time

Take α = 0.8 and k = 4.

**Step 1: `α^(k+1)`.** The little raised number is a **power**: multiply α by itself that many times. k + 1 = 5, so 0.8⁵ = 0.8 × 0.8 × 0.8 × 0.8 × 0.8:

- 0.8 × 0.8 = 0.64
- 0.64 × 0.8 = 0.512
- 0.512 × 0.8 = 0.4096
- 0.4096 × 0.8 = **0.32768**

In Python a power is two stars: `0.8 ** 5`.

**Step 2: the top, 1 − 0.32768** = 0.67232.

**Step 3: the bottom, 1 − α** = 1 − 0.8 = 0.2.

**Step 4: divide**: 0.67232 / 0.2 = **3.3616** tokens per big pass on average.

Why this works: it's a short way to write 1 + α + α² + α³ + α⁴ = 1 + 0.8 + 0.64 + 0.512 + 0.4096 = 3.3616. The "1" is the token the big model always adds itself; each next term is the chance that the first 1, 2, 3, 4 guesses **all** got accepted in a row.

**Step 5: the cost**, 1 + k·c = 1 + 4 × 0.05 = 1.2. The `·` means "times".

**Step 6: speed-up** = 3.3616 / 1.2 = **2.80**.

<div class="wrong"><b>α = 1 in the formula</b>: 1 − 1 = 0 on the bottom, and dividing by zero crashes. When every guess is accepted you simply get all k guesses plus the big model's own token: k + 1. That's why your function checks <code>alpha == 1</code> first.</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `alpha ** (k + 1)` | "alpha to the power k plus one" | the power from step 1. The brackets make Python add first. |
| `if alpha == 1:` | | the special case, checked before the division |
| `expected_tokens(alpha, k)` inside `speedup` | | one of your functions can use another |
| `range(2, max_k + 1)` | "from 2 up to max k" | 2, 3, ..., max_k. The end number is not included, so `+ 1` puts max_k in. |
| `if s > best_s:` | | the best-so-far pattern: remember the biggest seen so far |

### 👀 Worked example: the best price per kilo

```python
prices = {1: 4.0, 2: 3.5, 3: 3.6}
best = 1
best_p = prices[1]
for size in range(2, 4):
    if prices[size] < best_p:
        best = size
        best_p = prices[size]
print(best)
```

1. Start with size 1 as "best so far": 4.0.
2. Size 2: 3.5 < 4.0 → new best is 2.
3. Size 3: 3.6 < 3.5? No → keep 2.
4. Prints `2`. `best_k` does the same, but looks for the **biggest** speed-up, so it uses `>`.

## 🎯 Your quest

1. `expected_tokens(alpha, k)` (when α = 1 the answer is k + 1).
2. `speedup(alpha, k, c)`.
3. `best_k(alpha, c, max_k=16)`: the k from 1 to max_k with the biggest speed-up.

**Part 1:** `expected_tokens`. Replace `return k + 1` with:

1. `if alpha == 1:`
2. `    return k + 1`
3. `return (1 - alpha ** (k + 1)) / (1 - alpha)`

**Part 2:** `speedup`. Replace `return 0` with:

1. `return expected_tokens(alpha, k) / (1 + k * c)`

**Part 3:** `best_k`. Replace `return 1` with:

1. `best = 1`
2. `best_s = speedup(alpha, 1, c)`
3. `for k in range(2, max_k + 1):`
4. `    s = speedup(alpha, k, c)`
5. `    if s > best_s:`
6. `        best = k`
7. `        best_s = s`
8. `return best`

**Remember:** accepted guesses must come in a row; long drafts only pay when α is high.

## Review

<details><summary>Cron for "every weekday at 7:30"?</summary>30 7 * * 1-5.</details>
