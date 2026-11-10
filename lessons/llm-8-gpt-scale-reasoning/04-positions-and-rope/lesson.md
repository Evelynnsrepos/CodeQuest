---
title: Positions: sinusoidal and RoPE
minutes: 60
xp: 50
hint: sinusoidal: pe = [], for i in range(d // 2): a = pos / 10000 ** (2 * i / d), then pe.append(math.sin(a)) and pe.append(math.cos(a))
hint: rope: d = len(x), out = [], for i in range(d // 2): a = pos * base ** (-2 * i / d), x0 = x[2 * i], x1 = x[2 * i + 1]
hint: rope, the two appends: out.append(x0 * math.cos(a) - x1 * math.sin(a)) and out.append(x0 * math.sin(a) + x1 * math.cos(a))
---
# How does the model know word order?

⏱️ About 60 minutes

> **Warm-up:** attention computes `q · k` for pairs of tokens. If you shuffled the words of a sentence, would any of those dot products change?

No. Attention by itself is blind to order, yet "dog bites man" ≠ "man bites dog". Position has to be put in.

**Sinusoidal encodings** (*Attention Is All You Need*, 2017) **add** a fixed vector to each token's embedding. For position `pos` and pair index `i = 0, 1, …, d/2 − 1`:

```
PE[2i]   = sin(pos / 10000^(2i/d))
PE[2i+1] = cos(pos / 10000^(2i/d))
```

Every pair is a clock hand turning at its own speed: fast for small `i`, very slow for large `i`. GPT-2 instead **learned** a position table, which can't go beyond its trained length (1024).

**RoPE** (rotary position embedding, Su et al. 2021), used by Llama, Qwen, Mistral and most current models, doesn't add anything. It **rotates** each pair `(x[2i], x[2i+1])` of the query and key by the angle `pos · θ_i` with `θ_i = 10000^(−2i/d)`:

```
x'[2i]   = x[2i]·cos(a) − x[2i+1]·sin(a)
x'[2i+1] = x[2i]·sin(a) + x[2i+1]·cos(a)      with a = pos · θ_i
```

The beautiful part: rotating q by angle `m·θ` and k by `n·θ` makes their dot product depend only on **the difference `m − n`**. So attention scores see *relative* distance, which generalizes better. Context-extension tricks like **YaRN** work by rescaling these θ values, which is how models trained on 8K tokens get stretched to 128K.

## 🔬 Take the formulas apart

**sin and cos.** Picture a clock hand of length 1 turned by an angle `a` (measured in "radians": a full turn is 2π ≈ 6.28). **cos(a)** is how far the tip is to the right, **sin(a)** how far up. a = 0: (cos, sin) = (1, 0). A quarter turn, a = π/2 ≈ 1.57: (0, 1).

**Sinusoidal** <div class="formula">PE[2i] = sin(<span class="k1">pos</span> / <span class="k2">10000^(2i/d)</span>), &nbsp; PE[2i+1] = cos(same)</div>
- Numbers come in **pairs** (positions 2i and 2i + 1). i counts the pairs: 0, 1, … d/2 − 1.
- <span class="k2">10000^(2i/d)</span>: `^` means "to the power of". For i = 0 it's 10000⁰ = 1; for bigger i it gets huge, so the hand turns **slower**.

Numbers, pos = 1, d = 4:
1. i = 0: 10000^(0/4) = 1, a = 1/1 = 1. sin 1 ≈ 0.841, cos 1 ≈ 0.540.
2. i = 1: 10000^(2/4) = 10000^0.5 = √10000 = 100, a = 1/100 = 0.01. sin 0.01 ≈ 0.010, cos 0.01 ≈ 1.000.
3. PE = **[0.8415, 0.5403, 0.01, 1.0]**.

**RoPE: rotating a pair** <div class="formula">x'₀ = x₀·cos(a) − x₁·sin(a), &nbsp; x'₁ = x₀·sin(a) + x₁·cos(a)</div>
These two lines turn the arrow (x₀, x₁) by angle a, keeping its length. Check with a quarter turn (cos = 0, sin = 1) on (1, 0): x'₀ = 1·0 − 0·1 = 0, x'₁ = 1·1 + 0·0 = 1 → **(0, 1)**: the arrow now points up. ✅

The angle is a = pos · base^(−2i/d). The minus in the power means "1 divided by": 10000^(−0.5) = 1/100.

**Why it's clever.** Turn q by m steps and k by n steps: their dot product only depends on how far apart they are, **m − n**. That's why the program prints the same score for (3, 1), (10, 8) and (52, 50).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `range(d // 2)` | | one round per pair |
| `10000 ** (2 * i / d)` | | 10000^(2i/d) |
| `base ** (-2 * i / d)` | | the same with a minus: 1 / base^(2i/d) |
| `math.sin(a)`, `math.cos(a)` | | sine, cosine |
| `x[2 * i]`, `x[2 * i + 1]` | | the two numbers of pair i |
| two `append`s per round | | the pair's two new numbers, in order |

### 👀 Worked example: rotating (1, 0) by a = 1

```python
a = 1
x0, x1 = 1.0, 0.0
print(x0 * math.cos(a) - x1 * math.sin(a))   # 0.540
print(x0 * math.sin(a) + x1 * math.cos(a))   # 0.841
```

The arrow (1, 0) turned to (0.540, 0.841): the same as (cos 1, sin 1).

## 🎯 Your quest

`sinusoidal(pos, d)`: replace `return [0.0] * d` with:

1. `    pe = []`
2. `    for i in range(d // 2):`
3. `        a = pos / 10000 ** (2 * i / d)`
4. `        pe.append(math.sin(a))`
5. `        pe.append(math.cos(a))`
6. `    return pe`

`rope(x, pos, base=10000)`: replace `return list(x)` with:

1. `    d = len(x)`
2. `    out = []`
3. `    for i in range(d // 2):`
4. `        a = pos * base ** (-2 * i / d)`
5. `        x0 = x[2 * i]`
6. `        x1 = x[2 * i + 1]`
7. `        out.append(x0 * math.cos(a) - x1 * math.sin(a))`
8. `        out.append(x0 * math.sin(a) + x1 * math.cos(a))`
9. `    return out`

Run it: the three printed scores are equal, because each pair is 2 positions apart.

## Review

<details><summary>Why does a residual connection help gradients?</summary>The + passes the gradient straight through (its derivative is 1), so it reaches early layers.</details>
<details><summary>Roughly what share of a transformer's parameters sit in the MLPs?</summary>About two thirds.</details>
