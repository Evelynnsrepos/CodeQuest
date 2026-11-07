---
title: Embeddings, meaning as direction
minutes: 35
xp: 30
hint: dot: total = 0, then for i in range(len(a)): and inside it total = total + a[i] * b[i], then return total
hint: cosine has one line: return dot(a, b) / (math.sqrt(dot(a, a)) * math.sqrt(dot(b, b)))
---
# From token ID to vector

⏱️ About 35 minutes

> **Warm-up:** token ID 412 and token ID 413 are neighbours in the vocabulary. Does that mean their meanings are similar?

No. IDs are arbitrary labels. So the very first thing a model does is look up each ID in an **embedding matrix**: a table with one row per vocabulary entry, each row a list of `d` numbers called a **vector**. In Llama 3 8B, `d` is 4,096 and the vocabulary has 128,256 tokens, so that one table alone holds about 525 million weights.

These vectors are learned during training, and they end up arranged so that **similar meanings point in similar directions**. You can measure that with the **dot product**:

```
a · b = a₁b₁ + a₂b₂ + … + a_d·b_d
```

The dot product is large when two vectors point the same way, near 0 when unrelated, negative when opposite. It also grows with the vectors' *length*, so to compare only direction you divide by both lengths. That's **cosine similarity**, always between −1 and 1:

```
cos(a, b) = (a · b) / (|a| · |b|)      where |a| = √(a · a)
```

Everything after this step is vector math. Each layer of the model adjusts every token's vector, mixing in information from other tokens (attention, next lesson) and from what the model knows (the MLP layers). At the end, the last token's vector is compared by dot products against one row per vocabulary entry (some models reuse the embedding table for this, others such as Llama 3 8B learn a separate output table), and those scores are the **logits** you met in lesson 5.

Embeddings are also the core of **RAG** (Module 3): you embed your documents and your question with an embedding model, then fetch the documents whose vectors have the highest cosine similarity to the question.

## 🔬 Take the formulas apart

**The dot product:** `a · b = a₁b₁ + a₂b₂ + … + a_d·b_d`

| Piece | Say it | Means | Example a = [3, 4], b = [4, 3] |
|---|---|---|---|
| `a₁`, `b₁` | "a one", "b one" | the first number of each vector (the small number is a position label) | 3 and 4 |
| `a₁b₁` | "a one times b one" | two letters written next to each other mean **multiply** | 3 × 4 = 12 |
| `+ … +` | "and so on" | do the same for every position | 4 × 3 = 12 |
| `d` | "d" | how many numbers each vector has | 2 |
| result | | add all the products | 12 + 12 = **24** |

**The length:** `|a| = √(a · a)`

The two straight lines `|a|` mean "the length of a". `√` is the **square root**: the number that, multiplied by itself, gives what's under it. √25 = 5, because 5 × 5 = 25.

`a · a` = 3 × 3 + 4 × 4 = 9 + 16 = 25. So |a| = √25 = **5**. (The old right-triangle rule: 3 right, 4 up is 5 long.)

**Cosine similarity:**

<div class="formula">cos(a, b) = <span class="k1">(a · b)</span> <span class="k2">/</span> <span class="k3">(|a| · |b|)</span></div>

| Piece | Means | Example |
|---|---|---|
| <span class="k1">a · b</span> | how much they point the same way, but also bigger for longer arrows | 24 |
| <span class="k2">/</span> | divided by | |
| <span class="k3">\|a\| · \|b\|</span> | both lengths multiplied: removes the "longer arrow" effect | 5 × 5 = 25 |

24 ÷ 25 = **0.96**: almost the same direction. 1 means the same direction, 0 unrelated, −1 opposite.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `a[i]` | "a at i" | the number at position `i` (positions start at 0) |
| `range(len(a))` | | all positions 0, 1, … of the list |
| `total = total + a[i] * b[i]` | | running total of the products |
| `math.sqrt(25)` | "square root of 25" | `5.0` |
| `dot(a, a)` | | calls your own `dot` with the same vector twice: that's `a · a` |

### 👀 Worked example: a running total over two lists

```python
def add_matching(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] + b[i]
    return total

print(add_matching([1, 2], [10, 20]))   # 33
```

i = 0: 0 + 1 + 10 = 11. i = 1: 11 + 2 + 20 = 33. Your `dot` is the same with `*` between `a[i]` and `b[i]`.

## 🎯 Your quest

**Part 1:** `dot(a, b)`. Replace `return 0` with:

1. `total = 0`
2. `for i in range(len(a)):`
3. `    total = total + a[i] * b[i]`
4. `return total`

**Part 2:** `cosine(a, b)`. Replace `return 0` with one line:

- `return dot(a, b) / (math.sqrt(dot(a, a)) * math.sqrt(dot(b, b)))`

Read it piece by piece: `dot(a, b)` on top, divided by length of a (`math.sqrt(dot(a, a))`) times length of b.

The program then shows how close every word is to `"king"` in a tiny 3-number embedding table.

## Review

<details><summary>What is a chat template, and who applies it in LM Studio?</summary>The format with special tokens that flattens a conversation into one string, exactly as the model was trained. LM Studio applies the template stored in the GGUF file.</details>
<details><summary>What is the difference between a base and an instruct model?</summary>A base model only continues text. An instruct model was further trained (SFT, then preference tuning) on conversations to follow requests.</details>
<details><summary>Write the softmax formula.</summary>softmax(zᵢ) = e^zᵢ / Σⱼ e^zⱼ</details>
<details><summary>What is √(3 · 3 + 4 · 4)?</summary>√25 = 5: the length of the vector [3, 4].</details>
