---
title: Attention
minutes: 45
xp: 40
hint: Step 1, after scores = []: for k in keys: and inside it scores.append(dot(q, k) / math.sqrt(len(q)))
hint: Step 3: for j in range(len(values)): then w = weights[j] and v = values[j]
hint: Inside that loop, a second loop: for i in range(len(v)): and inside it output[i] = output[i] + w * v[i]
---
# How a token looks at other tokens

⏱️ About 45 minutes

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

<svg viewBox="0 0 560 300" width="100%" style="max-width:560px" role="img" aria-label="Attention: the query of the token it is compared with the key of every earlier token, softmax turns the scores into weights, and the weighted sum of the values is its new vector"><defs><marker id="ah2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs><rect x="20" y="20" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="37.0" font-size="13" fill="currentColor" text-anchor="middle">The</text><text x="65.0" y="53.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="72" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="89.0" font-size="13" fill="currentColor" text-anchor="middle">cat</text><text x="65.0" y="105.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="124" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="141.0" font-size="13" fill="currentColor" text-anchor="middle">didn't</text><text x="65.0" y="157.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="176" width="90" height="38" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="65.0" y="193.0" font-size="13" fill="currentColor" text-anchor="middle">eat</text><text x="65.0" y="209.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">key, value</text><rect x="20" y="236" width="90" height="34" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="65.0" y="257.3" font-size="13" fill="currentColor" text-anchor="middle">it</text><text x="120" y="258" font-size="11" fill="currentColor" text-anchor="start" font-weight="normal">its query is compared with every key ↑</text><line x1="112" y1="39" x2="196" y2="39" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><line x1="112" y1="91" x2="196" y2="91" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><line x1="112" y1="143" x2="196" y2="143" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><line x1="112" y1="195" x2="196" y2="195" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><rect x="200" y="22" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="43.0" font-size="12" fill="currentColor" text-anchor="middle">score 0.3</text><rect x="200" y="74" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="95.0" font-size="12" fill="currentColor" text-anchor="middle">score 2.4</text><rect x="200" y="126" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="147.0" font-size="12" fill="currentColor" text-anchor="middle">score 0.3</text><rect x="200" y="178" width="110" height="34" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="255.0" y="199.0" font-size="12" fill="currentColor" text-anchor="middle">score 1.2</text><text x="255" y="226" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">score = query · key ÷ √d</text><line x1="312" y1="120" x2="352" y2="120" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><text x="332.0" y="114.0" font-size="11" fill="currentColor" opacity=".8" text-anchor="middle">softmax</text><rect x="356" y="22" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="43.0" font-size="12" fill="currentColor" text-anchor="middle">0.08</text><rect x="356" y="74" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="95.0" font-size="12" fill="currentColor" text-anchor="middle">0.65</text><rect x="356" y="126" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="147.0" font-size="12" fill="currentColor" text-anchor="middle">0.08</text><rect x="356" y="178" width="70" height="34" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="391.0" y="199.0" font-size="12" fill="currentColor" text-anchor="middle">0.19</text><line x1="428" y1="120" x2="456" y2="120" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah2)"/><rect x="460" y="80" width="90" height="80" rx="8" fill="#e5484d" fill-opacity=".14" stroke="#e5484d" stroke-width="2"/><text x="505.0" y="118.0" font-size="13" fill="currentColor" text-anchor="middle">new “it”</text><text x="505.0" y="134.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">Σ weight · value</text><text x="391" y="226" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">weights add up to 1</text></svg>

**The rest of the transformer**, at a glance:

- **Multi-head:** each layer runs many attention "heads" in parallel (Llama 3 8B: 32 heads), each with its own matrices, so different heads can track different relationships (grammar, references, position…).
- **MLP (feed-forward):** after attention, each token's vector goes through a two-layer neural network on its own. Most of the parameters, and much of the stored knowledge, live here.
- **Residual connections and normalization:** each block *adds* its result to the token's vector instead of replacing it, which keeps very deep stacks trainable.
- **Layers:** the attention + MLP block repeats (32 times in Llama 3 8B). Early layers handle surface patterns, later ones more abstract meaning.

## 🔬 Take the formulas apart

