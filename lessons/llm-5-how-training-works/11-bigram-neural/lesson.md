---
title: makemore 2: the same model, trained by gradient descent
xp: 55
---
# From counting to learning

> **Warm-up:** counting worked for one letter of context. Why won't it work for 10 letters of context, let alone 8,000 tokens?

The table would need 27¹⁰ rows: more than there are atoms in a… well, far too many, and almost all would be empty. Counting doesn't **generalize** to contexts it hasn't seen. Neural networks do, because they learn *weights* that are shared across contexts.

So let's rebuild the bigram model as a neural network, trained with gradient descent, and check that it learns the same thing:

- **Parameters:** a 27 × 27 table `W` of **logits**, all starting at 0 (so every next character starts equally likely).
- **Forward:** for a previous character `a`, the logits are row `W[a]`; `softmax` turns them into probabilities. (In matrix language: a one-hot vector times `W`, exactly what an embedding lookup is.)
- **Loss:** average negative log-likelihood of the true next characters, i.e. **cross-entropy**.
- **Gradient:** from LLMs 4, lesson 8: for each pair `(a, b)`, row `a` gets `softmax(W[a]) − onehot(b)`. Average over all pairs.
- **Update:** `W -= lr · grad`.

After training, the loss gets close to **2.21**, the best any bigram table can do on this data. (The counting model scored 2.41 because smoothing deliberately gives a little probability to pairs never seen; the neural version gets a similar effect from regularization, which we skip here.) Both are the same kind of model: a table of next-character probabilities. The difference is that the neural version can be scaled up: replace the table lookup with an MLP over several previous characters (makemore part 3), then with a transformer (lesson 12), and the training loop **stays exactly the same**.

## Your quest

Write `loss_and_grad(W, pairs)`. It returns `(loss, grad)`:

1. Compute `probs = [softmax(row) for row in W]` once.
2. Start `grad` as a 27 × 27 table of zeros and `loss` at 0.
3. For every pair `(a, b)`: add `−log probs[a][b]` to the loss; add `probs[a][j]` to `grad[a][j]` for every `j`; subtract 1 from `grad[a][b]`.
4. Divide the loss and every gradient entry by the number of pairs.

The training loop is given. Watch the loss fall from log 27 ≈ 3.30 towards 2.21.

## Review

<details><summary>Why does a bigram model use add-one smoothing?</summary>So pairs never seen in training don't get probability 0, which would make log-probabilities −∞.</details>
<details><summary>What NLL does uniform guessing among 27 characters give?</summary>log 27 ≈ 3.30.</details>
<details><summary>What is the gradient of cross-entropy with respect to the logits?</summary>softmax(logits) − onehot(true token).</details>
