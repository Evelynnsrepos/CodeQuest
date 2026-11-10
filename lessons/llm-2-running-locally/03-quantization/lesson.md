---
title: Quantization, by hand
minutes: 45
xp: 35
hint: Find the biggest size: biggest = 0, then for w in block: if abs(w) > biggest: biggest = abs(w)
hint: Then: if biggest > 0: scale = biggest / 7 (the starter already has scale = 1.0 for the all-zero case)
hint: Then: for w in block: q = round(w / scale), then q = max(-8, min(7, q)), then qs.append(q)
hint: dequantize: restored = [], for q in qs: restored.append(q * scale), return restored
hint: Look at the outlier block's quantized list: did the small weights all turn into 0? Then outlier_hurts = True
---
# Shrinking weights to 4 bits

⏱️ About 45 minutes

> **Warm-up:** a weight like `0.0371` is stored in 16 bits. If you only had 4 bits (16 possible values), how would you store it?

**Quantization** stores each weight with fewer bits. 4 bits allow only 16 different whole numbers, −8 to 7. The trick is to give every small **block** of weights (32 in llama.cpp) its own **scale**:

```
block:   [0.12, -0.40, 0.05, 0.33]          (real blocks have 32 weights)
scale  = max(|w|) / 7 = 0.40 / 7 = 0.0571
q      = round(w / scale), clamped to −8…7
       = [2, -7, 1, 6]                       ← stored with 4 bits each
dequantized = q × scale
       = [0.114, -0.400, 0.057, 0.343]      ← what the model computes with
```

The block stores 32 small integers plus one 16-bit scale, so each weight costs 4 + 16/32 = **4.5 bits**. That's llama.cpp's `Q4_0`. Every weight now has a small **rounding error**, and quality drops a little. Quantization works because LLMs are surprisingly tolerant of this noise, down to about 4 bits. Below that, quality falls off quickly, and small models suffer more than big ones.

Why blocks? One scale for the whole tensor would be ruined by a single large weight (an **outlier**): every other weight would round to 0. Small blocks keep the damage local.

## 🔬 Take the steps apart

**`|w|`** (say "the absolute value of w") is the size of a number **without its sign**: |−0.40| = 0.40, |0.33| = 0.33. It answers "how far from 0?".

**`max(|w|)`** is the biggest of those sizes in the block. For [0.12, −0.40, 0.05, 0.33] that's **0.40** (from −0.40).

**The scale** `= max(|w|) ÷ 7`. 7 is the biggest number 4 bits can store on the positive side. Dividing by 7 means: "the biggest weight in this block will become 7 (or −7)". 0.40 ÷ 7 = **0.0571**.

**`q = round(w ÷ scale)`**: how many "scale steps" is this weight? Then round to a whole number.

| w | w ÷ 0.0571 | round | |
|---|---|---|---|
| 0.12 | 2.1 | **2** | |
| −0.40 | −7.0 | **−7** | the biggest becomes −7 |
| 0.05 | 0.88 | **1** | |
| 0.33 | 5.78 | **6** | |

**Clamped to −8…7** means: if a number is below −8 make it −8, if above 7 make it 7. With our scale it never happens, but it's a safety net.

**Dequantize** `= q × scale`: 2 × 0.0571 = 0.114 (was 0.12). The difference, 0.006, is the **rounding error**.

## 🔀 What if it were different?

<div class="wrong"><b>One scale for a block with an outlier</b>: block [0.12, −0.40, 0.05, 6.50]. Scale = 6.50 ÷ 7 = 0.93. Now 0.12 ÷ 0.93 = 0.13 rounds to <b>0</b>, and 0.05 → 0 too. The small weights are wiped out.</div>
<div class="right">Small blocks: the outlier only hurts its own 32 neighbours ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `abs(-0.4)` | "absolute value of minus 0.4" | `0.4` |
| `round(2.1)` | "round 2.1" | `2`, the nearest whole number |
| `min(7, q)` | "the smaller of 7 and q" | stops `q` from going above 7 |
| `max(-8, …)` | "the bigger of −8 and …" | stops it from going below −8 |
| `max(-8, min(7, q))` | | both at once: the **clamp** |
| `return scale, qs` | | gives back two things as a pair |

### 👀 Worked example: the biggest-so-far loop, by size

```python
temps = [3, -9, 5]
biggest = 0
for t in temps:
    if abs(t) > biggest:
        biggest = abs(t)
print(biggest)   # 9
```

3 → biggest 3. −9: |−9| = 9 > 3 → biggest 9. 5: 5 > 9? No. Result **9**.

## 🎯 Your quest

**Part 1:** `quantize(block)`. Make the function read:

1. `biggest = 0`
2. `for w in block:`
3. `    if abs(w) > biggest:`
4. `        biggest = abs(w)`
5. `scale = 1.0` (already there: used if every weight is 0)
6. `if biggest > 0:`
7. `    scale = biggest / 7`
8. `qs = []` (already there)
9. `for w in block:`
10. `    q = round(w / scale)`
11. `    q = max(-8, min(7, q))`
12. `    qs.append(q)`
13. `return scale, qs` (already there)

**Part 2:** `dequantize(scale, qs)`. Replace `return []` with:

1. `restored = []`
2. `for q in qs:`
3. `    restored.append(q * scale)`
4. `return restored`

**Part 3:** press **Run** and look at the outlier block. Did its small weights survive, or did they turn into 0? Set `outlier_hurts` to `True` (they were hurt) or `False`.

## Review

<details><summary>What are the first four bytes of a GGUF file?</summary>The magic letters "GGUF".</details>
<details><summary>Name three things GGUF metadata stores besides the weights.</summary>For example: architecture, layer count, context length, tokenizer vocabulary and merges, chat template, quantization type.</details>
<details><summary>Block [0.7, −0.1]: what is the scale and what are the 4-bit values?</summary>Scale = 0.7 ÷ 7 = 0.1. 0.7 ÷ 0.1 = 7 and −0.1 ÷ 0.1 = −1, so [7, −1].</details>
