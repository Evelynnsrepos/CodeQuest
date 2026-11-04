---
title: Weights are just numbers
xp: 20
---
# Weights and parameters

> **Warm-up:** when a model is called "8B", 8 billion *what*? And what is actually inside the 5 GB file you downloaded in LM Studio?

A model file is almost entirely a huge list of numbers called **weights** or **parameters**. "8B" means 8 billion of them. Training (Module 5) is the process that finds good values for them; **inference**, using the model, just does arithmetic with them.

The basic building block is a weighted sum. One "neuron" multiplies each input by a weight, adds them up, and adds a **bias**:

```
inputs   x = [2.0, 3.0]
weights  w = [0.5, -1.0]
bias     b = 0.25
output = 2.0·0.5 + 3.0·(−1.0) + 0.25 = −1.75
```

An LLM does this billions of times per token, organised into big grids of weights called **matrices** (Module 4 covers the math). The weights don't store sentences or facts in readable form. Knowledge is smeared across all of them as patterns.

**How big is the file?** Each weight is stored with some number of **bits**:

| Format | Bits per weight | 8B model |
|---|---|---|
| FP32 (training) | 32 | 32 GB |
| FP16 / BF16 (released models) | 16 | 16 GB |
| Q8_0 | ~8.5 | ~8.5 GB |
| Q4_K_M (LM Studio's usual pick) | ~4.8 | ~4.8 GB |

So: **gigabytes ≈ billions of parameters × bits ÷ 8** (8 bits = 1 byte). Shrinking the bits is called **quantization**, and Module 2 is all about it. To *run* a model you also need memory for the context (the KV cache, Module 2), so the file must be noticeably smaller than your 12 GB of VRAM.

## Your quest

1. Write `neuron(inputs, weights, bias)`: multiply each input by its weight, add them all up, add the bias, return the result. `zip(inputs, weights)` gives you matching pairs.
2. Write `model_size_gb(params_billion, bits)` using the formula above.
3. Set `fp16_8b_fits_in_12gb` to `True` or `False`.

## Review

<details><summary>In BPE, what gets merged at each step?</summary>The most frequent pair of neighbouring tokens in the training text becomes one new token.</details>
<details><summary>Why does a model need its exact own tokenizer?</summary>The model learned what each token ID means. A different tokenizer gives different IDs for the same text, so the input would be gibberish to it.</details>
