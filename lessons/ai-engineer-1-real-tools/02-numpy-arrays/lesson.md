---
title: NumPy: math on whole arrays
xp: 50
---
# No more loops

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

## Your quest

1. `standardize(X)`: subtract each column's mean and divide by each column's standard deviation (`X.std(axis=0)`). This is "z-scores per feature" (Math 4, lesson 08), done before training most models.
2. `cosine_matrix(A)`: for a matrix whose rows are vectors, return the matrix of cosine similarities between every pair of rows. Hint: divide each row by its length (`np.linalg.norm(A, axis=1, keepdims=True)`), then `B @ B.T`.
3. `most_similar(A, i)`: the index of the row most similar to row `i`, **not counting** `i` itself.

No Python loops allowed in 1 and 2 (the check times them on big arrays).

**Remember:** think in whole arrays; `axis=0` = per column.

## Review

<details><summary>What is a virtual environment for?</summary>A private set of packages for one project, so projects can't break each other.</details>
