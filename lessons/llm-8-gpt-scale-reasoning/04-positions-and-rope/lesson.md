---
title: Positions: sinusoidal and RoPE
xp: 50
---
# How does the model know word order?

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

## Your quest

1. `sinusoidal(pos, d)`: the list of `d` numbers above.
2. `rope(x, pos, base=10000)`: return the rotated copy of `x` (length `d`, even).

Run it: the three printed scores are equal, because each pair is 2 positions apart.

## Review

<details><summary>Why does a residual connection help gradients?</summary>The + passes the gradient straight through (its derivative is 1), so it reaches early layers.</details>
<details><summary>Roughly what share of a transformer's parameters sit in the MLPs?</summary>About two thirds.</details>
