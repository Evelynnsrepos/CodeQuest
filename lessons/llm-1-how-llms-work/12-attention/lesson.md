---
title: Attention
xp: 40
---
# How a token looks at other tokens

> **Warm-up:** in "The animal didn't cross the street because **it** was too tired", how do *you* know what "it" means? What would a model need to do to know it?

The word "it" needs information from "animal". **Attention** is the mechanism that lets each token pull in information from other tokens. It is the heart of the **transformer**, the architecture from the 2017 paper *Attention Is All You Need*, which every modern LLM is built on.

Each token's vector is turned (by three learned weight matrices) into three new vectors:

- a **query** `q`: "what am I looking for?"
- a **key** `k`: "what do I contain?"
- a **value** `v`: "what will I pass on if someone attends to me?"

For one token's query, attention does this:

1. **Score** every key: `score = (q · k) / √d`, where `d` is the vector length.
2. **Softmax** the scores into weights that add up to 1.
3. **Output** = weighted sum of the value vectors.

```
q("it") · k("animal") → high score → weight 0.8
q("it") · k("street") → low score  → weight 0.1 ...
output = 0.8·v("animal") + 0.1·v("street") + …
```

**Why divide by √d?** A dot product of two random vectors with `d` entries grows with `d` (its variance is about `d`). With `d = 128`, raw scores get so large that softmax puts ~100% on one key and the gradients during training vanish. Dividing by √d keeps the scores at a sensible size. That is the "scaled" in *scaled dot-product attention*.

**The rest of the transformer**, at a glance:

- **Multi-head:** each layer runs many attention "heads" in parallel (Llama 3 8B: 32 heads), each with its own matrices, so different heads can track different relationships (grammar, references, position…).
- **MLP (feed-forward):** after attention, each token's vector goes through a two-layer neural network on its own. Most of the parameters, and much of the stored knowledge, live here.
- **Residual connections and normalization:** each block *adds* its result to the token's vector instead of replacing it, which keeps very deep stacks trainable.
- **Layers:** the attention + MLP block repeats (32 times in Llama 3 8B). Early layers handle surface patterns, later ones more abstract meaning.

## Your quest

Write `attend(q, keys, values)` for one query. `dot` and `softmax` are given.

1. Make a list of scores: `dot(q, k) / math.sqrt(len(q))` for every key.
2. Turn them into `weights` with `softmax`.
3. Start `output` as a list of zeros the length of a value vector, then for each weight `w` and value `v`, add `w * v[i]` to `output[i]` for every position `i`.

## Watch

- 3Blue1Brown, *Deep Learning* series, chapters 5 to 7 (transformers, attention, how LLMs store facts). Watch after this lesson; it will click.
- Andrej Karpathy, *Intro to Large Language Models* (1-hour talk): the big picture of everything in this course so far.

## Review

<details><summary>What does cosine similarity measure that the dot product doesn't?</summary>Only the angle (direction) between vectors, not their lengths. It ranges from −1 to 1.</details>
<details><summary>What is an embedding matrix?</summary>A learned table with one vector per vocabulary token. The model's first step is looking up each token ID's row.</details>
