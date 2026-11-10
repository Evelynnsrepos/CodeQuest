---
title: Diffusion: generating images from noise
minutes: 50
xp: 60
hint: alpha_bars: out = [] and prod = 1.0, then for b in betas: prod = prod * (1 - b) and out.append(prod)
hint: add_noise: for i in range(len(x0)): out.append(math.sqrt(abar) * x0[i] + math.sqrt(1 - abar) * eps[i])
hint: predict_x0: out.append((xt[i] - math.sqrt(1 - abar) * eps_hat[i]) / math.sqrt(abar))
hint: guided: u = eps_uncond[i], then out.append(u + w * (eps_cond[i] - u))
---
# Learn to remove noise, then start from pure noise

⏱️ About 50 minutes

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

## 🔬 Take the formulas apart

**The signs:**

| Sign | Say it | Means |
|---|---|---|
| `β_t` | "beta t" | how much noise step t adds (a small number like 0.1) |
| `ᾱ_t` | "alpha bar t" | how much of the original image is left after t steps |
| `x_0` | "x zero" | the clean image (here: a short list of numbers) |
| `x_t` | "x t" | the image after t steps of noise |
| `ε` | "epsilon" | random noise, one random number per pixel |
| `ε ~ Normal(0, 1)` | "epsilon is drawn from a normal distribution" | the noise is random, mostly between −2 and 2, centred on 0 |
| `ε̂` | "epsilon hat" | the network's **guess** of the noise. A hat means "estimate". |
| `√` | "square root" | √0.64 = 0.8, because 0.8 × 0.8 = 0.64 |

**ᾱ in small steps**, betas (0.1, 0.2):

1. Step 1: 1 − 0.1 = 0.9. ᾱ₁ = **0.9**.
2. Step 2: 1 − 0.2 = 0.8. ᾱ₂ = 0.9 × 0.8 = **0.72**. Each step multiplies in one more factor: a **running product**.

**Adding noise** with x₀ = 1, ε = 0.5, ᾱ = 0.64:

1. √ᾱ = √0.64 = 0.8, and √(1 − ᾱ) = √0.36 = 0.6.
2. x_t = 0.8 × 1 + 0.6 × 0.5 = 0.8 + 0.3 = **1.1**.

**Getting it back** with the right noise guess ε̂ = 0.5:

1. x_t − √(1 − ᾱ) · ε̂ = 1.1 − 0.6 × 0.5 = 1.1 − 0.3 = 0.8.
2. Divide by √ᾱ = 0.8: 0.8 / 0.8 = **1**. That's x₀ again.

**Guidance** with ε_uncond = 0.1, ε_cond = 0.3, w = 7.5:

1. The difference the prompt makes: 0.3 − 0.1 = 0.2.
2. Exaggerate it: 7.5 × 0.2 = 1.5.
3. Add to the no-prompt guess: 0.1 + 1.5 = **1.6**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `prod = 1.0` then `prod = prod * (1 - b)` | | a **running product**: like a running total, but multiplying. It starts at 1, because times 1 changes nothing. |
| `math.sqrt(x)` | "square root of x" | √x |
| `for i in range(len(x0)):` | | once per pixel |
| `x0[i]`, `eps[i]` | | the same pixel in both lists |

## 🎯 Your quest

1. `alpha_bars(betas)`: the list of `ᾱ_t` for every step (running product of `1 − β`).
2. `add_noise(x0, eps, abar)`: the forward formula, element-wise ("element-wise" means: for each number in the list on its own).
3. `predict_x0(xt, eps_hat, abar)`: the estimate above.
4. `guided(eps_uncond, eps_cond, w)`: classifier-free guidance, element-wise.

**Part 1:** `alpha_bars`. Replace `return []` with:

1. `out = []`
2. `prod = 1.0`
3. `for b in betas:`
4. `    prod = prod * (1 - b)`
5. `    out.append(prod)`
6. `return out`

**Part 2:** `add_noise`. Replace `return x0` with:

1. `out = []`
2. `for i in range(len(x0)):`
3. `    out.append(math.sqrt(abar) * x0[i] + math.sqrt(1 - abar) * eps[i])`
4. `return out`

**Part 3:** `predict_x0`. Replace `return xt` with:

1. `out = []`
2. `for i in range(len(xt)):`
3. `    out.append((xt[i] - math.sqrt(1 - abar) * eps_hat[i]) / math.sqrt(abar))`
4. `return out`

**Part 4:** `guided`. Replace `return eps_cond` with:

1. `out = []`
2. `for i in range(len(eps_cond)):`
3. `    u = eps_uncond[i]`
4. `    out.append(u + w * (eps_cond[i] - u))`
5. `return out`

## Review

<details><summary>What does CLIP's contrastive loss push together and apart?</summary>Matching image and caption embeddings together, non-matching pairs apart.</details>
<details><summary>How many 16×16 patches does a 224×224 image have?</summary>196 (14 × 14).</details>
