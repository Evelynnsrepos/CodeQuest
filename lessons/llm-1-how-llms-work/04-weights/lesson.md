---
title: Weights are just numbers
minutes: 25
xp: 20
hint: neuron, inside the loop: total = total + inputs[i] * weights[i]
hint: neuron, last line: return total + bias
hint: model_size_gb: return params_billion * bits / 8
hint: 8B in FP16 is 16 GB. 16 is more than 12, so: fp16_8b_fits_in_12gb = False
---
# Weights and parameters

⏱️ About 25 minutes

> **Warm-up:** when a model is called "8B", 8 billion *what*? And what is actually inside the 5 GB file you downloaded in LM Studio?

A model file is almost entirely a huge list of numbers called **weights** or **parameters**. "8B" means 8 billion of them. Training (Module 5) is the process that finds good values for them; **inference**, using the model, just does arithmetic with them.

The basic building block is a weighted sum. One "neuron" multiplies each input by a weight, adds them up, and adds a **bias**:

```
inputs   x = [2.0, 3.0]
weights  w = [0.5, -1.0]
bias     b = 0.25
output = 2.0·0.5 + 3.0·(−1.0) + 0.25 = −1.75
```

An LLM does this billions of times per token, organised into big grids of weights called **matrices** (Module 4 covers the math). The weights don't store sentences or facts in readable form. Knowledge is smeared across all of them as patterns.

**How big is the file?** Each weight is stored with some number of **bits**:

| Format | Bits per weight | 8B model |
|---|---|---|
| FP32 (training) | 32 | 32 GB |
| FP16 / BF16 (released models) | 16 | 16 GB |
| Q8_0 | ~8.5 | ~8.5 GB |
| Q4_K_M (LM Studio's usual pick) | ~4.8 | ~4.8 GB |

So: **gigabytes ≈ billions of parameters × bits ÷ 8** (8 bits = 1 byte). Shrinking the bits is called **quantization**, and Module 2 is all about it. To *run* a model you also need memory for the context (the KV cache, Module 2), so the file must be noticeably smaller than your 12 GB of VRAM.

## 🔬 Take the two formulas apart

**The neuron:** `output = x₁·w₁ + x₂·w₂ + b`

| Piece | Say it | Means | Example |
|---|---|---|---|
| `x₁`, `x₂` | "x one, x two" | the inputs. The small number below is just a label: the first one, the second one. | 2.0 and 3.0 |
| `w₁`, `w₂` | "w one, w two" | the weights, one for each input | 0.5 and −1.0 |
| `·` | "times" | multiply (the same as ×) | 2.0 · 0.5 = 1.0 |
| `b` | "b" | the bias: one extra number added at the end | 0.25 |

So: 1.0 + (3.0 · −1.0) + 0.25 = 1.0 − 3.0 + 0.25 = **−1.75**. A minus times a plus gives a minus.

**The file size:** `GB ≈ billions of parameters × bits ÷ 8`

| Piece | Means | Example |
|---|---|---|
| `≈` | "about equal": the real file is a little bigger | |
| billions of parameters | the "8" in "8B" | 8 |
| bits | bits per weight, from the table | 16 |
| `÷ 8` | 8 bits make 1 byte | 8 × 16 ÷ 8 = **16 GB** |

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `range(len(inputs))` | "range of length of inputs" | the positions 0, 1, … up to the last one |
| `inputs[i]` | "inputs at i" | the input at position `i` |
| `weights[i]` | "weights at i" | the matching weight, same position |
| `total = total + x` | "total becomes total plus x" | a **running total**: start at 0, keep adding |
| `*`, `/` | "times", "divided by" | multiply and divide |
| `return total + bias` | | adds the bias and gives back the answer |
| `True` / `False` | | yes / no, no quotes |

### 👀 Worked example: a shopping bill

Prices and amounts in two lists, matched by position, plus a delivery fee at the end. That's the neuron's shape: multiply matching numbers, add up, add one extra.

```python
def bill(prices, amounts, delivery):
    total = 0
    for i in range(len(prices)):
        total = total + prices[i] * amounts[i]
    return total + delivery

print(bill([2, 5], [3, 1], 4))   # 15
```

1. `total` = 0. `len(prices)` is 2, so `i` is 0, then 1.
2. `i` = 0: 0 + 2 × 3 = **6**.
3. `i` = 1: 6 + 5 × 1 = **11**.
4. After the loop: 11 + 4 = **15**.

## 🎯 Your quest

**Part 1:** `neuron(inputs, weights, bias)`. The loop line is already there. Replace the `pass` line and the return line, so the function reads:

1. `total = 0`
2. `for i in range(len(inputs)):`
3. `    total = total + inputs[i] * weights[i]`
4. `return total + bias`

**Part 2:** `model_size_gb(params_billion, bits)`. Replace `return 0` with:

- `return params_billion * bits / 8`

**Part 3:** press **Run**. An 8B model in FP16 is how many GB? Does that fit in 12 GB? Set `fp16_8b_fits_in_12gb` to `True` or `False`.

## Review

<details><summary>In BPE, what gets merged at each step?</summary>The most frequent pair of neighbouring tokens in the training text becomes one new token.</details>
<details><summary>Why does a model need its exact own tokenizer?</summary>The model learned what each token ID means. A different tokenizer gives different IDs for the same text, so the input would be gibberish to it.</details>
