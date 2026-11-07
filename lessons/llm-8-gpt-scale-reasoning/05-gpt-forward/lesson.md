---
title: A whole GPT forward pass
minutes: 70
xp: 70
hint: Start: x = [], for t in tokens: x.append(list(P["wte"][t]))
hint: In each layer: build Q, K, V with one loop over i: h = rms_norm(x[i]), Q.append(rope(matvec(L["Wq"], h), i)), the same for K, and V.append(matvec(L["Wv"], h))
hint: Residual 1: a = causal_attention(Q, K, V), then for each i: o = matvec(L["Wo"], a[i]) and x[i][c] = x[i][c] + o[c] for every c
hint: Residual 2: for each i: hidden = matvec(L["W1"], rms_norm(x[i])), g = gelu of each, m = matvec(L["W2"], g), x[i][c] = x[i][c] + m[c]
hint: After the layers: last = rms_norm(x[-1]), logits = dot(row, last) for each row of P["wte"], return softmax(logits)
---
# Put every part together

⏱️ About 70 minutes

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

<svg viewBox="0 0 420 470" width="100%" style="max-width:420px" role="img" aria-label="A GPT from bottom to top: token ids, embeddings plus positions, N transformer blocks each with layer norm, attention and a residual add, then layer norm, MLP and a residual add, then a final norm, logits and softmax"><defs><marker id="ah5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs><rect x="110" y="420" width="200" height="36" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="210.0" y="442.0" font-size="12" fill="currentColor" text-anchor="middle">token ids  [464, 3797, 3332]</text><line x1="210" y1="418" x2="210" y2="392" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><rect x="110" y="354" width="200" height="36" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="210.0" y="376.3333333333333" font-size="13" fill="currentColor" text-anchor="middle">embedding + position</text><line x1="210" y1="352" x2="210" y2="326" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><rect x="60" y="120" width="300" height="204" rx="12" fill="none" stroke="currentColor" stroke-opacity=".5" stroke-dasharray="6 4" stroke-width="1.5"/><text x="370" y="226" font-size="16" fill="currentColor" text-anchor="start" font-weight="bold">× N</text><text x="370" y="244" font-size="11" fill="currentColor" text-anchor="start" font-weight="normal">blocks</text><rect x="110" y="280" width="200" height="32" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="210.0" y="300.3333333333333" font-size="13" fill="currentColor" text-anchor="middle">LayerNorm → attention</text><rect x="170" y="236" width="80" height="28" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="210.0" y="254.0" font-size="12" fill="currentColor" text-anchor="middle">+ add</text><rect x="110" y="180" width="200" height="32" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="210.0" y="200.33333333333334" font-size="13" fill="currentColor" text-anchor="middle">LayerNorm → MLP</text><rect x="170" y="136" width="80" height="28" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="210.0" y="154.0" font-size="12" fill="currentColor" text-anchor="middle">+ add</text><line x1="210" y1="278" x2="210" y2="266" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><line x1="210" y1="234" x2="210" y2="214" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><line x1="210" y1="178" x2="210" y2="166" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><path d="M 210 320 L 80 320 L 80 250 L 168 250" fill="none" stroke="#30a46c" stroke-width="1.6" marker-end="url(#ah5)"/><path d="M 210 224 L 80 224 L 80 150 L 168 150" fill="none" stroke="#30a46c" stroke-width="1.6" marker-end="url(#ah5)"/><text x="20" y="196" font-size="10" fill="#30a46c" text-anchor="start" font-weight="normal">residual</text><text x="20" y="208" font-size="10" fill="#30a46c" text-anchor="start" font-weight="normal">highway</text><line x1="210" y1="134" x2="210" y2="108" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><rect x="110" y="70" width="200" height="36" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="210.0" y="92.33333333333333" font-size="13" fill="currentColor" text-anchor="middle">final norm → logits</text><line x1="210" y1="68" x2="210" y2="50" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah5)"/><rect x="110" y="14" width="200" height="34" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="210.0" y="35.333333333333336" font-size="13" fill="currentColor" text-anchor="middle">softmax → next token</text></svg>

## 🐍 Python you need

All the helpers are given. You only connect them.

| You write | Say it | What it does |
|---|---|---|
| `list(P["wte"][t])` | | a **copy** of token t's embedding row, so changing x doesn't change the table |
| `for L in P["layers"]:` | | each layer is a dictionary of matrices |
| `L["Wq"]` | | that layer's query matrix |
| `rope(matvec(L["Wq"], h), i)` | | query = Wq·h, then rotated for position i |
| `x[i][c] = x[i][c] + o[c]` | | the residual: add, entry by entry, **into** x |
| `x[-1]` | | the last token's vector: it predicts the next one |

### 👀 Worked example: the shape of one layer

Tokens [0, 3, 5] → 3 vectors of size 4.

1. For each of the 3 positions: normalize, make its q, k (rotated) and v.
2. Attention mixes the 3 v's, each position looking only backwards.
3. Each position adds Wo·(its attention output) to itself.
4. Each position adds its own MLP output to itself.

After 2 layers, the last vector is compared (dot product) with all 6 embedding rows → 6 scores → softmax → 6 probabilities that add up to 1.

## 🎯 Your quest

Write `gpt_forward(tokens, P)`. Replace `return []` with these lines (the indentation shows what's inside what):

1. `    x = []`
2. `    for t in tokens:`
3. `        x.append(list(P["wte"][t]))`
4. `    for L in P["layers"]:`
5. `        Q = []`
6. `        K = []`
7. `        V = []`
8. `        for i in range(len(x)):`
9. `            h = rms_norm(x[i])`
10. `            Q.append(rope(matvec(L["Wq"], h), i))`
11. `            K.append(rope(matvec(L["Wk"], h), i))`
12. `            V.append(matvec(L["Wv"], h))`
13. `        a = causal_attention(Q, K, V)`
14. `        for i in range(len(x)):`
15. `            o = matvec(L["Wo"], a[i])`
16. `            for c in range(len(x[i])):`
17. `                x[i][c] = x[i][c] + o[c]`
18. `        for i in range(len(x)):`
19. `            hidden = matvec(L["W1"], rms_norm(x[i]))`
20. `            g = []`
21. `            for z in hidden:`
22. `                g.append(gelu(z))`
23. `            m = matvec(L["W2"], g)`
24. `            for c in range(len(x[i])):`
25. `                x[i][c] = x[i][c] + m[c]`
26. `    last = rms_norm(x[-1])`
27. `    logits = []`
28. `    for row in P["wte"]:`
29. `        logits.append(dot(row, last))`
30. `    return softmax(logits)`

It prints six probabilities; the biggest is 0.403 for token 3.

## Review

<details><summary>Why does RoPE make attention depend on relative position?</summary>Rotating q by mθ and k by nθ makes their dot product depend only on (m − n)θ.</details>
<details><summary>Why is GELU applied between W1 and W2?</summary>Without a non-linearity, two matrices in a row collapse into one linear map.</details>
