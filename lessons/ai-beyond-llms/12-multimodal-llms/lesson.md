---
title: Multimodal LLMs: how a chat model sees
minutes: 30
xp: 50
hint: image_tokens: patches = (width // patch) * (height // patch), then return patches // (merge * merge)
hint: splice: out = [] and k = 0. For each t in tokens: if t == marker: copy every piece of images[k] into out, then k = k + 1
hint: splice: else: out.append(t). At the end: return out
---
# Gluing eyes onto a language model

⏱️ About 30 minutes

> **Warm-up:** you drop a screenshot into a vision model in LM Studio. The LLM inside only understands token embeddings. What has to happen to the picture first?

It has to become **token embeddings** too. The common recipe (LLaVA, 2023; used in most open vision-language models):

1. A **vision encoder**, usually a CLIP-style ViT (lesson 9), turns the image into one vector per patch.
2. A small **projector** (a linear layer or 2-layer MLP) maps each patch vector into the LLM's embedding space.
3. Those vectors are **spliced into the prompt** where the `<image>` placeholder was, and the LLM reads them like any other tokens.
4. Training: first only the projector (on image–caption pairs), then projector + LLM on visual instruction data.

**Image tokens cost context.** A ViT with 14-pixel patches on a 336×336 image gives 24 × 24 = 576 tokens. Some models (Qwen2-VL and later) merge each 2×2 group of neighbouring patches into one token, cutting that by 4, and accept different image sizes, so a big screenshot can still be thousands of tokens. That's KV cache and VRAM (LLMs 2).

**On your machine:** in GGUF, the vision part ships as a separate **`mmproj`** file next to the main model; LM Studio downloads both for vision models (look for the eye icon). Which vision models are available and how well they run changes quickly; check the model page.

Beyond images: "omni" models take audio the same way (an audio encoder, like Whisper's, plus a projector), and some models *generate* images by predicting image tokens autoregressively instead of using diffusion.

## 🔬 The token count, step by step

`(width // patch) · (height // patch) / merge²` for a 224 × 224 image, patch 16:

1. `//` divides and drops the rest: 224 // 16 = **14** patches across, and 14 down.
2. 14 · 14 = **196** patches (the `·` means "times").
3. `merge²` ("merge squared") is merge × merge. With merge = 1 nothing changes: 196 tokens.
4. With merge = 2, every 2 × 2 block of patches becomes one token: 196 / 4 = **49** tokens.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `width // patch` | "width floor-divided by patch" | whole patches only |
| `merge * merge` | | merge squared |
| `k = 0` ... `k = k + 1` | | counts which image comes next |
| `images[k]` | | the k-th image: a list of image tokens |
| `for piece in images[k]: out.append(piece)` | | copies every token of that image into `out`, one by one |
| `if t == marker:` ... `else:` | | the marker is swapped for the image, everything else is copied as it is |

### 👀 Worked example: splice

`splice(["hi", "<img>", "!"], [["p1", "p2"]], "<img>")`:

1. `"hi"`: not the marker → `out` = `["hi"]`.
2. `"<img>"`: the marker → copy `images[0]`, which is `["p1", "p2"]` → `out` = `["hi", "p1", "p2"]`. Now `k` = 1, ready for a second image.
3. `"!"`: copied → `["hi", "p1", "p2", "!"]`.

The input list is never changed, because you build a new list `out`.

## 🎯 Your quest

1. `image_tokens(width, height, patch, merge)`: `(width // patch) · (height // patch)` patches, divided by `merge²`.
2. `splice(tokens, images, marker)`: return a new list where the k-th `marker` in `tokens` is replaced by all items of `images[k]`.

**Part 1:** `image_tokens`. Replace `return 0` with:

1. `patches = (width // patch) * (height // patch)`
2. `return patches // (merge * merge)`

**Part 2:** `splice`. Replace `return tokens` with:

1. `out = []`
2. `k = 0`
3. `for t in tokens:`
4. `    if t == marker:`
5. `        for piece in images[k]:`
6. `            out.append(piece)`
7. `        k = k + 1`
8. `    else:`
9. `        out.append(t)`
10. `return out`

## Review

<details><summary>Which frequency does DFT bin k stand for?</summary>k · sample_rate / N.</details>
<details><summary>What does Whisper's encoder read?</summary>A log-mel spectrogram of a 30-second audio chunk.</details>
