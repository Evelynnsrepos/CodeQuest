---
title: How fast will it run? Bandwidth and offloading
minutes: 35
xp: 35
hint: tokens_per_second: seconds = gpu_gb / gpu_bw + cpu_gb / cpu_bw, then return 1 / seconds
hint: layers_on_gpu: per_layer = model_gb / layers, then fit = int(vram_free_gb / per_layer)
hint: Then: if fit > layers: fit = layers. Last line: return fit
---
# Tokens per second

⏱️ About 35 minutes

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

## 🔬 Take the formulas apart

**Bandwidth** is how many GB the memory can move per second, written **GB/s** ("gigabytes per second"). 384 GB/s means 384 GB every second.

**Time to read some data** = how much ÷ how fast. Reading a 4.9 GB model at 384 GB/s takes 4.9 ÷ 384 = **0.0128 seconds**.

**Tokens per second** is the other way round: how many tokens fit into one second = 1 ÷ (seconds per token). 1 ÷ 0.0128 ≈ **78**.

With offloading, the two parts are read one after the other, so their times **add up**:

<div class="formula">seconds per token = <span class="k1">GPU GB ÷ GPU bandwidth</span> + <span class="k2">CPU GB ÷ RAM bandwidth</span></div>

Example: 10 GB on the GPU (384 GB/s) and 4.3 GB on the CPU (51 GB/s):

- GPU part: 10 ÷ 384 = 0.026 s
- CPU part: 4.3 ÷ 51 = 0.084 s, three times the GPU part, for less than half the data
- total: 0.11 s per token → 1 ÷ 0.11 ≈ **9 tokens/s**

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `gpu_gb / gpu_bw` | | seconds for the GPU part |
| `1 / seconds` | "one divided by seconds" | tokens per second |
| `int(9.7)` | "int of 9.7" | cuts off the decimals: `9`. It does **not** round up. You can't put 0.7 of a layer on the GPU. |
| `if fit > layers:` | | can't put more layers on the GPU than the model has |

### 👀 Worked example: how many full boxes fit in the van?

```python
def boxes_in_van(total_kg, boxes, van_kg):
    per_box = total_kg / boxes
    fit = int(van_kg / per_box)
    if fit > boxes:
        fit = boxes
    return fit

print(boxes_in_van(100, 10, 35))    # 3
print(boxes_in_van(100, 10, 500))   # 10
```

1. Each box is 100 ÷ 10 = 10 kg.
2. 35 ÷ 10 = 3.5 → `int` → **3** whole boxes.
3. With a 500 kg van: 500 ÷ 10 = 50, but there are only 10 boxes, so **10**.

## 🎯 Your quest

**Part 1:** `tokens_per_second(gpu_gb, cpu_gb, gpu_bw, cpu_bw)`. Replace `return 0` with:

1. `seconds = gpu_gb / gpu_bw + cpu_gb / cpu_bw`
2. `return 1 / seconds`

**Part 2:** `layers_on_gpu(model_gb, layers, vram_free_gb)`. Replace `return 0` with:

1. `per_layer = model_gb / layers`
2. `fit = int(vram_free_gb / per_layer)`
3. `if fit > layers:`
4. `    fit = layers`
5. `return fit`

## Review

<details><summary>Write the KV cache formula.</summary>2 × layers × kv_heads × head_dim × bytes per value, per token.</details>
<details><summary>What is grouped-query attention and why does it matter locally?</summary>Several query heads share one key/value head, so the KV cache is several times smaller and long contexts fit in less VRAM.</details>
<details><summary>Which LM Studio load setting changes VRAM use the most?</summary>Context Length, because the KV cache is reserved for all of it.</details>
