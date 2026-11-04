---
title: Quantization: squeezing weights into small integers
xp: 60
---
# One scale number, many tiny integers

> **Warm-up:** you need to store 0.5, −1.27 and 0.03 using only whole numbers from −127 to 127. How would you do it so you can get the originals back (nearly)?

**In one sentence:** quantization picks a scale so the biggest weight maps to the biggest integer, stores round(weight ÷ scale) as a small integer, and multiplies back by the scale when needed.

## 🪜 Plain words

1. Find the weight furthest from 0: here 1.27.
2. Decide that it becomes the largest allowed integer (127 for 8 bits).
3. Scale = 1.27 / 127 = 0.01. Every integer step now means 0.01.
4. Store each weight as round(weight / 0.01). Keep the one scale number.
5. To use them: integer × scale.

The rounding loses at most **half a step** per weight.

## 🪜 With numbers

**8-bit** (−127..127): scale 0.01. 0.5 → **50**, −1.27 → **−127**, 0.03 → **3**. Back: 0.5, −1.27, 0.03. Perfect here.

**4-bit** (−7..7): scale 1.27 / 7 = 0.181. 0.5 / 0.181 = 2.76 → **3**, −1.27 → **−7**, 0.03 → 0.17 → **0**. Back: 0.544, −1.27, 0. Errors 0.044 and 0.03.

**One outlier** (100 in the group), 8-bit: scale 100 / 127 = 0.787. Now 0.5 → 1 (0.787), 0.03 → **0**. One giant weight ruins the precision of all the others. That's why formats like GGUF use a separate scale for every small block (e.g. 32 weights).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `s` | "s" / "the scale" | value of one integer step | `scale` |
| `q` | "q" | the stored integer | `q` |
| `ŵ` | "w hat" | the reconstructed (approximate) weight | `q * scale` |
| `max \|w\|` | "max absolute w" | the furthest weight from 0 | `max(abs(w) for w in ws)` |
| `round( )` | | nearest whole number | `round(x)` |
| `q_max = 2^(b−1) − 1` | "q max" | biggest integer with b bits (signed) | `2 ** (bits - 1) - 1` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">s</span> = <span class="k2">max |w|</span> / <span class="k3">q_max</span> &nbsp;&nbsp; <span class="k4">q</span> = round( <span class="k5">w</span> / <span class="k1">s</span> ) &nbsp;&nbsp; <span class="k6">ŵ</span> = <span class="k4">q</span> · <span class="k1">s</span></div>

| Piece | Say it | Means | 4-bit example |
|---|---|---|---|
| <span class="k2">max \|w\|</span> | "max absolute w" | biggest size in the group | 1.27 |
| <span class="k3">q_max</span> | "q max" | 2^(4−1) − 1 | 7 |
| <span class="k1">s</span> | "the scale" | one step | 0.181 |
| <span class="k4">q</span> | "q" | stored integers | 3, −7, 0 |
| <span class="k6">ŵ</span> | "w hat" | used weights | 0.544, −1.27, 0 |

## 🔀 What if it were different?

<div class="wrong"><b>q_max = 2ᵇ − 1 = 255 for 8 bits</b> (forgetting the sign takes a bit): scale 0.005, −1.27 → −254, which doesn't fit in −128..127. Overflow wraps or clips the weight badly.</div>
<div class="wrong"><b>Truncate instead of round</b> (int()): 2.76 → 2 → 0.363 instead of 0.544 (error 0.137, three times worse). Truncation always biases towards 0.</div>
<div class="wrong"><b>One scale for a whole layer with outliers</b>: small weights collapse to 0 (the 100-outlier example).</div>
<div class="right">8-bit: 50, −127, 3 with scale 0.01; 4-bit: 3, −7, 0 with scale 0.181 ✓</div>

## 🗣️ Say it out loud

"The scale is max absolute w over q max; q is the rounding of w over the scale."

## 🤖 Where AI uses it

Running models locally (LLMs 2): Q8_0, Q4_K_M and friends in GGUF, AWQ, GPTQ. A 7B model goes from 14 GB (BF16) to about 4 GB (4-bit) and fits on a normal GPU. QLoRA (LLMs 6) fine-tunes on top of 4-bit weights.

## 🎯 Your quest

1. `quantize(ws, bits)`: return `(qs, scale)` (symmetric, as above).
2. `dequantize(qs, scale)`.
3. `max_error(ws, bits)`: biggest |w − ŵ| after quantizing and dequantizing.

**Remember:** one scale per group, integers for the rest; max error is half a step.

## Review

<details><summary>FP16's biggest number?</summary>65,504.</details>
<details><summary>Why keep FP32 master weights?</summary>Small updates vanish when added to BF16 weights.</details>
