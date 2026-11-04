---
title: Checkpoint: will it fit in 12 GB?
xp: 60
---
# Checkpoint

The Module 2 checkpoint: predict whether a model fits on **your** GPU *before* downloading it. Use 11 GB as the budget: your desktop, browser and driver keep about 1 GB of the 12.

The full estimate, built from this module's lessons:

```
weights GB = estimated parameters × bits per weight ÷ 8 ÷ 1e9
KV GB      = KV bytes per token × context ÷ 1e9
total      = weights + KV + 1 GB compute buffers
```

## Your quest

`estimate_params` and `kv_bytes_per_token` from the last lesson are given.

1. Write `predict(config, bpw, context, budget_gb)`: return `True` if the total fits in `budget_gb`, else `False`.
2. Then **predict by hand first** (a calculator is fine), and set:
   - `fits_a`: Qwen3-14B at Q4_K_M (4.8 bpw) with an 8,192-token context
   - `fits_b`: Llama 3.1 8B at Q6_K (6.6 bpw) with a 16,384-token context
   - `fits_c`: Qwen3-14B at IQ4_XS (4.3 bpw) with a 4,096-token context

Run your code to see whether your hand predictions were right. If one was wrong, find out which part you misjudged before submitting.

## On your machine (the real checkpoint)

1. Pick a model on Hugging Face you've never used. Open its `config.json` and a GGUF repo for it.
2. Write down your prediction: which quant, which context length, how many GB, does it fit?
3. Load it in LM Studio with those settings and compare against the memory LM Studio reports and `amdgpu_top` shows.

If your prediction was within about 10%, you've passed. If not, find which term you got wrong.

## What's next

LLMs 3 connects your model to tools: tool calling, MCP, `mcp.json`, agents and RAG.
