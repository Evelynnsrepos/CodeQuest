---
title: The GPT training recipe
minutes: 40
xp: 50
hint: initial_loss: return math.log(vocab)
hint: lr_at: if step < warmup: return max_lr * (step + 1) / warmup. Then if step >= total: return min_lr
hint: Otherwise: r = (step - warmup) / (total - warmup), return min_lr + 0.5 * (1 + math.cos(math.pi * r)) * (max_lr - min_lr)
---
# How a GPT is actually trained

⏱️ About 40 minutes

> **Warm-up:** before any training, the model's weights are random. What loss should you expect on the very first batch, and why is that a useful check?

A randomly initialized model spreads its probability roughly evenly over the vocabulary, so the cross-entropy loss is about `−ln(1/V) = ln V`. For GPT-2's 50,257 tokens that's **10.82**. If your first loss is far from it (say 40), the initialization is broken. Karpathy calls this the first sanity check.

The standard recipe (GPT-3 paper, nanoGPT, Llama):

- **AdamW** (LLMs 5) with `β1 = 0.9, β2 = 0.95`, **weight decay 0.1** on the matrices (not on norms and biases).
- **Gradient clipping**: if the gradient's total length exceeds 1.0, scale it down to 1.0. It stops one bad batch from wrecking the run.
- **bf16 mixed precision**: compute in 16-bit, keep master weights in 32-bit.
- **Big batches** via gradient accumulation (LLMs 6): GPT-3 used about 0.5 M tokens per step at 125M size.
- **Learning-rate schedule**: a linear **warmup** (from near 0 to `max_lr` over the first steps, because Adam's moment estimates are unreliable at the start), then **cosine decay** down to `min_lr` (often `max_lr / 10`), then stay there.

```
step < warmup:           lr = max_lr · (step + 1) / warmup
step ≥ total:            lr = min_lr
otherwise:               r  = (step − warmup) / (total − warmup)
                         lr = min_lr + 0.5 · (1 + cos(π·r)) · (max_lr − min_lr)
```

Newer runs often use **WSD** (warmup, stable, decay: a flat learning rate then a short final decay), which makes it easy to continue training. Both are in use; cosine is the classic.

**On your machine:** nanoGPT's `shakespeare_char` config trains a small GPT in minutes on a GPU. On AMD that needs the ROCm build of PyTorch, and official ROCm support for consumer cards varies by card and version (check the ROCm compatibility table; this changes often). It also runs on CPU, just slowly.

## 🔬 Take the formulas apart

**The starting loss.** A fresh model guesses about equally: each of V tokens gets probability 1/V. The loss is the surprise of the right one (LLMs 4, lesson 10):

<div class="formula">−log(1/V) = <span class="k1">log V</span></div>
Why? log(1/V) = −log V (dividing turns into a minus inside a log), and the minus in front flips it back. For GPT-2, V = 50,257: log 50,257 ≈ **10.825**. If your first loss is much higher, something is broken.

**The schedule** (like LLMs 5 lesson 9, but it ends at a floor `min_lr` instead of 0):
<div class="formula">lr = <span class="k1">min_lr</span> + <span class="k2">0.5 · (1 + cos(π·r))</span> · <span class="k3">(max_lr − min_lr)</span></div>
- <span class="k2">0.5 · (1 + cos(π·r))</span> slides from 1 (r = 0) to 0 (r = 1).
- times the <span class="k3">gap</span> between the top and the floor, plus the <span class="k1">floor</span>.

Numbers, max 6e-4, min 6e-5, warmup 100, total 10,000. Step 5000: r = 4900 / 9900 ≈ 0.495, cos(π · 0.495) ≈ 0.016, 0.5 · 1.016 = 0.508. Gap = 5.4e-4. lr ≈ 6e-5 + 0.508 × 5.4e-4 ≈ **3.34e-4**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.log(vocab)` | | natural log |
| `if step >= total:` | "greater than or equal to" | after the end, stay at the floor |
| `math.cos(math.pi * r)` | | cos(π·r) |
| three `return`s | | the first matching case answers |

### 👀 Worked example: the three phases

- step 0 (warmup): 6e-4 × 1/100 = **6e-6**.
- step 99: 6e-4 × 100/100 = **6e-4**, the top.
- step 12,000 (≥ total): **6e-5**, the floor.

## 🎯 Your quest

`initial_loss(vocab)`: replace `return 0.0` with `    return math.log(vocab)`

`lr_at(step, max_lr, min_lr, warmup, total)`: replace `return max_lr` with:

1. `    if step < warmup:`
2. `        return max_lr * (step + 1) / warmup`
3. `    if step >= total:`
4. `        return min_lr`
5. `    r = (step - warmup) / (total - warmup)`
6. `    return min_lr + 0.5 * (1 + math.cos(math.pi * r)) * (max_lr - min_lr)`

## Review

<details><summary>How many parameters does one GPT-2 layer have, as a formula of d?</summary>12d² + 13d.</details>
<details><summary>Does the number of heads change the attention parameter count?</summary>No, heads only split the width d.</details>
