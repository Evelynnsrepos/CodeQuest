---
title: Speech: spectrograms and Whisper
xp: 60
---
# Turning sound into something a transformer can read

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

## Your quest

1. `frames(signal, size, hop)`: all full frames, starting at 0, `hop`, `2·hop`, … (drop a last partial one).
2. `dft_magnitudes(frame)`: `|X_k|` for `k = 0 … N // 2`.
3. `hz_to_mel(f)`.

## Review

<details><summary>What does a diffusion model learn to predict during training?</summary>The noise that was added to the image (ε).</details>
<details><summary>What does classifier-free guidance do?</summary>Pushes the prediction further in the direction of the prompt: ε_uncond + w·(ε_cond − ε_uncond).</details>
