---
title: Embeddings, meaning as direction
xp: 30
---
# From token ID to vector

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

## Python you need

`math.sqrt(x)` is the square root.

## Your quest

1. Write `dot(a, b)`.
2. Write `cosine(a, b)` using `dot` and `math.sqrt`.

The program then finds the word closest to `"king"` in a tiny 3-dimensional embedding table.

## Review

<details><summary>What is a chat template, and who applies it in LM Studio?</summary>The format with special tokens that flattens a conversation into one string, exactly as the model was trained. LM Studio applies the template stored in the GGUF file.</details>
<details><summary>What is the difference between a base and an instruct model?</summary>A base model only continues text. An instruct model was further trained (SFT, then preference tuning) on conversations to follow requests.</details>
<details><summary>Write the softmax formula.</summary>softmax(zᵢ) = e^zᵢ / Σⱼ e^zⱼ</details>
