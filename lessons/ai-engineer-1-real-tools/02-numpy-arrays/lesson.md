---
title: NumPy: math on whole arrays
minutes: 45
xp: 50
hint: standardize: means = X.mean(axis=0) and stds = X.std(axis=0), then return (X - means) / stds
hint: cosine_matrix: lengths = np.linalg.norm(A, axis=1, keepdims=True), B = A / lengths, return B @ B.T
hint: most_similar: sims = cosine_matrix(A)[i].copy(), then sims[i] = -np.inf so row i can't win, then return int(sims.argmax())
---
# No more loops

⏱️ About 45 minutes

> **Warm-up:** in Math 2 you wrote a dot product with a `for` loop. How long would that take for 1,000 vectors of 768 numbers each?

**NumPy** stores numbers in **arrays**: blocks of memory where every number has the same type. Operations run in fast compiled code over the **whole array at once** ("vectorized"), typically 50–100× faster than a Python loop. Every AI library (PyTorch, pandas, scikit-learn) is built on this idea.

```python
import numpy as np
a = np.array([1.0, 2.0, 3.0])
a * 2            # array([2., 4., 6.])   no loop
a @ a            # 14.0                  dot product
X = np.array([[1, 2], [3, 4], [5, 6]])   # 3 rows, 2 columns
X.shape          # (3, 2)
X.mean(axis=0)   # mean of each column: array([3., 4.])
X.mean(axis=1)   # mean of each row:    array([1.5, 3.5, 5.5])
```

**axis** is the direction you squash: `axis=0` goes **down** the rows (one result per column), `axis=1` goes **across** (one result per row).

**Broadcasting:** when shapes differ, NumPy stretches the smaller one. `X - X.mean(axis=0)` subtracts the column means (shape `(2,)`) from every row of `X` (shape `(3, 2)`).

## 🔬 The math, step by step

**Standardizing one column** (1, 2, 3):

1. The mean: (1 + 2 + 3) / 3 = **2**.
2. The standard deviation ("std", how spread out the numbers are): take each distance from the mean, square it, average, then the square root (√). Distances −1, 0, 1 → squares 1, 0, 1 → average 2/3 = 0.667 → √0.667 = **0.816**.
3. Each z-score = (value − mean) / std: (1 − 2) / 0.816 = **−1.22**, (2 − 2) / 0.816 = **0**, (3 − 2) / 0.816 = **1.22**.

Now every column has mean 0 and std 1, so "200 euros" and "3 rooms" are on the same scale. `X.mean(axis=0)` does step 1 for every column at once, `X.std(axis=0)` step 2, and broadcasting does step 3 for every number.

**Cosine between every pair of rows**, the trick in two steps:

1. Make every row length 1: divide it by its length. The length of (3, 4) is √(3² + 4²) = √25 = 5, so it becomes (0.6, 0.8).
2. For rows of length 1, the cosine is just the dot product. `B @ B.T` computes the dot product of every row with every row: entry [i][j] is the cosine of row i and row j.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `X.mean(axis=0)` | "mean down the rows" | one mean per column |
| `X.std(axis=0)` | | one standard deviation per column |
| `(X - means) / stds` | | broadcasting: every row minus the means, divided by the stds |
| `np.linalg.norm(A, axis=1, keepdims=True)` | "the norm of each row" | the length of each row. `keepdims=True` keeps it as a column (shape `(n, 1)`), so the division works row by row. |
| `B.T` | "B transposed" | rows become columns |
| `B @ B.T` | "B matrix-times B transposed" | all the dot products at once |
| `M[i]` | | row i of the matrix |
| `.copy()` | | a separate copy, so changing it doesn't change the original |
| `sims[i] = -np.inf` | "minus infinity" | a number smaller than everything, so position i can never be the biggest |
| `sims.argmax()` | "arg max" | the **position** of the biggest number (not the number itself) |
| `int(...)` | | turns NumPy's number type into a plain Python whole number |

## 🎯 Your quest

1. `standardize(X)`: subtract each column's mean and divide by each column's standard deviation (`X.std(axis=0)`). This is "z-scores per feature" (Math 4, lesson 08), done before training most models.
2. `cosine_matrix(A)`: for a matrix whose rows are vectors, return the matrix of cosine similarities between every pair of rows. Hint: divide each row by its length (`np.linalg.norm(A, axis=1, keepdims=True)`), then `B @ B.T`.
3. `most_similar(A, i)`: the index of the row most similar to row `i`, **not counting** `i` itself.

No Python loops allowed in 1 and 2 (the check times them on big arrays).

**Part 1:** `standardize`. Replace `return X` with:

1. `means = X.mean(axis=0)`
2. `stds = X.std(axis=0)`
3. `return (X - means) / stds`

**Part 2:** `cosine_matrix`. Replace `return A` with:

1. `lengths = np.linalg.norm(A, axis=1, keepdims=True)`
2. `B = A / lengths`
3. `return B @ B.T`

**Part 3:** `most_similar`. Replace `return 0` with:

1. `sims = cosine_matrix(A)[i].copy()`
2. `sims[i] = -np.inf`
3. `return int(sims.argmax())`

**Remember:** think in whole arrays; `axis=0` = per column.

## Review

<details><summary>What is a virtual environment for?</summary>A private set of packages for one project, so projects can't break each other.</details>
