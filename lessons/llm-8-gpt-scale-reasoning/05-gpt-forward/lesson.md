---
title: A whole GPT forward pass
xp: 70
---
# Put every part together

> **Warm-up:** list, in order, what happens to the token IDs `[0, 3, 5]` between entering a GPT and coming out as probabilities for the next token.

Here's the whole thing, Llama-style (pre-norm, RMSNorm, RoPE, single head to keep it short):

```
x = [embedding row of each token]                       # LLMs 1, lesson 11
for each layer:
    h = [rms_norm(row) for row in x]
    Q = [rope(Wq·h[i], i)],  K = [rope(Wk·h[i], i)],  V = [Wv·h[i]]
    a = causal_attention(Q, K, V)
    x[i] = x[i] + Wo·a[i]                               # residual 1
    x[i] = x[i] + W2·gelu(W1·rms_norm(x[i]))            # residual 2 (MLP)
last = rms_norm(x[-1])
logits = [dot(row, last) for row in wte]                # tied output head
probs = softmax(logits)
```

The **output head** turns the final vector back into one score per vocabulary token. Many small models (GPT-2, Gemma) **tie** it to the embedding table: the same `wte` matrix is used to read tokens in and to score them out, saving `vocab × d` parameters. Llama 3 8B doesn't tie (its head is separate).

This is the same computation LM Studio runs for every token you see; the real one has 32 layers, 32 heads, `d = 4096`, and a KV cache so earlier positions' K and V aren't recomputed (LLMs 1, lesson 7).

**On your machine:** Karpathy's *Let's build GPT: from scratch, in code, spelled out* (YouTube, 2 h) builds this in PyTorch and trains it on Shakespeare. Then `nanoGPT` / `build-nanogpt` on GitHub reproduce GPT-2 124M.

## Your quest

All parts are given. Write `gpt_forward(tokens, P)` following the pseudocode. `P["wte"]` is the embedding table, `P["layers"]` a list of dicts with `Wq, Wk, Wv, Wo, W1, W2`. Return the probability list for the token **after** the last one.

## Review

<details><summary>Why does RoPE make attention depend on relative position?</summary>Rotating q by mθ and k by nθ makes their dot product depend only on (m − n)θ.</details>
<details><summary>Why is GELU applied between W1 and W2?</summary>Without a non-linearity, two matrices in a row collapse into one linear map.</details>
