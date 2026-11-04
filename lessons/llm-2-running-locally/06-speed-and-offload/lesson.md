---
title: How fast will it run? Bandwidth and offloading
xp: 35
---
# Tokens per second

> **Warm-up:** your GPU can do tens of trillions of operations per second. Why does an 8B model then only produce something like 50–80 tokens per second?

Because generating a token isn't limited by math, it's limited by **memory bandwidth**. For every single new token, the GPU has to read **every weight once** from VRAM. The arithmetic is quick; moving gigabytes is not. So:

```
tokens/s (upper bound) ≈ memory bandwidth ÷ bytes read per token ≈ bandwidth ÷ model file size
```

| Memory | Typical bandwidth |
|---|---|
| RX 6700 XT / 6750 XT (12 GB) | ~384 GB/s |
| RX 7700 XT (12 GB) | ~432 GB/s |
| DDR4-3200, dual channel | ~51 GB/s |
| DDR5-6000, dual channel | ~96 GB/s |

Look up your own card's number (`lspci | grep VGA` names it; the spec sheet lists "memory bandwidth"). Real speeds land at roughly 60–80% of the upper bound.

An 8B Q4_K_M (4.9 GB) on a 384 GB/s card: 384 ÷ 4.9 ≈ 78 tokens/s at best.

**Prompt processing is different.** Reading your prompt handles many tokens per weight read, so it's limited by compute instead, and is far faster per token (hundreds to thousands of tokens/s).

**Offloading.** When a model doesn't fit in VRAM, llama.cpp can keep some layers on the GPU and run the rest from system RAM on the CPU. In LM Studio that's the **GPU Offload** slider (number of layers). Every token must then also stream the CPU part from slow RAM:

```
seconds per token = GPU GB ÷ GPU bandwidth + CPU GB ÷ RAM bandwidth
```

Even a small CPU share dominates, because RAM is 4–8× slower. That's why "it fits if I offload half" usually means "it runs at a third of the speed".

## Your quest

1. `tokens_per_second(gpu_gb, cpu_gb, gpu_bw, cpu_bw)`: 1 divided by the seconds per token above. Bandwidths are in GB/s.
2. `layers_on_gpu(model_gb, layers, vram_free_gb)`: each layer is `model_gb / layers` GB. Return how many whole layers fit in `vram_free_gb`, but never more than `layers`. `int(x)` cuts off the decimals.

## Review

<details><summary>Write the KV cache formula.</summary>2 × layers × kv_heads × head_dim × bytes per value, per token.</details>
<details><summary>What is grouped-query attention and why does it matter locally?</summary>Several query heads share one key/value head, so the KV cache is several times smaller and long contexts fit in less VRAM.</details>
<details><summary>Which LM Studio load setting changes VRAM use the most?</summary>Context Length, because the KV cache is reserved for all of it.</details>
