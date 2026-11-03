---
title: Decision trees
xp: 50
---
# Twenty questions, learned from data

> **Warm-up:** how would you write rules by hand to guess whether someone buys a product from their age? How would you choose the cut-off age?

A **decision tree** asks yes/no questions ("age ≤ 31?") and follows branches to a prediction. Training chooses, at each node, the question that best **separates** the labels. A common measure of how mixed a group is, is **Gini impurity**:

```
gini(labels) = 1 − Σ_k p_k²        p_k = share of label k
```

A pure group (all "yes") has gini 0; a 50/50 group has 0.5. For a candidate split, compute the **weighted** gini of both sides:

```
score = (n_left / n)·gini(left) + (n_right / n)·gini(right)
```

and pick the split with the lowest score. Then repeat inside each side until groups are pure or small (the depth limit fights overfitting).

One tree overfits easily. Ensembles fix that:

- **Random forest**: many trees on random subsets of rows and features; average their votes.
- **Gradient boosting** (XGBoost, LightGBM, CatBoost): each new small tree fits the errors of the trees so far. The usual winner on tabular data.

Trees need no feature scaling and are easy to explain ("rejected because income ≤ 2000 and …"), which matters in finance and medicine.

## Your quest

1. `gini(labels)`.
2. `best_split(xs, labels)`: try every distinct value `t` of `xs` (in increasing order) as the rule `x ≤ t` goes left. Skip a split that leaves one side empty. Return `(t, score)` with the lowest score (first one on ties), score rounded to 4 decimals.

## Review

<details><summary>Gradient of the logistic loss with respect to w_j?</summary>(p − y) · x_j.</details>
<details><summary>Why can't plain linear regression predict a probability well?</summary>Its output isn't limited to 0..1.</details>
