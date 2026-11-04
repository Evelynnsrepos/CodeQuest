---
title: Vision transformers and CLIP
xp: 50
---
# Images as tokens, and images meet text

> **Warm-up:** a transformer reads a sequence of token vectors. How could you turn a photo into a sequence?

Cut it into squares. A **Vision Transformer (ViT, 2020)** splits a 224×224 image into 16×16 **patches** (14 × 14 = 196 of them), flattens each patch into a vector, multiplies it by a learned matrix to get a token embedding, adds position embeddings, and runs a normal transformer. With enough data, ViTs match or beat CNNs and use exactly the same machinery as LLMs.

**CLIP** (OpenAI, 2021) connects images and text. It trains an image encoder and a text encoder together on 400 M image–caption pairs from the web with a **contrastive** loss: in a batch of N pairs, the N matching (image, caption) embeddings should have high cosine similarity and the N² − N wrong pairings low. It's a softmax cross-entropy over the similarity matrix, row-wise and column-wise.

The payoff is **zero-shot classification**: embed captions like "a photo of a cat", "a photo of a dog", embed the image, and pick the most similar caption, with no training on those classes. CLIP-style encoders are also the "eyes" of multimodal LLMs and guide many image generators.

## Your quest

`cosine` is given.

1. `patchify(image, p)`: `image` is a square list of rows, side divisible by `p`. Return the list of patches in reading order (left to right, then top to bottom), each flattened row by row.
2. `zero_shot(image_emb, text_embs, labels)`: the label whose text embedding has the highest cosine similarity to the image embedding.

## Review

<details><summary>How big is the output of a 3×3 kernel on a 10×10 image without padding?</summary>8×8.</details>
<details><summary>What did ResNet add that transformers later borrowed?</summary>Residual (skip) connections.</details>
