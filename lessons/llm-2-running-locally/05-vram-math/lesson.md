---
title: VRAM math and the KV cache
xp: 35
---
# Will it fit in 12 GB?

> **Warm-up:** an 8B model at Q4_K_M is a 4.9 GB file. Your GPU has 12 GB. How long a context can you run before it stops fitting?

Three things share your VRAM when a model is loaded:

```
VRAM used ≈ model weights + KV cache + compute buffers (+ your desktop)
```

**The KV cache** (lesson 7 of LLMs 1) stores a key and a value vector for every token, in every layer:

```
KV bytes per token = 2 (K and V) × layers × kv_heads × head_dim × bytes per value
```

For Llama 3.1 8B (`config.json`: 32 layers, 8 KV heads, head dimension 128) with the default 16-bit cache:

```
2 × 32 × 8 × 128 × 2 bytes = 131,072 bytes ≈ 0.13 MB per token
8,192-token context  → 1.07 GB
32,768-token context → 4.3 GB
131,072 (the maximum)→ 17.2 GB   ← more than the whole model!
```

Notice `kv_heads` is 8 while the model has 32 attention heads. That's **grouped-query attention (GQA)**: several query heads share one key/value head, cutting the cache 4×. Almost every modern model uses it, and it's why `num_key_value_heads` is worth checking in `config.json`.

The cache is reserved for the **Context Length you set when loading** the model, whether you use it or not. Ways to make room in LM Studio's load settings:

- a smaller Context Length (the most effective knob)
- **KV cache quantization** to 8-bit (halves the cache; needs Flash Attention turned on in llama.cpp)
- a smaller quant of the weights

Leave about 1 GB for compute buffers, and some more for your desktop. Hyprland plus a browser can easily hold several hundred MB of VRAM; `amdgpu_top` or `radeontop` (both in nixpkgs) show you live usage.

## Your quest

1. `kv_cache_gb(layers, kv_heads, head_dim, context, bytes_per_value)`: the formula above times `context`, divided by 1e9 (`1_000_000_000`).
2. `total_vram_gb(weights_gb, kv_gb)`: weights + KV cache + 1.0 GB overhead.
3. `max_context(weights_gb, layers, kv_heads, head_dim, budget_gb)`: the largest context, in whole multiples of 1,024 tokens, whose total (with a 16-bit cache) stays at or under `budget_gb`. A `while` loop that tries 1,024, 2,048, … is fine.

## Review

<details><summary>What does the _M in Q4_K_M mean?</summary>Medium: some sensitive tensors get more bits (Q6_K) than the rest (Q4_K).</details>
<details><summary>Q8 of a small model or Q4 of a twice-as-big model, at the same file size?</summary>Usually the bigger model at Q4.</details>
<details><summary>What is an importance matrix (imatrix)?</summary>Statistics from running sample text through the model, used during quantization to keep the most important weights more precise.</details>
