---
title: Training on AMD, or on a rented GPU
minutes: 30
xp: 40
hint: training_hours: tokens = examples * avg_tokens * epochs, seconds = tokens / tokens_per_second, return seconds / 3600
hint: cloud_cost: return (hours + setup_hours) * price_per_hour
hint: diagnose: check None first: if hip_version is None: return "cpu-only build". Then if cuda_available: return "ready". Last line: the HSA text
---
# Where your training actually runs

⏱️ About 30 minutes

> **Warm-up:** almost every fine-tuning tutorial says `pip install ...` and assumes an NVIDIA GPU. What breaks on your Radeon?

Training libraries are **NVIDIA-first**: many speed tricks are written in CUDA, and AMD support arrives later or partially. The situation improves every few months, so treat everything here as "check the current docs":

**PyTorch on ROCm.** PyTorch publishes ROCm builds; pytorch.org's *Get Started* selector gives the current install line (of the form `pip install torch --index-url https://download.pytorch.org/whl/rocm6.x`). On ROCm, PyTorch reuses the CUDA names, so the test is the same:

```python
import torch
print(torch.cuda.is_available())   # True means your GPU is usable
print(torch.version.hip)           # a version string on ROCm builds, None on CUDA/CPU builds
```

If it says `False`, the usual suspects are the `HSA_OVERRIDE_GFX_VERSION` from LLMs 2, lesson 9, and your user missing the `video`/`render` groups.

**On NixOS** you have three routes: `python3Packages.torchWithRocm` from nixpkgs (in a dev shell; builds can be slow and lag behind), a Python virtualenv inside a `nix-shell` with ROCm libraries, or the low-friction one: a **container** (`podman`/`distrobox`) from AMD's official `rocm/pytorch` images.

**QLoRA pieces.** `bitsandbytes` (4-bit) has gained ROCm support in recent releases; Unsloth and Axolotl's AMD support has been changing. If 4-bit doesn't work on your card, plain LoRA on a **smaller** model in BF16 (e.g. 1–2B) fits in 12 GB and teaches you the same workflow.

**Renting a GPU** is the pragmatic option for first runs: services like RunPod, Vast.ai or Lambda rent NVIDIA GPUs by the hour (roughly €0.30–€2 per hour for 24–80 GB cards; prices change). Everything "just works" there, and a QLoRA run on a few hundred examples of a 1–4B model takes minutes to an hour. Remember: **stop the instance when you're done** (it bills while idle), and don't upload data you wouldn't want on someone else's computer.

How long will a run take? Count tokens:

```
training tokens = examples × average tokens per example × epochs
hours           = training tokens ÷ (tokens per second the setup trains at) ÷ 3600
```

Measure tokens/s with a short test run (the trainer logs it), then extrapolate.

## 🔬 Take the formulas apart

<div class="formula">tokens = <span class="k1">examples</span> × <span class="k2">avg tokens</span> × <span class="k3">epochs</span></div>
800 × 450 × 3 = **1,080,000** tokens to train on.

<div class="formula">hours = tokens ÷ <span class="k1">tokens per second</span> ÷ <span class="k2">3600</span></div>
1,080,000 ÷ 1,500 = 720 seconds. An hour has 60 × 60 = <span class="k2">3600</span> seconds: 720 ÷ 3600 = **0.2 hours** (12 minutes).

<div class="formula">cost = (<span class="k1">hours</span> + <span class="k2">setup</span>) × <span class="k3">price per hour</span></div>
(0.2 + 0.5) × 0.80 € = 0.7 × 0.80 = **0.56 €**. The setup half hour costs more than the training itself.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `(a + b) * c` | | brackets first |
| `def f(..., setup_hours=0.5):` | | 0.5 unless the caller gives another number |
| `if hip_version is None:` | | true when there is no ROCm version: a build without GPU support |
| `if cuda_available:` | | true when PyTorch sees the GPU. (On AMD, PyTorch still calls it "cuda".) |

### 👀 Worked example: the order of the checks

`diagnose(False, None)`: hip_version is None → "cpu-only build". The second `if` never runs.
`diagnose(False, "6.4.43482")`: not None, not available → falls through to the last line.
`diagnose(True, "6.4.43482")`: not None, available → "ready".

## 🎯 Your quest

`training_hours`: replace `return 0` with:

1. `    tokens = examples * avg_tokens * epochs`
2. `    seconds = tokens / tokens_per_second`
3. `    return seconds / 3600`

`cloud_cost`: replace `return 0` with `    return (hours + setup_hours) * price_per_hour`

`diagnose`: replace `return ""` with:

1. `    if hip_version is None:`
2. `        return "cpu-only build"`
3. `    if cuda_available:`
4. `        return "ready"`
5. `    return "check HSA_OVERRIDE_GFX_VERSION and groups"`

## Review

<details><summary>Name the four steps from adapter to LM Studio.</summary>Merge into a BF16 base, convert to GGUF (convert_hf_to_gguf.py), quantize (llama-quantize), import (lms import).</details>
<details><summary>Why merge into a BF16 base instead of the 4-bit one?</summary>Merging into the 4-bit base bakes quantization error in before you quantize again for GGUF.</details>
