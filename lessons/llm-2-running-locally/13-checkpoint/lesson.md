---
title: Checkpoint: will it fit in 12 GB?
minutes: 45
xp: 60
hint: predict, line 1: weights = estimate_params(config) * bpw / 8 / 1000000000
hint: predict, line 2: kv = kv_bytes_per_token(config) * context / 1000000000
hint: predict, line 3: return weights + kv + 1.0 <= budget_gb
hint: By hand: Qwen3-14B has about 14.77 billion parameters and 163,840 KV bytes per token. Llama 3.1 8B: 8.03 billion and 131,072.
---
# Checkpoint

⏱️ About 45 minutes

The Module 2 checkpoint: predict whether a model fits on **your** GPU *before* downloading it. Use 11 GB as the budget: your desktop, browser and driver keep about 1 GB of the 12.

The full estimate, built from this module's lessons:

```
weights GB = estimated parameters × bits per weight ÷ 8 ÷ 1e9
KV GB      = KV bytes per token × context ÷ 1e9
total      = weights + KV + 1 GB compute buffers
```

## 🔬 One prediction by hand (other numbers than the quest)

**Llama 3.1 8B at Q4_K_M (4.8 bpw) with a 32,768-token context.** From lesson 12 you know: 8.03 billion parameters, 131,072 KV bytes per token.

1. **Weights:** 8.03 × 4.8 ÷ 8 = **4.82 GB**. (Working in billions already includes the ÷ 1e9.)
2. **KV cache:** 131,072 × 32,768 = 4,294,967,296 bytes, ÷ 1,000,000,000 = **4.29 GB**.
3. **Total:** 4.82 + 4.29 + 1.0 = **10.11 GB**.
4. **Fits in 11?** 10.11 ≤ 11 → **yes**, `True`.

For the quest you need two more numbers: **Qwen3-14B** has about **14.77 billion** parameters and **163,840** KV bytes per token.

`1e9` (say "one e nine") is how Python can write 10⁹ = 1,000,000,000. You can write either.

## 🐍 Python you need

`estimate_params` and `kv_bytes_per_token` from lesson 12 are given.

| You write | Say it | What it does |
|---|---|---|
| `estimate_params(config) * bpw / 8 / 1000000000` | | parameters × bits ÷ 8 bits per byte ÷ a billion bytes per GB |
| `a <= b` | "a is at most b" | gives `True` or `False` directly |
| `return weights + kv + 1.0 <= budget_gb` | | Python adds the left side first, then compares, and returns the `True`/`False` |

### 👀 Worked example: returning a comparison

```python
def fits_in_bag(book_kg, laptop_kg, bag_max):
    return book_kg + laptop_kg + 0.5 <= bag_max

print(fits_in_bag(1.2, 2.0, 4))   # True: 3.7 <= 4
print(fits_in_bag(1.2, 2.0, 3))   # False: 3.7 > 3
```

You don't need an `if`: the comparison **is** the answer.

## 🎯 Your quest

**Part 1:** `predict(config, bpw, context, budget_gb)`. Replace `return None` with:

1. `weights = estimate_params(config) * bpw / 8 / 1000000000`
2. `kv = kv_bytes_per_token(config) * context / 1000000000`
3. `return weights + kv + 1.0 <= budget_gb`

**Part 2:** **predict by hand first** (a calculator is fine, follow the 4 steps above), and set each to `True` or `False`:

- `fits_a`: Qwen3-14B at Q4_K_M (4.8 bpw) with an 8,192-token context
- `fits_b`: Llama 3.1 8B at Q6_K (6.6 bpw) with a 16,384-token context
- `fits_c`: Qwen3-14B at IQ4_XS (4.3 bpw) with a 4,096-token context

Run your code to see whether your hand predictions were right. If one was wrong, find out which step you misjudged before submitting.

## On your machine (the real checkpoint)

1. Pick a model on Hugging Face you've never used. Open its `config.json` and a GGUF repo for it.
2. Write down your prediction: which quant, which context length, how many GB, does it fit?
3. Load it in LM Studio with those settings and compare against the memory LM Studio reports and `amdgpu_top` shows.

If your prediction was within about 10%, you've passed. If not, find which term you got wrong.

## What's next

LLMs 3 connects your model to tools: tool calling, MCP, `mcp.json`, agents and RAG.
