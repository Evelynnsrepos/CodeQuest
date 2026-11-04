---
title: Big and tiny numbers: scientific notation
xp: 30
---
# Writing 8,000,000,000 without counting zeros

> **Warm-up:** "Llama 3 8B was trained on 15T tokens with a learning rate of 3e-4." What could `8B`, `15T` and `3e-4` mean?

**In one sentence:** scientific notation writes a number as "a few digits times 10 to some power", so you can see its size at a glance.

## 🪜 Plain words

Counting zeros in 15,000,000,000,000 is slow and easy to get wrong. Instead, say "15, then move the decimal point 12 places to the right". For tiny numbers, move it to the **left** instead.

Everyday shortcuts do the same: K = thousand, M = million, B = billion, T = trillion.

## 🪜 With numbers

- 8 B = 8 billion = 8,000,000,000 (9 zeros).
- 3e-4: start with 3 and move the point 4 places left: 0.0003.
- An 8 billion parameter model with 2 bytes each: 8 billion times 2 = 16 billion bytes = **16 GB**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `10⁴` | "ten to the four" | 10,000 (1 with 4 zeros) | `1e4` |
| `3 · 10⁴` | "three times ten to the four" | 30,000 | `3e4` |
| `3 · 10⁻⁴` | "three times ten to the minus four" | 0.0003 | `3e-4` |
| `3e-4` | "three e minus four" | the computer way of writing it | `3e-4` |
| K, M, B, T | thousand, million, billion, trillion | 10³, 10⁶, 10⁹, 10¹² | `1e3` … `1e12` |
| `~` | "about" | roughly | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">3</span> <span class="k2">·</span> <span class="k3">10</span><sup><span class="k4">−4</span></sup></div>

| Piece | Say it | Means | |
|---|---|---|---|
| <span class="k1">3</span> | "three" | the digits that matter | 3 |
| <span class="k2">·</span> | "times" | multiply | |
| <span class="k3">10</span> | "ten" | always 10 in this notation | |
| <sup><span class="k4">−4</span></sup> | "to the minus four" | move the point 4 places; **minus = left (smaller)**, plus = right (bigger) | 0.0003 |

Model size in GB:

<div class="formula"><span class="k1">GB</span> = <span class="k2">params</span> · <span class="k3">bytes</span> <span class="k4">/ 10⁹</span></div>

| Piece | Say it | Means | 8B model in FP16 |
|---|---|---|---|
| <span class="k2">params</span> | "params" | number of weights | 8 · 10⁹ |
| <span class="k3">bytes</span> | "bytes" | bytes per weight | 2 |
| <span class="k4">/ 10⁹</span> | "divided by ten to the nine" | bytes → GB | 16 · 10⁹ / 10⁹ = 16 |

## 🔀 What if the formula were different?

<div class="wrong"><b>3e4</b> instead of <b>3e-4</b> (lost the minus): a learning rate of 30,000 instead of 0.0003. Training explodes on the first step.</div>
<div class="wrong"><b>params · bytes / 10⁶</b>: 16,000 "GB". You divided by a million (that gives MB).</div>
<div class="right"><b>8e9 · 2 / 1e9</b> = 16 GB ✓</div>

Note: GB = 10⁹ bytes, but GiB = 2³⁰ ≈ 1.074 · 10⁹. Tools mix them up; the difference is about 7%.

## 🗣️ Say it out loud

`3 · 10⁻⁴` → "three times ten to the minus four" → "zero point zero zero zero three".

## 🤖 Where AI uses it

Parameter counts, token counts, FLOPs, learning rates (`1e-5` to `1e-3`), tiny safety numbers like `1e-8`.

## 🎯 Your quest

1. `human(n)`: write a number with a suffix and one decimal: `"8.0B"`, `"15.0T"`, `"124.4M"`, `"3.5K"`; below 1000 just `str(n)`. T for ≥ 10¹², B for ≥ 10⁹, M for ≥ 10⁶, K for ≥ 10³.
2. `model_gb(params, bytes_per_param)`: size in GB (10⁹ bytes).

**Remember:** in `3e-4`, the `e` means "times ten to the".

## Review

<details><summary>What is 2⁻¹?</summary>½ = 0.5.</details>
<details><summary>How many values fit in 8 bits?</summary>2⁸ = 256.</details>
