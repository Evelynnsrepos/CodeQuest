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

<svg viewBox="0 0 560 250" width="100%" style="max-width:560px" role="img" aria-label="Attention: the query of the token it is compared with the key of every earlier token, softmax turns the scores into weights, and the weighted sum of the values is its new vector"><defs><marker id="ah2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs><rect x="20" y="20" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="37.0" font-size="13" fill="currentColor" text-anchor="middle">The</text><text x="65.0" y="53.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="72" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="89.0" font-size="13" fill="currentColor" text-anchor="middle">cat</text><text x="65.0" y="105.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="124" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="141.0" font-size="13" fill="currentColor" text-anchor="middle">didn't</text><text x="65.0" y="157.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="176" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="193.0" font-size="13" fill="currentColor" text-anchor="middle">eat</text><text x="65.0" y="209.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="210" width="90" height="34" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="65.0" y="231.33333333333334" font-size="13" fill="currentColor" text-anchor="middle">it</text><text x="65" y="206" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">query ↓</text><line x1="112" y1="39" x2="196" y2="39" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><line x1="112" y1="91" x2="196" y2="91" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><line x1="112" y1="143" x2="196" y2="143" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><line x1="112" y1="195" x2="196" y2="195" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><rect x="200" y="22" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="43.0" font-size="12" fill="currentColor" text-anchor="middle">score 0.3</text><rect x="200" y="74" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="95.0" font-size="12" fill="currentColor" text-anchor="middle">score 2.4</text><rect x="200" y="126" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="147.0" font-size="12" fill="currentColor" text-anchor="middle">score 0.3</text><rect x="200" y="178" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="199.0" font-size="12" fill="currentColor" text-anchor="middle">score 1.2</text><text x="255" y="238" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">score = query · key ÷ √d</text><line x1="312" y1="120" x2="352" y2="120" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><text x="332.0" y="114.0" font-size="11" fill="currentColor" opacity=".8" text-anchor="middle">softmax</text><rect x="356" y="22" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="43.0" font-size="12" fill="currentColor" text-anchor="middle">0.07</text><rect x="356" y="74" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="95.0" font-size="12" fill="currentColor" text-anchor="middle">0.66</text><rect x="356" y="126" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="147.0" font-size="12" fill="currentColor" text-anchor="middle">0.07</text><rect x="356" y="178" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="199.0" font-size="12" fill="currentColor" text-anchor="middle">0.20</text><line x1="428" y1="120" x2="456" y2="120" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><rect x="460" y="80" width="90" height="80" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="505.0" y="118.0" font-size="13" fill="currentColor" text-anchor="middle">new “it”</text><text x="505.0" y="134.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">Σ weight · value</text><text x="391" y="238" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">weights add up to 1</text></svg>

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
