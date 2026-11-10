---
title: makemore 2: the same model, trained by gradient descent
minutes: 60
xp: 55
hint: First: probs = [], for row in W: probs.append(softmax(row))
hint: Then for a, b in pairs: loss = loss - math.log(probs[a][b]), and for j in range(27): grad[a][j] = grad[a][j] + probs[a][j]
hint: Still in 'for a, b': grad[a][b] = grad[a][b] - 1 (8 spaces)
hint: After the loop: n = len(pairs), divide every grad[i][j] by n with two loops, then return loss / n, grad
---
# From counting to learning

⏱️ About 60 minutes

> **Warm-up:** counting worked for one letter of context. Why won't it work for 10 letters of context, let alone 8,000 tokens?

The table would need 27¹⁰ rows: more than there are atoms in a… well, far too many, and almost all would be empty. Counting doesn't **generalize** to contexts it hasn't seen. Neural networks do, because they learn *weights* that are shared across contexts.

So let's rebuild the bigram model as a neural network, trained with gradient descent, and check that it learns the same thing:

- **Parameters:** a 27 × 27 table `W` of **logits**, all starting at 0 (so every next character starts equally likely).
- **Forward:** for a previous character `a`, the logits are row `W[a]`; `softmax` turns them into probabilities. (In matrix language: a one-hot vector times `W`, exactly what an embedding lookup is.)
- **Loss:** average negative log-likelihood of the true next characters, i.e. **cross-entropy**.
- **Gradient:** from LLMs 4, lesson 8: for each pair `(a, b)`, row `a` gets `softmax(W[a]) − onehot(b)`. Average over all pairs.
- **Update:** `W -= lr · grad`.

After training, the loss gets close to **2.21**, the best any bigram table can do on this data. (The counting model scored 2.41 because smoothing deliberately gives a little probability to pairs never seen; the neural version gets a similar effect from regularization, which we skip here.) Both are the same kind of model: a table of next-character probabilities. The difference is that the neural version can be scaled up: replace the table lookup with an MLP over several previous characters (makemore part 3), then with a transformer (lesson 12), and the training loop **stays exactly the same**.

## 🔬 Take the formula apart

For one pair (a, b), "after a comes b":

<div class="formula">grad of row a = <span class="k1">softmax(W[a])</span> − <span class="k2">onehot(b)</span></div>

- <span class="k1">softmax(W[a])</span>: the model's probabilities for what follows `a` (LLMs 1).
- <span class="k2">onehot(b)</span>: a list of 27 zeros with a single **1** at position b, "the right answer".
- Subtract: every entry gets its probability, and entry b gets probability − 1. That's the LLM gradient from LLMs 4, lesson 8.
- Only row a gets anything. Rows of letters that didn't come first stay at 0 for this pair.

Numbers with only 3 characters: W[a] = [0, 0, 0], so softmax = [⅓, ⅓, ⅓]. True next is position 2. Gradient = [⅓, ⅓, ⅓ − 1] = **[0.33, 0.33, −0.67]**. The update W − lr·grad **raises** logit 2 and lowers the others. Next time, position 2 is a little more likely.

**Average over all pairs:** add up every pair's gradient and loss, then divide each by n (the number of pairs).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `probs.append(softmax(row))` | | one probability row per letter, computed once (it's slow) |
| `for a, b in pairs:` | | each pair `(3, 7)` taken apart into `a` and `b` |
| `loss = loss - math.log(probs[a][b])` | | add this pair's surprise |
| `grad[a][j] = grad[a][j] + probs[a][j]` | | the softmax part, for every j |
| `grad[a][b] = grad[a][b] - 1` | | the "− onehot" part: only at the right answer |
| two loops over `i` and `j` | | visits every cell of the 27 × 27 table |

### 👀 Worked example: two pairs, three letters

pairs = `[(0, 2), (0, 1)]`, all logits 0, so every probability row is [⅓, ⅓, ⅓].

1. Pair (0, 2): row 0 gets [⅓, ⅓, ⅓], then entry 2 gets −1 → [⅓, ⅓, −⅔].
2. Pair (0, 1): add [⅓, ⅓, ⅓] again → [⅔, ⅔, −⅓], then entry 1 gets −1 → [⅔, −⅓, −⅓].
3. Divide by n = 2: row 0 = **[⅓, −⅙, −⅙]**. Letter 0 (never the answer) gets pushed down; 1 and 2 get pushed up equally.

## 🎯 Your quest

Write `loss_and_grad(W, pairs)`. Between `loss = 0.0` and `return loss, grad`, add:

1. `    probs = []`
2. `    for row in W:`
3. `        probs.append(softmax(row))`
4. `    for a, b in pairs:`
5. `        loss = loss - math.log(probs[a][b])`
6. `        for j in range(27):`
7. `            grad[a][j] = grad[a][j] + probs[a][j]`
8. `        grad[a][b] = grad[a][b] - 1`
9. `    n = len(pairs)`
10. `    for i in range(27):`
11. `        for j in range(27):`
12. `            grad[i][j] = grad[i][j] / n`

Then change the last line to `    return loss / n, grad`.

The training loop is given. Watch the loss fall from log 27 ≈ 3.30 towards 2.21.

## Review

<details><summary>Why does a bigram model use add-one smoothing?</summary>So pairs never seen in training don't get probability 0, which would make log-probabilities −∞.</details>
<details><summary>What NLL does uniform guessing among 27 characters give?</summary>log 27 ≈ 3.30.</details>
<details><summary>What is the gradient of cross-entropy with respect to the logits?</summary>softmax(logits) − onehot(true token).</details>
