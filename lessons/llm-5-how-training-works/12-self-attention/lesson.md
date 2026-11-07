---
title: Let's build GPT: a causal self-attention head
minutes: 70
xp: 60
hint: H = len(Q[0]), then for t in range(len(X)): scores = [], for s in range(t + 1): scores.append(dot(Q[t], K[s]) / math.sqrt(H))
hint: Still in 'for t': weights = softmax(scores), then vec = []
hint: for h in range(len(V[0])): total = 0, for s in range(t + 1): total = total + weights[s] * V[s][h], then vec.append(total)
hint: Last line in 'for t' (8 spaces): out.append(vec)
---
# The heart of GPT, for a whole sequence

⏱️ About 70 minutes

> **Warm-up:** in LLMs 1 you computed attention for *one* query. During training, a model learns from every position of a sequence at once. What stops position 3 from simply looking at the answer at position 4?

The **causal mask**. Karpathy's *"Let's build GPT: from scratch, in code, spelled out"* builds a transformer around one head of **causal self-attention**. For a sequence `X` of `T` token vectors (each of size `C`):

```
Q = X @ Wq     K = X @ Wk     V = X @ Wv          (each T × H, H = head size)
scores[t][s] = Q[t] · K[s] / √H     if s ≤ t
             = −∞                   if s > t       ← the mask: no peeking at the future
weights = softmax of each row of scores            (e^−∞ = 0, so future tokens get weight 0)
out[t]  = Σₛ weights[t][s] · V[s]
```

Because of the mask, one forward pass over a sequence of `T` tokens produces `T` predictions at once, each using only earlier tokens: **one training example per position**. That's why transformers train so efficiently in parallel, and it's the same mask you met in LLMs 1, lesson 13.

The rest of a GPT, all of which you've now met:

- **Token embedding** + **position embedding** (learned in GPT-2; rotary RoPE in Llama/Qwen) so the model knows *what* and *where*. Without position information, attention can't tell word order.
- **Multi-head attention:** several heads in parallel, outputs concatenated and projected back to size `C`.
- **MLP** after attention, applied to each position separately.
- **Residual connections** (`x = x + attention(norm(x))`, `x = x + mlp(norm(x))`) and **normalization** (LayerNorm or RMSNorm) so deep stacks train.
- A final **linear layer** to vocabulary logits, then cross-entropy against the next token at **every** position.

Karpathy's `nanoGPT` repository implements all of this in about 300 lines of PyTorch. Once you have PyTorch with ROCm running (Module 6), training his Shakespeare character model on your GPU takes minutes.

## 🔬 Take the formulas apart

**Scores** <div class="formula">scores[t][s] = <span class="k1">Q[t] · K[s]</span> / <span class="k2">√H</span></div>
- `t` is the position asking, `s` a position being looked at.
- <span class="k1">Q[t] · K[s]</span>: a dot product (LLMs 4, lesson 3), "how well does s match what t is looking for?"
- <span class="k2">/ √H</span>: H is the head size (here 2). Dividing by √H keeps scores from growing just because vectors are longer.

**The mask** (s ≤ t): position t may only look at s = 0, 1, … t. In code you simply **don't compute** the others: `range(t + 1)`.

**Weights** = softmax of the scores (LLMs 1): positive numbers that add up to 1.

**Output** <div class="formula">out[t] = <span class="k3">Σₛ</span> <span class="k4">weights[s]</span> · <span class="k5">V[s]</span></div>
A weighted mix of the value vectors: <span class="k3">Σₛ</span> "add up over every allowed s". For each entry h of the output vector: weights[0]·V[0][h] + weights[1]·V[1][h] + …

**Numbers** for t = 1 with H = 1 (so √H = 1): Q[1] = [2], K[0] = [1], K[1] = [0], V[0] = [1, 0], V[1] = [0, 1].
1. scores: Q[1]·K[0] = 2, Q[1]·K[1] = 0 → [2, 0].
2. softmax: e² ≈ 7.39, e⁰ = 1, total 8.39 → weights ≈ [0.881, 0.119].
3. out[1][0] = 0.881·1 + 0.119·0 = **0.881**. out[1][1] = 0.881·0 + 0.119·1 = **0.119**.

Position 1 mostly copies position 0's value, because their query and key matched best.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len(Q[0])` | | the length of one query vector: the head size H |
| `for s in range(t + 1):` | | s = 0 … t: only the past and itself (the mask) |
| `dot(Q[t], K[s])` | | the given dot product |
| `V[s][h]` | | entry h of value vector s |
| `len(V[0])` | | how many entries each value vector has |

`matmul`, `dot` and `softmax` are given (written with plain loops).

### 👀 Worked example: a weighted mix

```python
weights = [0.25, 0.75]
V = [[4, 0], [0, 8]]
vec = []
for h in range(2):
    total = 0
    for s in range(2):
        total = total + weights[s] * V[s][h]
    vec.append(total)
print(vec)        # [1.0, 6.0]
```

1. h = 0: 0.25·4 + 0.75·0 = 1.
2. h = 1: 0.25·0 + 0.75·8 = 6.

## 🎯 Your quest

Write `causal_attention(X, Wq, Wk, Wv)`. Between `out = []` and `return out`, add:

1. `    H = len(Q[0])`
2. `    for t in range(len(X)):`
3. `        scores = []`
4. `        for s in range(t + 1):`
5. `            scores.append(dot(Q[t], K[s]) / math.sqrt(H))`
6. `        weights = softmax(scores)`
7. `        vec = []`
8. `        for h in range(len(V[0])):`
9. `            total = 0`
10. `            for s in range(t + 1):`
11. `                total = total + weights[s] * V[s][h]`
12. `            vec.append(total)`
13. `        out.append(vec)`

Position 0 can only look at itself, so its output is exactly V[0] = [1.5, 0.5].

## Review

<details><summary>Why can't a counting model scale to long contexts?</summary>The table needs a row for every possible context, which grows exponentially, and it can't generalize to unseen contexts.</details>
<details><summary>In the neural bigram model, what plays the role of the embedding lookup?</summary>Selecting row W[a] of the logits table, equivalent to a one-hot vector times W.</details>
