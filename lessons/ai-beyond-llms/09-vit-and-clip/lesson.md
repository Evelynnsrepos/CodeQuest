---
title: Vision transformers and CLIP
minutes: 40
xp: 50
hint: patchify: for r in range(0, n, p): and for c in range(0, n, p): are the top-left corners. For each, patch = [] and two loops over i and j appending image[r + i][c + j]
hint: patchify: after the two inner loops, patches.append(patch). Return patches at the end
hint: zero_shot: best = 0 and best_s = cosine(image_emb, text_embs[0]), then for i in range(1, len(text_embs)): keep the higher score. Return labels[best]
---
# Images as tokens, and images meet text

⏱️ About 40 minutes

> **Warm-up:** a transformer reads a sequence of token vectors. How could you turn a photo into a sequence?

Cut it into squares. A **Vision Transformer (ViT, 2020)** splits a 224×224 image into 16×16 **patches** (14 × 14 = 196 of them), flattens each patch into a vector, multiplies it by a learned matrix to get a token embedding, adds position embeddings, and runs a normal transformer. With enough data, ViTs match or beat CNNs and use exactly the same machinery as LLMs.

**CLIP** (OpenAI, 2021) connects images and text. It trains an image encoder and a text encoder together on 400 M image–caption pairs from the web with a **contrastive** loss: in a batch of N pairs, the N matching (image, caption) embeddings should have high cosine similarity and the N² − N wrong pairings low. It's a softmax cross-entropy over the similarity matrix, row-wise and column-wise.

The payoff is **zero-shot classification**: embed captions like "a photo of a cat", "a photo of a dog", embed the image, and pick the most similar caption, with no training on those classes. CLIP-style encoders are also the "eyes" of multimodal LLMs and guide many image generators.

## 🔬 Take the cosine apart

`cosine(a, b)` is **given**:

<div class="formula">cos = <span class="k1">a·b</span> / ( <span class="k2">|a|</span> · <span class="k3">|b|</span> )</div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">a·b</span> | "a dot b" | multiply pair by pair, then add |
| <span class="k2">\|a\|</span> | "the length of a" | √(a₁² + a₂² + ...). `√` is the **square root**: the number that times itself gives what's inside. √9 = 3. |

Image embedding a = (1, 0). Two captions: b = (10, 1) and c = (1, 1).

1. a·b = 1·10 + 0·1 = 10. |a| = √(1 + 0) = 1. |b| = √(100 + 1) = 10.05. cos = 10 / 10.05 = **0.995**.
2. a·c = 1·1 + 0·1 = 1. |c| = √(1 + 1) = 1.414. cos = 1 / 1.414 = **0.707**.

b wins, because it points in almost the same **direction** as a. Dividing by the lengths makes the size of the vectors not matter.

**Patches by hand**: a 4 × 4 image with letters

```
a b c d
e f g h
i j k l
m n o p
```

and p = 2 has four patches. Reading order is left to right, then top to bottom; each patch is read row by row: `[a, b, e, f]`, `[c, d, g, h]`, `[i, j, m, n]`, `[k, l, o, p]`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for r in range(0, n, p):` | | `r` = 0, p, 2p, ...: the top row of each patch |
| `for c in range(0, n, p):` | | `c`: the left column of each patch |
| `image[r + i][c + j]` | | the cell i rows down and j columns right of that corner |
| `range(1, len(text_embs))` | | starts at 1, because number 0 is already the "best so far" |
| `labels[best]` | | the caption text at the winning position |

## 🎯 Your quest

`cosine` is given.

1. `patchify(image, p)`: `image` is a square list of rows, side divisible by `p`. Return the list of patches in reading order (left to right, then top to bottom), each flattened row by row.
2. `zero_shot(image_emb, text_embs, labels)`: the label whose text embedding has the highest cosine similarity to the image embedding.

**Part 1:** `patchify`. Replace `return []` with:

1. `n = len(image)`
2. `patches = []`
3. `for r in range(0, n, p):`
4. `    for c in range(0, n, p):`
5. `        patch = []`
6. `        for i in range(p):`
7. `            for j in range(p):`
8. `                patch.append(image[r + i][c + j])`
9. `        patches.append(patch)`
10. `return patches`

**Part 2:** `zero_shot`. Replace `return labels[0]` with:

1. `best = 0`
2. `best_s = cosine(image_emb, text_embs[0])`
3. `for i in range(1, len(text_embs)):`
4. `    s = cosine(image_emb, text_embs[i])`
5. `    if s > best_s:`
6. `        best = i`
7. `        best_s = s`
8. `return labels[best]`

## Review

<details><summary>How big is the output of a 3×3 kernel on a 10×10 image without padding?</summary>8×8.</details>
<details><summary>What did ResNet add that transformers later borrowed?</summary>Residual (skip) connections.</details>
