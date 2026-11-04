---
title: Floating point: FP32, BF16, FP16
xp: 60
---
# Why 1 + 0.001 can equal 1

> **Warm-up:** in Python, `1.0 + 1e-17 == 1.0` is `True`. Why would a computer lose that 1e-17? And what happens when it loses a training update?

**In one sentence:** a float stores a number as "1.something × 2^power" with a fixed number of bits for each part; fewer bits for the "something" means coarser precision, fewer bits for the power means a smaller range.

## 🪜 Plain words

Like scientific notation (Math 1 lesson 08) but in base 2. Three parts:

- **sign**: + or −
- **exponent bits**: the power of 2 → decides the **range** (how big/small)
- **mantissa bits**: the digits after the "1." → decides the **precision** (how fine)

| format | bytes | exponent bits | mantissa bits | biggest | step just above 1 |
|---|---|---|---|---|---|
| FP32 | 4 | 8 | 23 | 3.4 × 10³⁸ | 0.00000012 |
| BF16 | 2 | 8 | 7 | 3.4 × 10³⁸ | 0.0078 |
| FP16 | 2 | 5 | 10 | **65,504** | 0.00098 |

BF16 keeps FP32's range but has few digits. FP16 has more digits but overflows above 65,504.

## 🪜 With numbers

- A weight is 1.0, the update is +0.001. In BF16, the nearest numbers around 1 are 1.0 and 1.0078. 1.001 rounds back to **1.0**: the update is lost. That's why training keeps a **master copy** of weights in FP32.
- 0.1 in FP16 is really **0.0999755859375**.
- An activation of 70,000 in FP16 becomes **inf** → NaN loss.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `(−1)ˢ` | "minus one to the s" | the sign: s = 0 → +, s = 1 → − | |
| `1.f` | "one point f" | the mantissa: hidden 1 plus the stored fraction bits | |
| `2ᵉ` | "two to the e" | the scale | `math.ldexp(m, e)` |
| `ε_mach` | "machine epsilon" | gap between 1 and the next number: 2^−(mantissa bits) | `2 ** -m` |
| `bias` | | exponent offset so small powers can be negative | `2 ** (e - 1) - 1` |

## 🔬 Take the formulas apart

<div class="formula">x = <span class="k1">(−1)ˢ</span> · <span class="k2">1.f</span> · 2<sup><span class="k3">e − bias</span></sup></div>

| Piece | Say it | Means | 6.5 |
|---|---|---|---|
| <span class="k1">(−1)ˢ</span> | "sign" | + or − | + |
| <span class="k2">1.f</span> | "one point f" | between 1 and 2, with as many binary digits as mantissa bits | 1.625 |
| 2<sup><span class="k3">e − bias</span></sup> | "two to the exponent" | the scale | 2² = 4 |

<div class="formula">biggest = ( 2 − 2<sup>−<span class="k4">m</span></sup> ) · 2<sup><span class="k5">bias</span></sup>, &nbsp; bias = 2<sup><span class="k6">E</span> − 1</sup> − 1 &nbsp;&nbsp; ε = 2<sup>−<span class="k4">m</span></sup></div>

| Piece | Means | FP16 (E = 5, m = 10) |
|---|---|---|
| <span class="k6">E</span> | exponent bits | 5 → bias 15 |
| <span class="k4">m</span> | mantissa bits | 10 |
| ( 2 − 2<sup>−m</sup> ) | largest mantissa: 1.1111111111 in binary | 1.999 |
| result | | 1.999 · 2¹⁵ = 65,504; ε = 0.00098 |

## 🔀 What if it were different?

<div class="wrong"><b>"BF16 and FP16 are the same, both 16 bits"</b>: FP16 overflows at 65,504; BF16 goes to 3.4 × 10³⁸ but has only ~2–3 decimal digits. FP16 training needs "loss scaling"; BF16 usually doesn't.</div>
<div class="wrong"><b>Keep the only copy of weights in BF16</b>: updates smaller than about 0.4% of a weight vanish (1 + 0.001 → 1). The model stops learning silently.</div>
<div class="wrong"><b>Compare floats with ==</b>: 0.1 + 0.2 == 0.3 is False. Compare with a tolerance.</div>
<div class="right">FP16 max 65,504, BF16 ε = 0.0078, 1.001 → 1.0 in BF16 ✓</div>

## 🗣️ Say it out loud

"x equals minus one to the s, times one point f, times two to the e minus bias."

## 🤖 Where AI uses it

"Mixed precision" training (BF16 compute, FP32 master weights), FP8 on new GPUs, and memory math: 7B parameters × 2 bytes (BF16) = 14 GB (LLMs 2).

## 🎯 Your quest

1. `epsilon(man_bits)`: 2^−man_bits.
2. `max_value(exp_bits, man_bits)`.
3. `round_to_bits(x, man_bits)`: round x to that many mantissa bits. Hint: `m, e = math.frexp(x)` gives x = m · 2ᵉ with 0.5 ≤ |m| &lt; 1; scale m by 2^(man_bits + 1), `round`, scale back, `math.ldexp`.
4. `bytes_for(n_params, fmt)`: fmt is `"fp32"`, `"bf16"`, `"fp16"` or `"fp8"`.

**Remember:** exponent bits = range, mantissa bits = precision.

## Review

<details><summary>Weight decay factor per step?</summary>(1 − ηλ).</details>
<details><summary>What does AdamW's "W" change?</summary>Weight decay is applied separately from the Adam step (decoupled).</details>
