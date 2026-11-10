---
title: Fine-tuning hyperparameters
minutes: 40
xp: 40
hint: effective_batch: return per_device * accumulation * gpus
hint: total_steps: batch = effective_batch(per_device, accumulation, gpus), then return math.ceil(examples / batch) * epochs
hint: warnings_for: eb = effective_batch(...) and steps = total_steps(...) from the config's values first
hint: Then five separate ifs (not elif), each with warnings.append("..."), in the order of the list
---
# Settings that make or break a run

⏱️ About 40 minutes

> **Warm-up:** LLMs 5 showed what a bad learning rate does. For LoRA on 500 examples, would you guess a larger or smaller learning rate than for pretraining? More or fewer epochs?

Starting points that work for most (Q)LoRA SFT runs (they are starting points, not laws; model cards and the Unsloth/TRL docs often suggest values too):

| Setting | Typical | Why |
|---|---|---|
| learning rate | `1e-4` – `2e-4` (LoRA) | LoRA update starts at zero (B is all zeros, A is random, so B·A = 0) and is tiny, so they tolerate higher rates than full fine-tuning (`~1e-5`) |
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

## 🔬 Take the formulas apart

<div class="formula">effective batch = <span class="k1">per-device</span> × <span class="k2">accumulation</span> × <span class="k3">GPUs</span></div>
- <span class="k1">per-device</span>: examples the GPU processes at once (small, so it fits in memory).
- <span class="k2">accumulation</span>: how many of those small batches are added up before **one** update.
- <span class="k3">GPUs</span>: you have 1.

2 × 8 × 1 = **16** examples per optimizer step.

<div class="formula">steps = <span class="k1">⌈examples ÷ effective batch⌉</span> × <span class="k2">epochs</span></div>
⌈ ⌉ means round **up** (LLMs 5, lesson 7). 600 ÷ 16 = 37.5 → 38 steps per epoch, × 3 epochs = **114**.

**Small numbers.** `5e-4` = 5 × 10⁻⁴ = 0.0005. The minus in the power means "divide": 10⁻⁴ = 1 / 10,000. `1e-5` = 0.00001.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `def f(a, b, gpus=1):` | | `gpus` is 1 unless the caller says otherwise |
| `math.ceil(x)` | | round up |
| `config["lr"]` | | read a value from the dictionary |
| `if config["lr"] > 5e-4:` | | compare with 0.0005 |
| five `if`s in a row | | each one is checked. Several warnings can be added. (`elif` would stop at the first.) |
| `warnings.append("...")` | | add one text to the list |

### 👀 Worked example: the risky config

`{"lr": 1e-3, "epochs": 10, "examples": 40, "per_device": 1, "accumulation": 2}`:

1. effective batch 1 × 2 = 2. Steps = ⌈40 ÷ 2⌉ × 10 = 20 × 10 = 200.
2. lr 0.001 > 0.0005 → "learning rate too high".
3. lr < 0.00001? No.
4. epochs 10 > 5 → "too many epochs".
5. effective batch 2 < 8 → "effective batch too small".
6. steps 200 < 20? No.

## 🎯 Your quest

`effective_batch`: replace `return 0` with `    return per_device * accumulation * gpus`

`total_steps`: replace `return 0` with:

1. `    batch = effective_batch(per_device, accumulation, gpus)`
2. `    return math.ceil(examples / batch) * epochs`

`warnings_for(config)`: between `warnings = []` and `return warnings`, add:

1. `    eb = effective_batch(config["per_device"], config["accumulation"])`
2. `    steps = total_steps(config["examples"], config["per_device"], config["accumulation"], config["epochs"])`
3. `    if config["lr"] > 5e-4:`
4. `        warnings.append("learning rate too high")`
5. `    if config["lr"] < 1e-5:`
6. `        warnings.append("learning rate too low")`
7. `    if config["epochs"] > 5:`
8. `        warnings.append("too many epochs")`
9. `    if eb < 8:`
10. `        warnings.append("effective batch too small")`
11. `    if steps < 20:`
12. `        warnings.append("very few steps")`

## Review

<details><summary>What does NF4 do differently from plain 4-bit quantization?</summary>Its 16 levels sit at the quantiles of a normal distribution, matching how trained weights are distributed.</details>
<details><summary>Roughly what share of an 8B model does r=16 LoRA on all seven modules train?</summary>About 0.5% (42M parameters).</details>
