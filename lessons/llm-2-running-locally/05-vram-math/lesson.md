---
title: VRAM math and the KV cache
minutes: 45
xp: 35
hint: kv_cache_gb: per_token = 2 * layers * kv_heads * head_dim * bytes_per_value, then return per_token * context / 1000000000
hint: total_vram_gb: return weights_gb + kv_gb + 1.0
hint: max_context: while total_vram_gb(weights_gb, kv_cache_gb(layers, kv_heads, head_dim, context + 1024, 2)) <= budget_gb:
hint: Inside the while loop: context = context + 1024. After it: return context
---
# Will it fit in 12 GB?

⏱️ About 45 minutes

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

## 🔬 Take the KV formula apart

<div class="formula">KV bytes per token = <span class="k1">2</span> × <span class="k2">layers</span> × <span class="k3">kv_heads</span> × <span class="k4">head_dim</span> × <span class="k5">bytes per value</span></div>

| Piece | Means | Llama 3.1 8B |
|---|---|---|
| <span class="k1">2</span> | one **K**ey and one **V**alue vector per token | 2 |
| <span class="k2">layers</span> | every layer keeps its own cache | 32 |
| <span class="k3">kv_heads</span> | how many key/value heads each layer has | 8 |
| <span class="k4">head_dim</span> | how many numbers in each head's vector | 128 |
| <span class="k5">bytes per value</span> | 16-bit = 2 bytes, 8-bit = 1 byte | 2 |

Step by step: 2 × 32 = 64, × 8 = 512, × 128 = 65,536, × 2 = **131,072 bytes** per token.

Then, for the whole context: × 8,192 tokens = 1,073,741,824 bytes. A **gigabyte** (GB) here is 1,000,000,000 bytes (in maths: 10⁹, "ten to the ninth", a 1 with nine zeros). 1,073,741,824 ÷ 1,000,000,000 ≈ **1.07 GB**.

Total VRAM: 4.9 (weights) + 1.07 (cache) + 1.0 (overhead) = **6.97 GB**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `2 * layers * kv_heads` | | multiplies everything, left to right |
| `1000000000` | "one billion" | 10⁹. No commas in Python numbers. |
| `while condition:` | "while … is true" | repeats as long as the condition holds, checking again before each round |
| `context + 1024` | | "the next size up": try one more step of 1,024 tokens |
| `context = context + 1024` | | actually take that step |

### 👀 Worked example: how many books fit on the shelf?

Each book is 3 cm, the shelf is 10 cm. Add books one at a time **while the next one still fits**:

```python
books = 0
while (books + 1) * 3 <= 10:
    books = books + 1
print(books)   # 3
```

| books | next would be | ≤ 10? |
|---|---|---|
| 0 | 1 × 3 = 3 | yes → books = 1 |
| 1 | 2 × 3 = 6 | yes → books = 2 |
| 2 | 3 × 3 = 9 | yes → books = 3 |
| 3 | 4 × 3 = 12 | **no** → stop |

The trick: test the **next** size, and only step up if it fits. Then you never go over. `max_context` does the same with steps of 1,024 tokens.

## 🎯 Your quest

**Part 1:** `kv_cache_gb(layers, kv_heads, head_dim, context, bytes_per_value)`. Replace `return 0` with:

1. `per_token = 2 * layers * kv_heads * head_dim * bytes_per_value`
2. `return per_token * context / 1000000000`

**Part 2:** `total_vram_gb(weights_gb, kv_gb)`. Replace `return 0` with:

- `return weights_gb + kv_gb + 1.0`

**Part 3:** `max_context(weights_gb, layers, kv_heads, head_dim, budget_gb)`. Between `context = 0` and `return context`:

1. `while total_vram_gb(weights_gb, kv_cache_gb(layers, kv_heads, head_dim, context + 1024, 2)) <= budget_gb:`
2. `    context = context + 1024`

Line 1 reads from the inside out: the KV cache for one step more, then the total with it, then "does that still fit?".

## Review

<details><summary>What does the _M in Q4_K_M mean?</summary>Medium: some sensitive tensors get more bits (Q6_K) than the rest (Q4_K).</details>
<details><summary>Q8 of a small model or Q4 of a twice-as-big model, at the same file size?</summary>Usually the bigger model at Q4.</details>
<details><summary>What is an importance matrix (imatrix)?</summary>Statistics from running sample text through the model, used during quantization to keep the most important weights more precise.</details>
<details><summary>Why does max_context test context + 1024 and not context?</summary>So it only steps up when the next size still fits. It never goes over the budget.</details>
