---
title: Running models on your own PC
xp: 25
---
# Will it fit?

> **Warm-up:** a model is called "Llama 3.1 8B". What does the 8B tell you?

**8B = 8 billion weights.** Each weight is stored with some number of bits:

| Format | Bits per weight | 8B model needs |
|---|---|---|
| FP16 (original) | 16 | 16 GB |
| Q8 | 8.5 | 8.5 GB |
| **Q4_K_M** (the usual choice) | ≈ 4.5 | ≈ 4.5 GB |

So: **GB ≈ billions of parameters × bits ÷ 8**. Add 1–2 GB for the **KV cache** (the model's working memory for the conversation) and overhead. If it fits in your GPU's memory (VRAM) it's fast; if it spills into normal RAM it still works, just much slower.

**Quantization** (fewer bits per weight) loses a little quality; Q4_K_M is usually the sweet spot. Tools: **Ollama** (`ollama run llama3.2`) and **LM Studio** download and run these files (GGUF format).

**Go deeper:** LLMs 2 (Running models locally), Math 5 lessons 12–13.

<div class="quiz" data-answer="0" data-why="8 × 4.5 ÷ 8 = 4.5 GB, plus 1–2 GB for the KV cache."><p><b>Predict first:</b> how many GB is an 8B model at Q4_K_M (4.5 bits per weight)?</p><button>4.5 GB</button><button>8 GB</button><button>36 GB</button></div>

## Your quest

1. `model_gb(params_b, bits)`: `params_b × bits / 8`.
2. `best_fit(params_b, vram_gb, overhead=1.5)`: try the formats `[("FP16", 16), ("Q8", 8.5), ("Q4_K_M", 4.5)]` in that order and return the **first** name whose `model_gb + overhead ≤ vram_gb`; `None` if none fits.

**Remember:** billions × bits ÷ 8 = GB.
