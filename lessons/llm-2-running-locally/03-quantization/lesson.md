---
title: Quantization, by hand
xp: 35
---
# Shrinking weights to 4 bits

> **Warm-up:** a weight like `0.0371` is stored in 16 bits. If you only had 4 bits (16 possible values), how would you store it?

**Quantization** stores each weight with fewer bits. 4 bits allow only 16 different whole numbers, −8 to 7. The trick is to give every small **block** of weights (32 in llama.cpp) its own **scale**:

```
block:   [0.12, -0.40, 0.05, 0.33]          (real blocks have 32 weights)
scale  = max(|w|) / 7 = 0.40 / 7 = 0.0571
q      = round(w / scale), clamped to −8…7
       = [2, -7, 1, 6]                       ← stored with 4 bits each
dequantized = q × scale
       = [0.114, -0.400, 0.057, 0.343]      ← what the model computes with
```

The block stores 32 small integers plus one 16-bit scale, so each weight costs 4 + 16/32 = **4.5 bits**. That's llama.cpp's `Q4_0`. Every weight now has a small **rounding error**, and quality drops a little. Quantization works because LLMs are surprisingly tolerant of this noise, down to about 4 bits. Below that, quality falls off quickly, and small models suffer more than big ones.

Why blocks? One scale for the whole tensor would be ruined by a single large weight (an **outlier**): every other weight would round to 0. Small blocks keep the damage local.

## Python you need

`round(x)` rounds to the nearest whole number. `max(-8, min(7, q))` clamps `q` into −8…7. `abs(x)` is the absolute value.

## Your quest

1. `quantize(block)`: return `(scale, qs)`, where `scale = max(|w|) / 7` and `qs` is the list of clamped, rounded values. If every weight is 0, use `scale = 1.0` to avoid dividing by zero.
2. `dequantize(scale, qs)`: return the list `q × scale`.
3. Run it and look at the error for the block with an outlier. Set `outlier_hurts` to `True` or `False`: did the small weights in that block survive?

## Review

<details><summary>What are the first four bytes of a GGUF file?</summary>The magic letters "GGUF".</details>
<details><summary>Name three things GGUF metadata stores besides the weights.</summary>For example: architecture, layer count, context length, tokenizer vocabulary and merges, chat template, quantization type.</details>
