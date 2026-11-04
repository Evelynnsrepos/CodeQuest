---
title: Measuring a classifier honestly
xp: 50
---
# When 99% accuracy is useless

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

## Your quest

`y_true` and `y_pred` are lists of 0 and 1. Return `0.0` when a denominator is 0.

1. `precision(y_true, y_pred)`
2. `recall(y_true, y_pred)`
3. `f1(y_true, y_pred)`

## Review

<details><summary>What are the two repeated steps of k-means?</summary>Assign each point to its nearest center, then move each center to the mean of its points.</details>
<details><summary>What does PCA find?</summary>The directions of largest variance in the data.</details>
