---
title: Logistic regression
minutes: 55
xp: 50
hint: predict: z = 0, then for j in range(len(w)): z = z + w[j] * x[j]. Then return sigmoid(z + b)
hint: train_logistic: w = [0.0] * len(X[0]) and b = 0.0, then for epoch in range(epochs): and inside it for i in range(len(X)):
hint: Inside: x = X[i], err = predict(w, b, x) - y[i], then for j in range(len(w)): w[j] = w[j] - lr * err * x[j]. Then b = b - lr * err
hint: accuracy: guess = 1 if predict(...) >= 0.5 (with if/else), then if guess == y[i]: correct = correct + 1. Return correct / len(X)
---
# Predicting a yes/no probability

⏱️ About 55 minutes

> **Warm-up:** a straight line can predict 1.4 or −0.3. Why is that a problem when the answer is "pass or fail"?

Probabilities must stay between 0 and 1. **Logistic regression** squashes the line through the **sigmoid**:

```
P(y = 1 | x) = σ(w·x + b)        σ(z) = 1 / (1 + e^(−z))
```

It's trained with the **binary cross-entropy** loss `−[y·ln p + (1−y)·ln(1−p)]`, and its gradient is beautifully simple (the same "prediction minus target" you derived for softmax + cross-entropy in LLMs 4):

```
∂loss/∂w_j = (p − y) · x_j        ∂loss/∂b = (p − y)
```

To classify, predict 1 when `p ≥ 0.5`. Logistic regression is a single neuron with a sigmoid, and softmax regression (many classes) is exactly an LLM's output layer without the transformer underneath.

## 🔬 Take the formulas apart

**The signs:**

| Sign | Say it | Means |
|---|---|---|
| `w·x` | "w dot x" | multiply the weights and the features pair by pair, then add: w = (2, −1), x = (1, 3) → 2·1 + (−1)·3 = −1 |
| `σ(z)` | "sigma of z" | the **sigmoid**: squashes any number into 0..1 |
| `e` | "e" | a fixed number, about 2.718 |
| `e^(−z)` | "e to the minus z" | e multiplied by itself −z times. In Python: `math.exp(-z)` |
| `P(y = 1 \| x)` | "the probability that y is 1, given x" | the model's chance for "yes" for this input |
| `ln` | "natural log" | the opposite of `e^`: ln(e²) = 2. ln of a small number is a big negative number. |
| `∂loss/∂w_j` | "the partial derivative of the loss with respect to w j" | how much the loss changes when you nudge only w_j (LLMs 4, lesson 07) |
| `lr` | "learning rate" | how big each nudge is |

**The sigmoid, in small steps** for z = 2:

1. −z = −2.
2. e^(−2) = 1 / (2.718 · 2.718) = 1 / 7.39 = **0.135**.
3. 1 + 0.135 = 1.135.
4. 1 / 1.135 = **0.881**. A big positive z gives nearly 1, z = 0 gives exactly 0.5 (because e⁰ = 1, and 1 / (1 + 1) = 0.5), a big negative z gives nearly 0.

**The loss −[y·ln p + (1−y)·ln(1−p)]**: when the answer is y = 1, the second part is 0 · ... = 0, so the loss is −ln p. If the model said p = 0.9: −ln 0.9 = 0.105 (small, good). If it said p = 0.1: −ln 0.1 = 2.3 (big, bad). You don't compute this one in the code; you use its gradient.

**One training step, in small steps**: w = [0], b = 0, the example x = [2] with label y = 1, lr = 0.5.

1. z = 0·2 + 0 = 0, so p = σ(0) = **0.5**.
2. err = p − y = 0.5 − 1 = **−0.5**. (The model guessed too low.)
3. The gradient for w₀ is err · x₀ = −0.5 · 2 = −1. New w₀ = 0 − 0.5 · (−1) = **0.5**. (Minus a minus: w goes **up**.)
4. The gradient for b is err = −0.5. New b = 0 − 0.5 · (−0.5) = **0.25**.
5. Check: now z = 0.5·2 + 0.25 = 1.25 and p = σ(1.25) = **0.78**. Closer to 1, as it should be.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `z = z + w[j] * x[j]` | | the dot product as a running total |
| `[0.0] * len(X[0])` | | one 0.0 for each feature: `[0.0] * 2` is `[0.0, 0.0]` |
| `for epoch in range(epochs):` | | repeat the whole training pass `epochs` times |
| `x = X[i]` | | example number i (a list of features); `y[i]` is its label |
| `w[j] = w[j] - lr * err * x[j]` | | changes one weight inside the list |
| `if p >= 0.5:` | "if p is at least 0.5" | `>=` means "greater than or equal" |

## 🎯 Your quest

`sigmoid` is given. `x` and `w` are lists (features).

1. `predict(w, b, x)`: `σ(w·x + b)`.
2. `train_logistic(X, y, lr, epochs)`: start with `w` all zeros and `b = 0`. For each epoch, for each example **in order**, compute `p` and update `w_j -= lr·(p − y)·x_j` and `b -= lr·(p − y)`. Return `(w, b)`.
3. `accuracy(w, b, X, y)`: the fraction of examples where `(p ≥ 0.5)` matches the label.

**Part 1:** `predict`. Replace `return 0.5` with:

1. `z = 0`
2. `for j in range(len(w)):`
3. `    z = z + w[j] * x[j]`
4. `return sigmoid(z + b)`

**Part 2:** `train_logistic`. Replace its `return` line with the training step from above, inside two loops:

1. `w = [0.0] * len(X[0])`
2. `b = 0.0`
3. `for epoch in range(epochs):`
4. `    for i in range(len(X)):`
5. `        x = X[i]`
6. `        err = predict(w, b, x) - y[i]`
7. `        for j in range(len(w)):`
8. `            w[j] = w[j] - lr * err * x[j]`
9. `        b = b - lr * err`
10. `return w, b`

**Part 3:** `accuracy`. Replace `return 0.0` with:

1. `correct = 0`
2. `for i in range(len(X)):`
3. `    if predict(w, b, X[i]) >= 0.5:`
4. `        guess = 1`
5. `    else:`
6. `        guess = 0`
7. `    if guess == y[i]:`
8. `        correct = correct + 1`
9. `return correct / len(X)`

## Review

<details><summary>Formula for the slope of the least-squares line?</summary>Covariance of x and y divided by the variance of x.</details>
<details><summary>Minimizing MSE is maximum likelihood under which noise assumption?</summary>Gaussian noise.</details>
