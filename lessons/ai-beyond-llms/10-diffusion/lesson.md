---
title: Diffusion: generating images from noise
xp: 60
---
# Learn to remove noise, then start from pure noise

> **Warm-up:** if you had a model that could slightly clean up any noisy image, how could you use it to create a brand-new image?

Start from **pure random noise** and clean it up a little, many times. That's a **diffusion model** (DDPM, Ho et al. 2020).

**Forward process (fixed, no learning):** gradually add Gaussian noise over `T` steps with a schedule `β_1 … β_T`. With `ᾱ_t = (1 − β_1)(1 − β_2)…(1 − β_t)` you can jump straight to step `t`:

```
x_t = √ᾱ_t · x_0 + √(1 − ᾱ_t) · ε        ε ~ Normal(0, 1)
```

**Training:** pick an image `x_0`, a random step `t` and noise `ε`, make `x_t`, and train a network (a U-Net CNN or a transformer) to **predict ε** from `x_t` and `t`. The loss is just MSE between the true and predicted noise.

**Generating:** start at `x_T` = noise and step backwards, each step removing a bit of the predicted noise. From a noise prediction `ε̂` you can estimate the clean image at any step:

```
x̂_0 = (x_t − √(1 − ᾱ_t) · ε̂) / √ᾱ_t
```

**Text-to-image** adds conditioning: the network also sees a text embedding (from CLIP or T5). **Classifier-free guidance** runs it with and without the prompt and exaggerates the difference, `ε = ε_uncond + w·(ε_cond − ε_uncond)` with `w` around 3–8; higher `w` follows the prompt more closely but looks less natural.

**Latent diffusion** (Stable Diffusion, 2022) diffuses in a small compressed "latent" space from an autoencoder instead of raw pixels, which is what makes it run on a 12 GB GPU.

**Changing fast:** many current models (Stable Diffusion 3, Flux) use **flow matching** with transformer backbones (DiT) instead of the classic DDPM recipe; the noise-to-image idea is the same. **On your machine:** ComfyUI runs these models locally. On AMD under Linux it uses the ROCm build of PyTorch; check its install guide for your card, since support changes between versions.

## Your quest

1. `alpha_bars(betas)`: the list of `ᾱ_t` for every step (running product of `1 − β`).
2. `add_noise(x0, eps, abar)`: the forward formula, element-wise.
3. `predict_x0(xt, eps_hat, abar)`: the estimate above.
4. `guided(eps_uncond, eps_cond, w)`: classifier-free guidance, element-wise.

## Review

<details><summary>What does CLIP's contrastive loss push together and apart?</summary>Matching image and caption embeddings together, non-matching pairs apart.</details>
<details><summary>How many 16×16 patches does a 224×224 image have?</summary>196 (14 × 14).</details>
