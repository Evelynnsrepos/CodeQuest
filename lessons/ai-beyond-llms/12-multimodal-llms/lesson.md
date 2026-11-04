---
title: Multimodal LLMs: how a chat model sees
xp: 50
---
# Gluing eyes onto a language model

> **Warm-up:** you drop a screenshot into a vision model in LM Studio. The LLM inside only understands token embeddings. What has to happen to the picture first?

It has to become **token embeddings** too. The common recipe (LLaVA, 2023; used in most open vision-language models):

1. A **vision encoder**, usually a CLIP-style ViT (lesson 9), turns the image into one vector per patch.
2. A small **projector** (a linear layer or 2-layer MLP) maps each patch vector into the LLM's embedding space.
3. Those vectors are **spliced into the prompt** where the `<image>` placeholder was, and the LLM reads them like any other tokens.
4. Training: first only the projector (on image–caption pairs), then projector + LLM on visual instruction data.

**Image tokens cost context.** A ViT with 14-pixel patches on a 336×336 image gives 24 × 24 = 576 tokens. Some models (Qwen2-VL and later) merge each 2×2 group of neighbouring patches into one token, cutting that by 4, and accept different image sizes, so a big screenshot can still be thousands of tokens. That's KV cache and VRAM (LLMs 2).

**On your machine:** in GGUF, the vision part ships as a separate **`mmproj`** file next to the main model; LM Studio downloads both for vision models (look for the eye icon). Which vision models are available and how well they run changes quickly; check the model page.

Beyond images: "omni" models take audio the same way (an audio encoder, like Whisper's, plus a projector), and some models *generate* images by predicting image tokens autoregressively instead of using diffusion.

## Your quest

1. `image_tokens(width, height, patch, merge)`: `(width // patch) · (height // patch)` patches, divided by `merge²`.
2. `splice(tokens, images, marker)`: return a new list where the k-th `marker` in `tokens` is replaced by all items of `images[k]`.

## Review

<details><summary>Which frequency does DFT bin k stand for?</summary>k · sample_rate / N.</details>
<details><summary>What does Whisper's encoder read?</summary>A log-mel spectrogram of a 30-second audio chunk.</details>
