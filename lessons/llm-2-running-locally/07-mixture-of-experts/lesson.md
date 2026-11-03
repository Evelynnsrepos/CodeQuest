---
title: Mixture of Experts (why "30B-A3B" runs fast)
xp: 30
---
# Total vs active parameters

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

## Your quest

1. `size_gb(params_billion, bpw)`: the file size, as in the earlier lessons.
2. `speed_from_ram(active_billion, bpw, ram_bw)`: tokens per second if all active weights are read from RAM: `ram_bw` ÷ (active size in GB).
3. Run it and set `faster` to `"dense"` or `"moe"`: which is faster when both run from RAM at 51 GB/s, a dense 14B or the 30B-A3B, both at Q4_K_M?

## Review

<details><summary>Why is token generation limited by memory bandwidth?</summary>Every weight has to be read once per generated token, and moving that data takes longer than the arithmetic.</details>
<details><summary>What does the GPU Offload slider in LM Studio control?</summary>How many layers live in VRAM; the rest run on the CPU from system RAM, which is much slower.</details>
