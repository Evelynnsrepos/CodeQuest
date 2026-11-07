---
title: Measuring a classifier honestly
minutes: 40
xp: 50
hint: counts: three counters at 0, then for i in range(len(y_true)): t = y_true[i] and p = y_pred[i]
hint: counts: if t == 1 and p == 1: tp = tp + 1 (and the same for fp: t == 0 and p == 1, fn: t == 1 and p == 0)
hint: precision: tp, fp, fn = counts(y_true, y_pred), then if tp + fp == 0: return 0.0, then return tp / (tp + fp)
hint: f1: p = precision(...), r = recall(...), if p + r == 0: return 0.0, then return 2 * p * r / (p + r)
---
# When 99% accuracy is useless

⏱️ About 40 minutes

> **Warm-up:** 1 in 100 transactions is fraud. A model that always says "not fraud" is 99% accurate. Is it any good?

It catches nothing. With **imbalanced classes**, accuracy hides failure. Count the four outcomes (positive = the class you care about, here 1):

| | predicted 1 | predicted 0 |
|---|---|---|
| **actually 1** | true positive (TP) | false negative (FN) |
| **actually 0** | false positive (FP) | true negative (TN) |

- **Precision** = TP / (TP + FP): of the alarms, how many were real?
- **Recall** = TP / (TP + FN): of the real cases, how many did we catch?
- **F1** = 2·P·R / (P + R): their harmonic mean, high only if both are.

There's a trade-off: lowering the decision threshold (say from 0.5 to 0.2) catches more (recall ↑) but raises false alarms (precision ↓). The **ROC curve** and **AUC** summarize all thresholds.

Honest evaluation also needs:

- a **held-out test set** never used for choosing anything (you did this in the LLM capstone),
- **cross-validation** on small data: split into k folds, train k times, each fold is the test set once, average,
- watching for **leakage**: a feature that secretly contains the answer (like "refund issued" when predicting fraud).

## 🔬 Take the formulas apart

Take the truth `[1, 1, 0, 0, 1]` and the model's guesses `[1, 0, 0, 0, 1]`. Line them up:

| position | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| truth | 1 | 1 | 0 | 0 | 1 |
| guess | 1 | 0 | 0 | 0 | 1 |
| outcome | TP | FN | TN | TN | TP |

So TP = 2, FP = 0, FN = 1.

1. **Precision** = TP / (TP + FP) = 2 / (2 + 0) = **1.0**. Every alarm was real.
2. **Recall** = TP / (TP + FN) = 2 / (2 + 1) = **0.667**. It caught 2 of the 3 real cases.
3. **F1** = 2·P·R / (P + R). The `·` means "times".
   - top: 2 × 1.0 × 0.667 = 1.333
   - bottom: 1.0 + 0.667 = 1.667
   - 1.333 / 1.667 = **0.8**

Why not just the average (1.0 + 0.667) / 2 = 0.83? The F1 ("harmonic mean") drags the score towards the **worse** of the two. A model with precision 1.0 and recall 0.01 gets an average of 0.5 but an F1 of 0.02, which is the honest answer.

<div class="wrong"><b>Divide when nothing was predicted</b>: TP + FP = 0 means 0 / 0, and Python crashes with ZeroDivisionError.</div>
<div class="right">check the bottom first, return 0.0 when it's 0 ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `if t == 1 and p == 1:` | | both must be true |
| `tp = tp + 1` | | count one more |
| `return tp, fp, fn` | | gives back three numbers at once |
| `tp, fp, fn = counts(...)` | | catches the three numbers into three names, in the same order |
| `if tp + fp == 0:` | | checks the bottom of the fraction before dividing |

## 🎯 Your quest

`y_true` and `y_pred` are lists of 0 and 1. Return `0.0` when a denominator is 0. ("Denominator" is the bottom of a fraction.)

1. `precision(y_true, y_pred)`
2. `recall(y_true, y_pred)`
3. `f1(y_true, y_pred)`

**Part 1:** the helper `counts`. Replace `return 0, 0, 0` with:

1. `tp = 0`
2. `fp = 0`
3. `fn = 0`
4. `for i in range(len(y_true)):`
5. `    t = y_true[i]`
6. `    p = y_pred[i]`
7. `    if t == 1 and p == 1:`
8. `        tp = tp + 1`
9. `    if t == 0 and p == 1:`
10. `        fp = fp + 1`
11. `    if t == 1 and p == 0:`
12. `        fn = fn + 1`
13. `return tp, fp, fn`

**Part 2:** `precision`. Replace `return 0.0` with:

1. `tp, fp, fn = counts(y_true, y_pred)`
2. `if tp + fp == 0:`
3. `    return 0.0`
4. `return tp / (tp + fp)`

**Part 3:** `recall`: the same four lines, but with `fn` instead of `fp` in lines 2 and 4:

1. `tp, fp, fn = counts(y_true, y_pred)`
2. `if tp + fn == 0:`
3. `    return 0.0`
4. `return tp / (tp + fn)`

**Part 4:** `f1`. Replace `return 0.0` with:

1. `p = precision(y_true, y_pred)`
2. `r = recall(y_true, y_pred)`
3. `if p + r == 0:`
4. `    return 0.0`
5. `return 2 * p * r / (p + r)`

## Review

<details><summary>What are the two repeated steps of k-means?</summary>Assign each point to its nearest center, then move each center to the mean of its points.</details>
<details><summary>What does PCA find?</summary>The directions of largest variance in the data.</details>
