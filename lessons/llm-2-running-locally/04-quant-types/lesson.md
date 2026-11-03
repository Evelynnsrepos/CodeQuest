---
title: Reading quant names (Q4_K_M and friends)
xp: 30
---
# Choosing a quantization

> **Warm-up:** on a model's download page in LM Studio you see `Q3_K_L`, `Q4_K_M`, `Q5_K_M`, `Q6_K`, `Q8_0`. Which would you pick, and why?

The name tells you how the weights were packed:

| Part | Meaning |
|---|---|
| `Q4`, `Q5`, … | roughly how many bits per weight |
| `_0`, `_1` | the old simple block formats (one scale, or scale plus offset, per 32 weights) |
| `_K` | **k-quants**: super-blocks of 256 weights whose per-block scales are themselves quantized. Better quality per bit. |
| `_S`, `_M`, `_L` | small / medium / large: how many sensitive tensors get extra bits. `Q4_K_M` stores most tensors in Q4_K and some important ones (parts of attention and the MLP) in Q6_K. |
| `IQ…` | **i-quants**: cleverer packing for very low bits (`IQ4_XS`, `IQ3_M`, `IQ2_M`). Slower on some hardware. |
| `F16`, `BF16` | not quantized |

Many uploads are made with an **importance matrix** (imatrix): the quantizer runs sample text through the model to find which weights matter most, and spends its rounding error elsewhere. It makes a real difference at 4 bits and below.

Approximate effective bits per weight (they vary a little by model):

```
Q2_K 2.9   Q3_K_M 3.9   IQ4_XS 4.3   Q4_K_M 4.8   Q5_K_M 5.7   Q6_K 6.6   Q8_0 8.5   F16 16
```

Rules of thumb that hold up well:

- **Q4_K_M is the usual sweet spot.** The quality loss from Q8 to Q4_K_M is small; below Q4 it grows fast.
- **A bigger model at Q4 usually beats a smaller model at Q8** of the same file size.
- **Leave room for the context** (next lesson). A 12 GB card can't use a 12 GB file.

## Your quest

`BPW` holds the table above, ordered from best quality to smallest.

1. `file_size_gb(params_billion, quant)`: billions of parameters × bits per weight ÷ 8.
2. `best_quant(params_billion, budget_gb)`: walk `BPW` in order and return the **first** (best) quant whose file size is at most `budget_gb`. Return `None` if none fits.

Dictionaries keep their order, so `for quant in BPW:` walks from best to smallest.

## Review

<details><summary>How many bits per weight does Q4_0 really use, and why not 4?</summary>4.5: each block of 32 weights also stores a 16-bit scale (16 / 32 = 0.5 extra bits).</details>
<details><summary>Why does quantization use small blocks?</summary>So one outlier weight only ruins the precision of its own block, not the whole tensor.</details>
