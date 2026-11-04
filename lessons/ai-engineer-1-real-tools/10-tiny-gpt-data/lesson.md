---
title: Tiny GPT 1: data and batches
xp: 55
---
# From text to training examples

> **Warm-up:** in LLMs 5 you trained a bigram model. What was one training example?

The next three lessons build and train a real (tiny) GPT in PyTorch, the same design as nanoGPT and as LLMs 8, small enough to train on a laptop CPU in under a minute.

Step 1 is the data:

1. **Tokenize** by character (the simplest tokenizer): every distinct character gets an id. `stoi` maps character → id, `itos` id → character.
2. **Encode** the whole text into one long tensor of ids.
3. **Batches:** pick random start positions; each example is `block` ids `x`, and the target `y` is the **same window shifted one to the right**. So for every position the model learns "given everything so far, predict the next character", `block` predictions per example.

```
text:  E i n _ M e n s c h
x:     E i n _ M e n s
y:       i n _ M e n s c
```

## Your quest

1. `build_vocab(text)`: `(stoi, itos)` with the **sorted** distinct characters.
2. `encode(s, stoi)` → list of ids; `decode(ids, itos)` → string.
3. `get_batch(data, block, batch, gen)`: `data` is a 1-D `long` tensor. Draw `batch` start indexes with `torch.randint(len(data) - block, (batch,), generator=gen)`, and return `(x, y)`, both of shape `(batch, block)`, `y` shifted by one.

**Remember:** the target is the input shifted by one.

## Review

<details><summary>Why do the ReLUs matter in an MLP?</summary>Without a nonlinearity, stacked linear layers collapse into one linear map and can't bend.</details>
