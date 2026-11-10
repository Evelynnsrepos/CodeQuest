---
title: Tiny GPT 3: train it and let it write
minutes: 45
xp: 80
hint: train: torch.manual_seed(seed), gen = torch.Generator().manual_seed(seed), opt = torch.optim.AdamW(model.parameters(), lr=lr), model.train(), losses = []
hint: train loop: for step in range(steps): x, y = get_batch(data, block, batch, gen), logits, loss = model(x, y), then zero_grad, backward, step, losses.append(loss.item())
hint: generate: gen, model.eval(), then with torch.no_grad(): for step in range(n): crop, predict, sample, append
hint: Crop: context = idx[:, -model.block:]. Last position: last = logits[:, -1, :] / temperature. Sample: torch.multinomial(probs, 1, generator=gen)
---
# Watch the loss fall, then sample

⏱️ About 45 minutes

> **Warm-up:** what number should the very first loss be for a vocabulary of 35 characters?

Now the loop from lesson 08 meets the model from lesson 11 and the batches from lesson 10. It's the same loop that trains every LLM, only smaller.

**Training:** AdamW with `lr=3e-3`, and each step: get a batch, `logits, loss = model(x, y)`, `zero_grad`, `backward`, `step`. Record `loss.item()`. Training on the poem for a few hundred steps takes seconds on a CPU.

**Generating** (LLMs 1, lesson 07): start from some ids, and repeat `n` times:

1. Crop the context to the last `model.block` ids (positions beyond that don't exist).
2. Run the model, keep only the **last** position's logits: `logits[:, -1, :] / temperature`.
3. `softmax`, then sample one id with `torch.multinomial(probs, 1, generator=gen)`.
4. Append it: `torch.cat([idx, next_id], dim=1)`.

Wrap generation in `torch.no_grad()` and call `model.eval()` first (and `model.train()` before training): some layers behave differently in the two modes.

## 🔬 Temperature and sampling, step by step

Say the last position's logits for three characters are (2, 1, 0).

1. **Temperature 1:** divide by 1, nothing changes. Softmax (lesson 03) → (0.665, 0.245, 0.090).
2. **Temperature 0.5:** divide by 0.5 → (4, 2, 0). Softmax → (0.867, 0.117, 0.016). The favourite gets even more likely: safer, more boring text.
3. **Temperature 2:** divide by 2 → (1, 0.5, 0). Softmax → (0.506, 0.307, 0.186). Closer to even: wilder text.
4. `torch.multinomial(probs, 1)` then picks one id at random, with those chances.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `torch.Generator().manual_seed(seed)` | | a seeded random-number source just for the batches |
| `model.train()` / `model.eval()` | | switches between training mode and prediction mode |
| `logits, loss = model(x, y)` | | your `forward` from lesson 11 returns both |
| `losses.append(loss.item())` | | keeps every loss as a plain number, to see it fall |
| `idx[:, -model.block:]` | "all rows, the last block columns" | crops to the last 32 ids. `:` alone means "all"; a negative start counts from the end. |
| `logits[:, -1, :]` | | all rows, **only the last** position, all characters |
| `F.softmax(last, dim=-1)` | | the chances for the next character |
| `torch.cat([idx, next_id], dim=1)` | | appends the new id at the end of each row |

## 🎯 Your quest

1. `train(model, data, steps, block=32, batch=16, lr=3e-3, seed=0)`: seed a `torch.Generator` for the batches and `torch.manual_seed(seed)`, train, return the list of losses.
2. `generate(model, idx, n, seed=0, temperature=1.0)`: return the new `idx` tensor of shape `(1, start + n)`.

The check trains a fresh model for 400 steps: the average of the last 20 losses must be **below 1.0** (it starts near 3.6). Then it generates 200 characters, which should look like German poem lines.

**Part 1:** `train`. Replace `return []` with:

1. `torch.manual_seed(seed)`
2. `gen = torch.Generator().manual_seed(seed)`
3. `opt = torch.optim.AdamW(model.parameters(), lr=lr)`
4. `model.train()`
5. `losses = []`
6. `for step in range(steps):`
7. `    x, y = get_batch(data, block, batch, gen)`
8. `    logits, loss = model(x, y)`
9. `    opt.zero_grad()`
10. `    loss.backward()`
11. `    opt.step()`
12. `    losses.append(loss.item())`
13. `return losses`

**Part 2:** `generate`. Above its `return idx` line, type:

1. `gen = torch.Generator().manual_seed(seed)`
2. `model.eval()`
3. `with torch.no_grad():`
4. `    for step in range(n):`
5. `        context = idx[:, -model.block:]`
6. `        logits, loss = model(context)`
7. `        last = logits[:, -1, :] / temperature`
8. `        probs = F.softmax(last, dim=-1)`
9. `        next_id = torch.multinomial(probs, 1, generator=gen)`
10. `        idx = torch.cat([idx, next_id], dim=1)`

Keep the `return idx` at the end, with 4 spaces.

**Remember:** the generation loop is just: crop, predict, sample, append.

## Review

<details><summary>Why must a fresh model's loss be near ln(vocab)?</summary>Small random weights give nearly uniform probabilities, 1/vocab each, and −ln(1/vocab) = ln(vocab).</details>
