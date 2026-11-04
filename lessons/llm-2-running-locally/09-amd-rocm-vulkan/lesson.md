---
title: AMD on Linux, ROCm vs Vulkan
xp: 30
---
# Getting your Radeon to do the work

> **Warm-up:** LM Studio on your machine can use a "Vulkan" or a "ROCm" runtime. Which one are you using right now, and do you know why?

llama.cpp talks to the GPU through a **backend**. On AMD there are two:

| | **Vulkan** | **ROCm (HIP)** |
|---|---|---|
| What it is | The cross-vendor graphics/compute API your games use | AMD's CUDA equivalent, the stack PyTorch uses on AMD |
| Driver | Mesa's RADV, already there on NixOS with `hardware.graphics.enable = true;` | The ROCm userspace libraries (big) |
| Card support | Practically every AMD GPU of the last decade | An official list, mostly recent high-end cards; others work with an override |
| Speed in llama.cpp | Often equal or better for generation | Often better for prompt processing |
| Training (Module 6) | No | Yes, PyTorch needs ROCm |

For **running** GGUF models, Vulkan is the low-hassle default; it's worth benchmarking both on your card (LM Studio: *Settings → Runtime* lists the installed runtimes; the exact menu moves between versions). For **training**, you'll need ROCm, so it's worth getting it working.

**Your card's target name.** ROCm identifies GPUs by a `gfx` code, for example `gfx1031` (RX 6700 XT / 6750 XT, 12 GB) or `gfx1101` (RX 7700 XT / 7800 XT). Find yours with:

```bash
nix shell nixpkgs#rocmPackages.rocminfo -c rocminfo | grep -m1 -o 'gfx[0-9a-f]*'
```

ROCm ships compiled code for the officially supported targets only. Cards in the same family usually run that code fine, so you tell ROCm to pretend your card is the supported sibling:

```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0   # RDNA2 (gfx103x) cards → act as gfx1030
export HSA_OVERRIDE_GFX_VERSION=11.0.0   # RDNA3 (gfx110x) cards → act as gfx1100
```

The supported list changes with every ROCm release, so check AMD's "ROCm compatibility matrix" for your version before assuming you need an override.

**On NixOS** the relevant switches are `nixpkgs.config.rocmSupport = true;` (packages like PyTorch and llama-cpp get built with ROCm) and per-package overrides such as `llama-cpp.override { vulkanSupport = true; }` or `{ rocmSupport = true; }`. With `services.ollama`, the `acceleration = "rocm";` and `rocmOverrideGfx = "10.3.0";` options do the same. Option names in nixpkgs change over time; `nixos-option` or search.nixos.org show the current ones.

## Your quest

Write `hsa_override(gfx)`:

- `gfx103` followed by anything (RDNA2) → `"10.3.0"`
- `gfx110` followed by anything (RDNA3) → `"11.0.0"`
- anything else → `None` (no known override; check the docs)

`text.startswith("gfx103")` checks the beginning of a string.

## Review

<details><summary>What is the default port of LM Studio's server? Of Ollama's?</summary>1234 and 11434.</details>
<details><summary>Why can other apps use "your local model" no matter which runner you use?</summary>All the runners offer the same OpenAI-compatible HTTP API.</details>
