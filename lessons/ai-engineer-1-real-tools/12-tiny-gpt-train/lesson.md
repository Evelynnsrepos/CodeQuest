---
title: Tiny GPT 3: train it and let it write
xp: 80
---
# Watch the loss fall, then sample

> **Warm-up:** what number should the very first loss be for a vocabulary of 35 characters?

Now the loop from lesson 08 meets the model from lesson 11 and the batches from lesson 10. It's the same loop that trains every LLM, only smaller.

**Training:** AdamW with `lr=3e-3`, and each step: get a batch, `logits, loss = model(x, y)`, `zero_grad`, `backward`, `step`. Record `loss.item()`. Training on the poem for a few hundred steps takes seconds on a CPU.

**Generating** (LLMs 1, lesson 07): start from some ids, and repeat `n` times:

1. Crop the context to the last `model.block` ids (positions beyond that don't exist).
2. Run the model, keep only the **last** position's logits: `logits[:, -1, :] / temperature`.
3. `softmax`, then sample one id with `torch.multinomial(probs, 1, generator=gen)`.
4. Append it: `torch.cat([idx, next_id], dim=1)`.

Wrap generation in `torch.no_grad()` and call `model.eval()` first (and `model.train()` before training): some layers behave differently in the two modes.

## Your quest

1. `train(model, data, steps, block=32, batch=16, lr=3e-3, seed=0)`: seed a `torch.Generator` for the batches and `torch.manual_seed(seed)`, train, return the list of losses.
2. `generate(model, idx, n, seed=0, temperature=1.0)`: return the new `idx` tensor of shape `(1, start + n)`.

The check trains a fresh model for 400 steps: the average of the last 20 losses must be **below 1.0** (it starts near 3.6). Then it generates 200 characters, which should look like German poem lines.

**Remember:** the generation loop is just: crop, predict, sample, append.

## Review

<details><summary>Why must a fresh model's loss be near ln(vocab)?</summary>Small random weights give nearly uniform probabilities, 1/vocab each, and −ln(1/vocab) = ln(vocab).</details>
