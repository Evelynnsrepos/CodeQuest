---
title: Logistic regression
xp: 50
---
# Predicting a yes/no probability

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

## Your quest

`sigmoid` is given. `x` and `w` are lists (features).

1. `predict(w, b, x)`: `σ(w·x + b)`.
2. `train_logistic(X, y, lr, epochs)`: start with `w` all zeros and `b = 0`. For each epoch, for each example **in order**, compute `p` and update `w_j -= lr·(p − y)·x_j` and `b -= lr·(p − y)`. Return `(w, b)`.
3. `accuracy(w, b, X, y)`: the fraction of examples where `(p ≥ 0.5)` matches the label.

## Review

<details><summary>Formula for the slope of the least-squares line?</summary>Covariance of x and y divided by the variance of x.</details>
<details><summary>Minimizing MSE is maximum likelihood under which noise assumption?</summary>Gaussian noise.</details>
