---
title: Checkpoint: analyse an experiment
xp: 120
---
# Embeddings and a model comparison, by hand

> **Warm-up:** before you start: which lessons of this course do you need to (1) find redundant features, (2) squash 3 features into 1, and (3) decide whether a new model really is better?

(Correlation; PCA; a t-test.)

## Your quest

`analyse(features, scores_a, scores_b)` returns a dict:

- `"redundant"`: the sorted list of feature-name **pairs** `(name1, name2)` (with name1 < name2 alphabetically) whose **absolute correlation** is above 0.95. `features` is a dict name → list of values.
- `"explained"`: the share of variance the first principal component keeps, for the features **standardized** first (each column minus its mean, divided by its sample std), so units don't decide. Use the covariance matrix and power iteration (lesson 04): λ₁ / trace.
- `"t"` and `"df"`: Welch's t-test of `scores_a` vs `scores_b`.
- `"better"`: `True` only if the t-test is significant **and** A's mean is higher.

You may copy your own functions from the earlier lessons; `T95` is given.

## Review

<details><summary>Name the four steps of PCA.</summary>Center (and maybe standardize), covariance matrix, eigenvectors, project.</details>
<details><summary>Why use the t-table instead of 1.96 for 5 runs?</summary>With few samples the standard deviation itself is uncertain, so the cut-off must be wider.</details>

## What's next

You can now read the math in most applied AI papers. For more: *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong; free online), 3Blue1Brown's *Essence of Linear Algebra* videos, and Gilbert Strang's MIT 18.06 lectures for SVD.
