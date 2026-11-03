---
title: The GPT training recipe
xp: 50
---
# How a GPT is actually trained

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

## Your quest

1. `initial_loss(vocab)`: the expected loss of a uniform guess.
2. `lr_at(step, max_lr, min_lr, warmup, total)`: the schedule above.

## Review

<details><summary>How many parameters does one GPT-2 layer have, as a formula of d?</summary>12d² + 13d.</details>
<details><summary>Does the number of heads change the attention parameter count?</summary>No, heads only split the width d.</details>
