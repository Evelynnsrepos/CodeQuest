---
title: Decision trees
minutes: 50
xp: 50
hint: gini: for k in set(labels): share = labels.count(k) / n and total = total + share ** 2. Then return 1 - total
hint: best_split: for t in sorted(set(xs)): build left and right with a loop: if xs[i] <= t: left.append(labels[i]) else right.append(labels[i])
hint: Skip empty sides: if len(left) == 0 or len(right) == 0: continue
hint: Keep the lowest: if best_score is None or score < best_score: best_t = t and best_score = score. Return (best_t, round(best_score, 4))
---
# Twenty questions, learned from data

⏱️ About 50 minutes

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

## 🔬 Take the formulas apart

**The signs:**

| Sign | Say it | Means |
|---|---|---|
| `p_k` | "p k" | the **share** of label k in the group: how many have it, divided by the group size |
| `p_k²` | "p k squared" | that share times itself |
| `Σ_k` | "sum over k" | add it up for every different label |
| `n_left / n` | | the part of all points that went left |

**Gini, in small steps** for the group `["y", "y", "n"]`:

1. n = 3. The labels are `y` (2 times) and `n` (1 time).
2. Shares: p_y = 2/3 = 0.667, p_n = 1/3 = 0.333.
3. Square each: 0.667² = 0.444, 0.333² = 0.111.
4. Σ adds them: 0.444 + 0.111 = 0.556.
5. gini = 1 − 0.556 = **0.444**. For `["y", "y", "y"]`: the share is 1, 1² = 1, and 1 − 1 = **0**: pure.

**A split score, in small steps** for x = (10, 20, 30) with labels (a, a, b):

| rule | left | right | score |
|---|---|---|---|
| x ≤ 10 | a | a, b | 1/3 · 0 + 2/3 · 0.5 = **0.3333** |
| x ≤ 20 | a, a | b | 2/3 · 0 + 1/3 · 0 = **0** |
| x ≤ 30 | a, a, b | (empty) | skipped |

The lowest score wins: **(20, 0.0)**. Each side's gini is weighted by how big that side is, so a tiny pure side can't win alone.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `set(labels)` | "set of labels" | each different value once: `set(["y", "y", "n"])` is `{"y", "n"}` |
| `labels.count("y")` | "labels count y" | how many times `"y"` is in the list: 2 |
| `sorted(set(xs))` | | the different values, smallest first |
| `if xs[i] <= t:` ... `else:` | | sends label i to the left or the right list |
| `continue` | | skips this `t` and tries the next one |
| `best_score is None or score < best_score` | | the best-so-far pattern, looking for the **lowest**. `<` keeps the first on a tie. |
| `round(x, 4)` | "round x to 4 places" | `0.33333` → `0.3333` |

## 🎯 Your quest

1. `gini(labels)`.
2. `best_split(xs, labels)`: try every distinct value `t` of `xs` (in increasing order) as the rule `x ≤ t` goes left. Skip a split that leaves one side empty. Return `(t, score)` with the lowest score (first one on ties), score rounded to 4 decimals.

**Part 1:** `gini`. Replace `return 0.0` with:

1. `n = len(labels)`
2. `total = 0`
3. `for k in set(labels):`
4. `    share = labels.count(k) / n`
5. `    total = total + share ** 2`
6. `return 1 - total`

**Part 2:** `best_split`. Replace `return (None, 1.0)` with:

1. `n = len(xs)`
2. `best_t = None`
3. `best_score = None`
4. `for t in sorted(set(xs)):`
5. `    left = []`
6. `    right = []`
7. `    for i in range(n):`
8. `        if xs[i] <= t:`
9. `            left.append(labels[i])`
10. `        else:`
11. `            right.append(labels[i])`
12. `    if len(left) == 0 or len(right) == 0:`
13. `        continue`
14. `    score = len(left) / n * gini(left) + len(right) / n * gini(right)`
15. `    if best_score is None or score < best_score:`
16. `        best_t = t`
17. `        best_score = score`
18. `return (best_t, round(best_score, 4))`

## Review

<details><summary>Gradient of the logistic loss with respect to w_j?</summary>(p − y) · x_j.</details>
<details><summary>Why can't plain linear regression predict a probability well?</summary>Its output isn't limited to 0..1.</details>
