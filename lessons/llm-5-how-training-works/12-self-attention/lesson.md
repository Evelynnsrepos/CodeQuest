---
title: Let's build GPT: a causal self-attention head
xp: 60
---
# The heart of GPT, for a whole sequence

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

## Your quest

Write `causal_attention(X, Wq, Wk, Wv)` using the given `matmul`, `dot` and `softmax`. Build `Q`, `K`, `V`; for each position `t` compute scores for `s = 0 … t` only (skipping future positions has the same effect as −∞), softmax them, and return the list of output vectors.

## Review

<details><summary>Why can't a counting model scale to long contexts?</summary>The table needs a row for every possible context, which grows exponentially, and it can't generalize to unseen contexts.</details>
<details><summary>In the neural bigram model, what plays the role of the embedding lookup?</summary>Selecting row W[a] of the logits table, equivalent to a one-hot vector times W.</details>
