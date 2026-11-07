---
title: Mixture of Experts (why "30B-A3B" runs fast)
minutes: 25
xp: 30
hint: size_gb: return params_billion * bpw / 8
hint: speed_from_ram: return ram_bw / size_gb(active_billion, bpw)
hint: Press Run and compare the two tok/s numbers. The bigger number wins: faster = "moe" or "dense"
---
# Total vs active parameters

⏱️ About 25 minutes

> **Warm-up:** `Qwen3-30B-A3B` has 30 billion parameters. Based on the last lesson, it should run slowly from RAM. Yet people run it at 20+ tokens/s on machines like yours. What could "A3B" mean?

In a normal (**dense**) model, every token goes through every weight. A **Mixture of Experts (MoE)** model replaces each MLP block with many smaller MLPs, the **experts** (Qwen3-30B-A3B has 128 per layer), plus a tiny **router** that picks a few of them (8 here) for each token. The rest of the experts sit idle for that token.

So an MoE model has two sizes:

| | Qwen3-30B-A3B | gpt-oss-20b |
|---|---|---|
| **Total** parameters (memory you need) | 30.5B | 21B |
| **Active** parameters per token (what you read per token, so speed) | 3.3B | 3.6B |

- **Memory** depends on the **total**: all experts must be loaded somewhere, since any token might need any of them.
- **Speed** depends on the **active** part: per token you only read the chosen experts plus the shared layers.
- **Quality** sits in between: roughly like a dense model somewhat bigger than the active size, often much better.

That makes MoE models a great fit for **12 GB VRAM + 32 GB RAM**: the attention layers and KV cache go on the GPU, the big expert weights stay in system RAM, and since only ~3B parameters are read per token, even RAM bandwidth gives usable speed. Recent llama.cpp builds have options to keep expert tensors on the CPU (`--n-cpu-moe`, `--override-tensor`), and LM Studio has exposed similar settings in its load options. Names change between versions, so look for "MoE" or "experts" in your load settings.

## 🔬 The two formulas, with numbers

**Size** (what you must store): billions × bits per weight ÷ 8. Qwen3-30B-A3B at Q4_K_M: 30.5 × 4.8 ÷ 8 = **18.3 GB**. Too big for 12 GB VRAM alone, but fine in 32 GB RAM.

**Speed from RAM** (lesson 6): bandwidth ÷ GB read per token. Per token, only the **active** 3.3B are read: 3.3 × 4.8 ÷ 8 = 1.98 GB. 51 ÷ 1.98 ≈ **26 tokens/s**.

A dense 14B reads all of it every token: 14 × 4.8 ÷ 8 = 8.4 GB. 51 ÷ 8.4 ≈ **6 tokens/s**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `params_billion * bpw / 8` | | the size formula |
| `size_gb(active_billion, bpw)` | | calls your first function from inside the second one, with the **active** size |
| `ram_bw / size_gb(...)` | | bandwidth divided by that size |
| `"moe"` | | text in quotes |

### 👀 Worked example: a function that uses another function

```python
def area(width, height):
    return width * height

def paint_tins(width, height, per_tin):
    return area(width, height) / per_tin

print(paint_tins(4, 3, 6))   # 2.0
```

`paint_tins(4, 3, 6)` first runs `area(4, 3)` = 12, then 12 ÷ 6 = **2.0** tins. `speed_from_ram` has the same shape.

## 🎯 Your quest

1. In `size_gb`, replace `return 0` with:
   - `return params_billion * bpw / 8`
2. In `speed_from_ram`, replace `return 0` with:
   - `return ram_bw / size_gb(active_billion, bpw)`
3. Press **Run** and compare the two "from RAM" speeds. Set `faster` to `"dense"` or `"moe"`.

## Review

<details><summary>Why is token generation limited by memory bandwidth?</summary>Every weight has to be read once per generated token, and moving that data takes longer than the arithmetic.</details>
<details><summary>What does the GPU Offload slider in LM Studio control?</summary>How many layers live in VRAM; the rest run on the CPU from system RAM, which is much slower.</details>
