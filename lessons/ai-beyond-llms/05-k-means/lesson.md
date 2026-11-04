---
title: Clustering with k-means
xp: 50
---
# Finding groups nobody labelled

> **Warm-up:** you have the listening habits of 10,000 users and no labels. How could a program discover "types" of listeners?

**k-means** finds `k` groups (clusters) in unlabelled data. Each cluster has a **center**. Repeat:

1. **Assign** every point to its nearest center.
2. **Update** every center to the mean of its points.

Each round can only lower the total squared distance from points to their centers, so it converges, though maybe to a local optimum; that's why libraries restart several times from different starts (k-means++ picks smart starting centers). You have to choose `k`; the "elbow" of the error-vs-k curve is a common heuristic.

Related unsupervised tools you'll meet:

- **PCA**: finds the directions of largest variance (eigenvectors of the covariance matrix) to compress or plot high-dimensional data.
- **t-SNE / UMAP**: 2D maps of embeddings, for example to look at how an LLM's embeddings group words.
- Clustering **embeddings** (LLMs 1, lesson 11) is how you group documents or support tickets by meaning today.

## Your quest

`dist2` (squared distance) is given. Write `kmeans(points, centers, iters)`:

- Run `iters` rounds of assign + update.
- Assign each point to the index of the nearest center (lowest index on ties).
- A center with no points keeps its position.
- Return `(centers, assignments)` after the last round, with centers as tuples and `assignments` from the last assign step.

## Review

<details><summary>Formula for Gini impurity?</summary>1 − Σ p_k².</details>
<details><summary>What does gradient boosting add with each new tree?</summary>A small tree that fits the errors of the trees so far.</details>
