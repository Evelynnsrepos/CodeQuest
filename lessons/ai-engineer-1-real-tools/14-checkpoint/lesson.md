---
title: Checkpoint: from a CSV to a trained model
xp: 120
---
# The whole toolbox, once

> **Warm-up:** list the libraries from this course and the one job each is best at.

(NumPy: fast math on arrays. pandas: loading and shaping tables. scikit-learn: classic models, splits, metrics. PyTorch: neural networks and gradients.)

A real AI engineering task, start to finish: a café gives you a German CSV of daily sales (`make_csv()` in the starter builds it). Predict `Umsatz` from the day, the temperature and rain.

## Your quest

`run(text)` returns a dict:

1. **Load** with pandas (`sep=";"`, `decimal=","`). Turn `Tag` into one-hot columns with `pd.get_dummies(df, columns=["Tag"], dtype=float)`: a model can't multiply "Sa", but it can use a column that is 1.0 on Saturdays.
2. **Split** features `X` (everything except `Umsatz`) and target `y`, then `train_test_split(..., test_size=0.25, random_state=0)`.
3. **Baseline:** scikit-learn `LinearRegression`, scored with `r2_score` on the test part. **R²** says how much of the ups and downs the model explains: 1 = perfect, 0 = no better than always guessing the average.
4. **PyTorch:** standardize `X` with the **training** mean and std (lesson 02, and lesson 13's leak warning), standardize `y` the same way, train an MLP (`n_features → 32 → 1`, ReLU) with AdamW (`lr=0.01`) for 500 full-batch steps with seed 0, predict the test part, undo the `y` scaling, and compute R².
5. Return `{"rows": number of rows, "features": number of feature columns, "baseline_r2": ..., "torch_r2": ...}`.

Both R² values should be above **0.9**. On data this simple, the linear baseline is as good as the network, which is the lesson: **always try the simple model first.**

## Review

<details><summary>What are the four steps of the generation loop?</summary>Crop the context, predict the last position, sample, append.</details>
<details><summary>Why standardize with the training set's mean only?</summary>Using test data to compute it leaks information and makes the test score too optimistic.</details>

## What's next

**AI engineer 2** builds real retrieval (RAG) and evaluations with these tools, and **AI engineer 3** ships them as a tested web service.
