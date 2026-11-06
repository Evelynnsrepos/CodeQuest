---
title: Running models on your own PC
minutes: 25
xp: 25
hint: model_gb has one line: return params_b * bits / 8
hint: best_fit: for name, bits in FORMATS: and inside it needed = model_gb(params_b, bits) + overhead
hint: Then if needed <= vram_gb: return name (12 spaces). After the loop, at 4 spaces: return None
---
# Will it fit?

⏱️ About 25 minutes · two functions

> **Warm-up:** a model is called "Llama 3.1 8B". What does the 8B tell you?

**In one sentence:** a model's size in GB is about **billions of weights × bits per weight ÷ 8**, and it runs fast only if that (plus a little extra) fits into your graphics card's memory.

## 💡 The idea in plain words

**8B = 8 billion weights** (the adjustable numbers from lesson 06). Every weight is stored in the computer's memory, and how much memory it takes depends on how precisely it's stored.

**Quantization** means storing each weight with fewer bits. It loses a little quality but makes the model much smaller. **Q4_K_M** is usually the sweet spot.

| Format | Bits per weight | 8B model needs |
|---|---|---|
| FP16 (original) | 16 | 16 GB |
| Q8 | 8.5 | 8.5 GB |
| **Q4_K_M** (the usual choice) | ≈ 4.5 | ≈ 4.5 GB |

Add 1–2 GB for the **KV cache** (the model's working memory for the conversation) and other overhead. If it all fits in your GPU's memory (**VRAM**: your graphics card has 12 GB) it's fast; if it spills into normal RAM it still works, just much slower.

Tools: **LM Studio** and **Ollama** (`ollama run llama3.2`) download and run these model files (GGUF format).

## 🔢 The maths, one step at a time

### Bits and bytes

- A **bit** is the smallest piece of computer memory: one 0 or 1.
- **8 bits = 1 byte**. So to turn bits into bytes, **divide by 8**.
- **1 GB** (gigabyte) = 1 billion bytes.

### Why "billions × bits ÷ 8" gives GB

For 8 billion weights at 16 bits each:

1. bits per weight × number of weights: 16 × 8 billion = 128 billion bits
2. ÷ 8 to get bytes: 128 ÷ 8 = 16 billion bytes
3. 1 billion bytes is 1 GB, so that's **16 GB**

Because "billion" appears in both the weights and in GB, you can leave it out and just use the number in front of the B:

<div class="formula"><span class="k1">GB</span> = <span class="k2">params in billions</span> × <span class="k3">bits</span> ÷ <span class="k4">8</span></div>

| Piece | Means | 8B at Q4_K_M |
|---|---|---|
| <span class="k2">params in billions</span> | the number before the B in the name | 8 |
| <span class="k3">bits</span> | bits per weight of the format | 4.5 |
| <span class="k4">÷ 8</span> | bits → bytes | |
| <span class="k1">GB</span> | memory the weights need | 8 × 4.5 ÷ 8 = **4.5** |

### Does it fit?

Model GB + overhead ≤ VRAM. The sign **≤** means "smaller than or equal to" (it fits exactly too).

8B on your 12 GB card, overhead 1.5 GB:

- FP16: 16 + 1.5 = 17.5. Is 17.5 ≤ 12? No.
- Q8: 8.5 + 1.5 = 10. Is 10 ≤ 12? **Yes** → use Q8 (the best quality that fits).

<div class="quiz" data-answer="0" data-why="8 × 4.5 ÷ 8 = 4.5 GB, plus 1–2 GB for the KV cache."><p><b>Predict first:</b> how many GB is an 8B model at Q4_K_M (4.5 bits per weight)?</p><button>4.5 GB</button><button>8 GB</button><button>36 GB</button></div>

**Go deeper:** LLMs 2 (Running models locally), Math 5 lessons 12–13.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `("Q8", 8.5)` | "a pair: Q8 and 8.5" | round brackets hold a fixed group of values, called a **tuple** |
| `FORMATS = [("FP16", 16), ...]` | "a list of pairs" | the list of formats, already in your editor |
| `for name, bits in FORMATS:` | "for each name and bits in FORMATS" | each pair is unpacked into two boxes: 1st turn `name = "FP16"`, `bits = 16`; 2nd turn `"Q8"`, `8.5`; … |
| `a <= b` | "a less than or equal to b" | `True` if a is smaller than b or the same |
| `overhead=1.5` in the `def` line | "overhead, default 1.5" | an input with a **default**: if the caller doesn't give one, it's 1.5 |
| `return` inside a loop | | stops the loop *and* the function: the first match wins |

### 👀 Worked example: the first shirt that fits

```python
SIZES = [("S", 90), ("M", 100), ("L", 110)]


def first_fit(chest):
    for name, width in SIZES:
        if chest <= width:
            return name
    return None
```

`first_fit(95)`:

1. `"S"`, 90: is 95 ≤ 90? No, keep going.
2. `"M"`, 100: is 95 ≤ 100? Yes → give back `"M"`, stop.

`first_fit(120)`: no size is wide enough, the loop ends, the last line gives back `None`.

Notice where `return None` sits: at 4 spaces, **after** the loop, not inside it. Inside, it would give up after the first size.

## 🎯 Your quest

1. `model_gb(params_b, bits)`: one line: `return params_b * bits / 8`.
2. `best_fit(params_b, vram_gb, overhead=1.5)`: like `first_fit`, trying the formats in order (best quality first):
   - `for name, bits in FORMATS:`
   - inside: `needed = model_gb(params_b, bits) + overhead`
   - inside: `if needed <= vram_gb:` → `return name`
   - after the loop: `return None`

`best_fit(8, 12)` should give `"Q8"`, like the calculation above.

**Remember:** billions × bits ÷ 8 = GB.
