---
title: Training on AMD, or on a rented GPU
xp: 40
---
# Where your training actually runs

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

## Your quest

1. `training_hours(examples, avg_tokens, epochs, tokens_per_second)`.
2. `cloud_cost(hours, price_per_hour, setup_hours=0.5)`: you also pay while setting up and downloading.
3. `diagnose(cuda_available, hip_version)`: return `"ready"` if `cuda_available` is true and `hip_version` is not `None`; `"cpu-only build"` if `hip_version` is `None`; otherwise `"check HSA_OVERRIDE_GFX_VERSION and groups"`.

## Review

<details><summary>Name the four steps from adapter to LM Studio.</summary>Merge into a BF16 base, convert to GGUF (convert_hf_to_gguf.py), quantize (llama-quantize), import (lms import).</details>
<details><summary>Why merge into a BF16 base instead of the 4-bit one?</summary>Merging into the 4-bit base bakes quantization error in before you quantize again for GGUF.</details>
