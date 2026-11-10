---
title: Will this model fit on my GPU?
minutes: 25
xp: 25
hint: model_gb: params_b * bits / 8 (8 bits make one byte).
hint: needed = model_gb(params_b, bits) + overhead, then if needed <= vram_gb: return name.
distractor: return params_b * bits * 8
distractor: if needed >= vram_gb:
---
# Running models on your own computer

⏱️ About 25 minutes · 🧩 4 gaps, 2 decoys

> **Warm-up:** your graphics card (GPU) has 12 GB of memory. Can it run an "8B" model?

**In one sentence:** a model's size in GB is about **parameters × bits per parameter ÷ 8**, and **quantization** (storing each number with fewer bits) makes it fit.

## 💡 The idea

**8B** means 8 **b**illion parameters: the numbers the model learned. Each one is stored with some number of **bits**:

- **FP16**: 16 bits each, full quality.
- **Q8**: about 8.5 bits, almost no quality loss.
- **Q4_K_M**: about 4.5 bits, a small quality loss, but a quarter of the size. The usual choice in LM Studio.

The model has to fit in your GPU's memory (**VRAM**), plus about 1.5 GB extra (the **overhead**) for the conversation itself.

## 🔢 The maths, step by step

8 **bits** make 1 **byte**. So: GB = billions of parameters × bits ÷ 8.

An 8B model on your 12 GB card:

1. **FP16:** 8 × 16 = 128, ÷ 8 = **16 GB**. Plus 1.5 = 17.5. Is 17.5 ≤ 12? No. ✗
2. **Q8:** 8 × 8.5 = 68, ÷ 8 = **8.5 GB**. Plus 1.5 = 10. Is 10 ≤ 12? Yes! ✓ → use **Q8**.

New symbol: **≤** means "is smaller than or equal to". In Python it's written `<=`. (And `>=` means "bigger than or equal to", that's a decoy here.)

A 70B model: even at Q4_K_M, 70 × 4.5 ÷ 8 ≈ 39.4 GB. Nothing fits on 12 GB → no answer (`None`).

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `[("FP16", 16), ...]` | a list of pairs | each pair: a name and its bits |
| `for name, bits in FORMATS:` | "for each name and bits" | unpacks each pair into two boxes |
| `overhead=1.5` | "overhead, default 1.5" | if nobody says otherwise, it's 1.5 |
| `<=` | "smaller than or equal to" | `10 <= 12` is `True` |
| `return name` inside the loop | | stops at the **first** format that fits. FP16 is tried first because it's the best quality. |

## 🧩 Your puzzle

1. `model_gb`: params × bits **÷ 8** (decoy: × 8).
2. `needed`: the model's size plus the overhead.
3. "Does it fit?": needed **≤** your VRAM.
4. If it fits, give back this format's name.

Run it: `16.0 Q8 None`.

**Remember:** GB ≈ params × bits ÷ 8, plus a bit for the chat.