<div class="formula">score = <span class="k1">(q · k)</span> <span class="k2">/ √d</span></div>
<div class="formula">output = <span class="k3">w₁·v₁ + w₂·v₂ + … </span></div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">q · k</span> | "q dot k" | the dot product from lesson 11: multiply matching numbers, add up. Big when the query and key point the same way. |
| `d` | "d" | how many numbers the query has. Here 4. |
| <span class="k2">/ √d</span> | "divided by the square root of d" | √4 = 2. Keeps the scores from getting too big for softmax. |
| `w₁`, `w₂`, … | "weight one, weight two" | the scores after softmax: they add up to 1 |
| <span class="k3">w₁·v₁ + w₂·v₂ + …</span> | "weighted sum of the values" | multiply each value **vector** by its weight, then add the vectors **position by position** |

**The quest's numbers, step by step.** The query for "it" is [2, 0.5, 0, 1].

1. **Scores.** q · k for animal = 2·2 + 0.5·1 + 0·0 + 1·1 = 5.5. For street = 0.5, for because = 1.0. Divided by √4 = 2: **2.75, 0.25, 0.5**.
2. **Softmax** (lesson 5): weights ≈ **0.84, 0.07, 0.09**. Most of the attention goes to "animal".
3. **Weighted sum** of the values [1, 0], [0, 1] and [0.5, 0.5], one position at a time:
   - position 0: 0.84·1 + 0.07·0 + 0.09·0.5 ≈ **0.886**
   - position 1: 0.84·0 + 0.07·1 + 0.09·0.5 ≈ **0.114**

The new vector for "it" is [0.886, 0.114]: mostly "animal".

## 🐍 Python you need

`dot` and `softmax` are given in the starter.

| You write | Say it | What it does |
|---|---|---|
| `math.sqrt(len(q))` | "square root of the length of q" | √d |
| `scores.append(x)` | | adds a score to the list |
| `[0.0] * 3` | "a list of three zeros" | `[0.0, 0.0, 0.0]`: a list repeated 3 times. The starter makes `output` like this. |
| `for j in range(len(values)):` | | goes over the positions of the values list, so `weights[j]` and `values[j]` belong together |
| `output[i] = output[i] + w * v[i]` | | adds to one position of the output list |
| a loop inside a loop | | for **each** value vector, go over **each** of its positions |

### 👀 Worked example: mixing two paint colours

Each colour is [red, blue]. Mix 75% of colour A and 25% of colour B:

```python
weights = [0.75, 0.25]
colours = [[1.0, 0.0], [0.0, 1.0]]
mix = [0.0] * 2
for j in range(len(colours)):
    w = weights[j]
    c = colours[j]
    for i in range(len(c)):
        mix[i] = mix[i] + w * c[i]
print(mix)   # [0.75, 0.25]
```

1. `mix` = [0, 0].
2. j = 0 (w = 0.75, c = [1, 0]): position 0 gets + 0.75, position 1 gets + 0. `mix` = [0.75, 0].
3. j = 1 (w = 0.25, c = [0, 1]): position 0 gets + 0, position 1 gets + 0.25. `mix` = [0.75, 0.25].

That's exactly step 3 of attention.

## 🎯 Your quest

Write `attend(q, keys, values)` for one query. `dot` and `softmax` are given. Make the function read:

1. `scores = []`
2. `for k in keys:`
3. `    scores.append(dot(q, k) / math.sqrt(len(q)))`
4. `weights = softmax(scores)`
5. `output = [0.0] * len(values[0])`
6. `for j in range(len(values)):`
7. `    w = weights[j]`
8. `    v = values[j]`
9. `    for i in range(len(v)):`
10. `        output[i] = output[i] + w * v[i]`
11. `return output`

Lines 1, 4, 5 and 11 are already there. It should print `[0.886, 0.114]`.

## Watch

- 3Blue1Brown, *Deep Learning* series, chapters 5 to 7 (transformers, attention, how LLMs store facts). Watch after this lesson; it will click.
- Andrej Karpathy, *Intro to Large Language Models* (1-hour talk): the big picture of everything in this course so far.

## Review

<details><summary>What does cosine similarity measure that the dot product doesn't?</summary>Only the angle (direction) between vectors, not their lengths. It ranges from −1 to 1.</details>
<details><summary>What is an embedding matrix?</summary>A learned table with one vector per vocabulary token. The model's first step is looking up each token ID's row.</details>
<details><summary>Scores 4 and 0 with d = 4: what goes into softmax?</summary>4 ÷ √4 = 2 and 0 ÷ 2 = 0.</details>
