---
title: Speech: spectrograms and Whisper
minutes: 60
xp: 60
hint: frames: for start in range(0, len(signal) - size + 1, hop): and inside it out.append(signal[start:start + size])
hint: dft_magnitudes: for k in range(N // 2 + 1): start re = 0 and im = 0, then for n in range(N): angle = 2 * math.pi * k * n / N
hint: Inside the n loop: re = re + frame[n] * math.cos(angle) and im = im - frame[n] * math.sin(angle)
hint: After the n loop (8 spaces): mags.append(math.sqrt(re * re + im * im))
hint: hz_to_mel: return 2595 * math.log10(1 + f / 700)
---
# Turning sound into something a transformer can read

⏱️ About 60 minutes

> **Warm-up:** audio is just a long list of numbers (air pressure, 16,000 per second). Why is it hard to recognize words directly from that list?

The same sound can look completely different sample by sample. What stays similar is **which frequencies** are present over time. So speech models first compute a **spectrogram**:

1. Cut the signal into short overlapping **frames** (Whisper: 25 ms windows = 400 samples at 16 kHz, moved by a **hop** of 10 ms = 160 samples).
2. For each frame, measure the strength of each frequency with the **Discrete Fourier Transform**:

```
X_k = Σ_n x_n · e^(−2πi·k·n/N)      magnitude |X_k| = √(re² + im²)
re = Σ x_n·cos(2πkn/N),  im = −Σ x_n·sin(2πkn/N),   k = 0 … N/2
```

Bin `k` corresponds to frequency `k · sample_rate / N`. (Real code uses the fast FFT and a window function.)

3. Group frequencies into **mel** bands, which mimic human hearing (we tell 100 Hz from 200 Hz easily, 10,100 from 10,200 Hz not): `mel = 2595 · log10(1 + f / 700)`. Then take the log.

The result, a **log-mel spectrogram**, is an image-like grid (time × 80 or 128 mel bands). **Whisper** (OpenAI, 2022, open weights) feeds 30-second chunks of it into a transformer **encoder**, and a **decoder** writes the transcript token by token, like an LLM conditioned on audio. It was trained on 680,000 hours of web audio, and it can also translate and detect language.

The reverse direction, **text-to-speech** (TTS), uses transformers or diffusion to generate audio tokens or spectrograms that a **vocoder** turns back into sound.

**On your machine:** `whisper.cpp` runs Whisper locally (it has a Vulkan backend for AMD), with quantized models like llama.cpp. LM Studio itself focuses on text and vision models.

## 🔬 Take the formulas apart

The DFT formula at the top uses complex numbers (that's the `i`). You don't need them: the second line, with `re` and `im`, says the same thing with ordinary numbers. That's the one you'll code.

**The signs:**

| Sign | Say it | Means |
|---|---|---|
| `x_n` | "x n" | sample number n of the frame |
| `N` | "N" | how many samples the frame has |
| `k` | "k" | which frequency you're testing: k = 1 means "a wave that goes up and down once in the frame", k = 2 twice, ... |
| `π` | "pi" | 3.14159..., in Python `math.pi`. 2π is one full circle. |
| `cos`, `sin` | "cosine", "sine" | the two basic waves. cos(0) = 1, cos(π/2) = 0, cos(π) = −1, cos(3π/2) = 0; sin is the same wave shifted: 0, 1, 0, −1 |
| `Σ_n` | "sum over n" | add up for every sample |
| `√(re² + im²)` | "the square root of re squared plus im squared" | the **magnitude**: how strong that frequency is |

**What `re` does:** it multiplies the frame by a test wave and adds up. If the frame looks like the wave, the products are mostly positive and the sum is big. If not, plus and minus cancel out to about 0. `im` does the same with the shifted wave, so a frequency is found even when it doesn't start at the top.

**By hand**, frame (1, 0, −1, 0), so N = 4 and k goes from 0 to N // 2 = 2:

1. **k = 0:** the angle is always 0, cos(0) = 1 and sin(0) = 0. re = 1 + 0 − 1 + 0 = **0**, im = 0. Magnitude **0**.
2. **k = 1:** the angles are 2π·1·n/4 for n = 0, 1, 2, 3: 0, π/2, π, 3π/2.
   - cos of those: 1, 0, −1, 0. re = 1·1 + 0·0 + (−1)·(−1) + 0·0 = **2**.
   - sin of those: 0, 1, 0, −1. Σ x·sin = 1·0 + 0·1 + (−1)·0 + 0·(−1) = 0, so im = **0**.
   - magnitude √(2² + 0²) = **2**.
3. **k = 2:** angles 0, π, 2π, 3π. cos: 1, −1, 1, −1. re = 1·1 + 0 + (−1)·1 + 0 = **0**. Magnitude **0**.
4. Result `[0, 2, 0]`: all the energy is in bin 1. The frame is one up-and-down wave, and the DFT found it.

**Mel**, `2595 · log10(1 + f / 700)`, for f = 1000 Hz:

1. `log10(x)` asks "10 to the power of what gives x?": log10(10) = 1, log10(100) = 2, log10(1) = 0.
2. f / 700 = 1000 / 700 = 1.4286. Plus 1: **2.4286**.
3. log10(2.4286) = **0.3853** (10^0.3853 is 2.4286).
4. 2595 × 0.3853 = **1000**. The scale is made so 1000 Hz is 1000 mel. Higher up, the mel numbers grow more slowly than Hz, just like your hearing.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `range(0, len(signal) - size + 1, hop)` | | every start position, jumping by `hop`. The end makes sure a full frame still fits. |
| `signal[start:start + size]` | | a **slice**: `size` samples beginning at `start` |
| `N // 2 + 1` | | half the frame size, plus 1 (the bins 0 to N/2) |
| `math.pi`, `math.cos(x)`, `math.sin(x)` | | π and the two waves |
| `im = im - ...` | | the formula has a minus in front of the sum, so subtract each piece |
| `math.sqrt(x)`, `math.log10(x)` | | square root, and the "power of 10" question |

### 👀 Worked example: frames

`frames([0, 1, 2, 3, 4, 5, 6], 3, 2)`:

1. `len(signal) - size + 1` = 7 − 3 + 1 = 5, so `range(0, 5, 2)` gives the starts 0, 2, 4.
2. Start 0: `[0, 1, 2]`. Start 2: `[2, 3, 4]`. Start 4: `[4, 5, 6]`.
3. A start at 6 would need samples 6, 7, 8, but there are only 7 samples. The range stops before it, so there's no partial frame.

## 🎯 Your quest

1. `frames(signal, size, hop)`: all full frames, starting at 0, `hop`, `2·hop`, … (drop a last partial one).
2. `dft_magnitudes(frame)`: `|X_k|` for `k = 0 … N // 2`.
3. `hz_to_mel(f)`.

**Part 1:** `frames`. Replace `return []` with:

1. `out = []`
2. `for start in range(0, len(signal) - size + 1, hop):`
3. `    out.append(signal[start:start + size])`
4. `return out`

**Part 2:** `dft_magnitudes`. Replace `return []` with:

1. `N = len(frame)`
2. `mags = []`
3. `for k in range(N // 2 + 1):`
4. `    re = 0`
5. `    im = 0`
6. `    for n in range(N):`
7. `        angle = 2 * math.pi * k * n / N`
8. `        re = re + frame[n] * math.cos(angle)`
9. `        im = im - frame[n] * math.sin(angle)`
10. `    mags.append(math.sqrt(re * re + im * im))`
11. `return mags`

**Part 3:** `hz_to_mel`. Replace `return f` with:

1. `return 2595 * math.log10(1 + f / 700)`

## Review

<details><summary>What does a diffusion model learn to predict during training?</summary>The noise that was added to the image (ε).</details>
<details><summary>What does classifier-free guidance do?</summary>Pushes the prediction further in the direction of the prompt: ε_uncond + w·(ε_cond − ε_uncond).</details>
