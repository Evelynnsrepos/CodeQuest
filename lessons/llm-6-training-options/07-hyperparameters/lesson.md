---
title: Fine-tuning hyperparameters
xp: 40
---
# Settings that make or break a run

> **Warm-up:** LLMs 5 showed what a bad learning rate does. For LoRA on 500 examples, would you guess a larger or smaller learning rate than for pretraining? More or fewer epochs?

Starting points that work for most (Q)LoRA SFT runs (they are starting points, not laws; model cards and the Unsloth/TRL docs often suggest values too):

| Setting | Typical | Why |
|---|---|---|
| learning rate | `1e-4` – `2e-4` (LoRA) | LoRA matrices start at zero and are tiny, so they tolerate higher rates than full fine-tuning (`~1e-5`) |
| scheduler | linear or cosine, ~3–10% warmup | LLMs 5, lesson 9 |
| epochs | 1–3 | more mostly memorizes small datasets |
| rank `r` | 8–64 | higher = more capacity, more memory; start at 16 |
| `lora_alpha` | `r` or `2r` | |
| `lora_dropout` | 0–0.1 | a little regularization |
| per-device batch size | 1–4 on 12 GB | memory-bound |
| gradient accumulation | 4–16 | gets the **effective batch** to 16–64 |
| `max_seq_length` | the longest real example | longer costs memory; shorter cuts answers |
| weight decay | 0–0.01 | |

The **effective batch size** is what the optimizer sees per step:

```
effective batch = per-device batch × gradient accumulation steps × number of GPUs
optimizer steps = ⌈examples ÷ effective batch⌉ × epochs
```

With 500 examples, effective batch 16 and 3 epochs, that's only 96 optimizer steps. Small datasets mean few steps, so each one matters. Watch the training and validation loss (logged every few steps) and stop when validation stops improving. A training loss that drops to near 0 almost always means memorizing.

## Your quest

1. `effective_batch(per_device, accumulation, gpus=1)`.
2. `total_steps(examples, per_device, accumulation, epochs, gpus=1)`.
3. `warnings_for(config)`: return a list of warning strings for a LoRA config dictionary. Add each warning whose condition holds, in this order:
   - `"learning rate too high"` if `lr > 5e-4`
   - `"learning rate too low"` if `lr < 1e-5`
   - `"too many epochs"` if `epochs > 5`
   - `"effective batch too small"` if the effective batch is below 8
   - `"very few steps"` if the total steps are below 20

## Review

<details><summary>What does NF4 do differently from plain 4-bit quantization?</summary>Its 16 levels sit at the quantiles of a normal distribution, matching how trained weights are distributed.</details>
<details><summary>Roughly what share of an 8B model does r=16 LoRA on all seven modules train?</summary>About 0.5% (42M parameters).</details>
