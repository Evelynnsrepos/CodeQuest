---
title: Clustering with k-means
minutes: 60
xp: 50
hint: Outer loop: for step in range(iters):. Inside it, first the assign step: assign = [], then for each point find the nearest center
hint: Nearest: best = 0, then for i in range(len(centers)): if dist2(p, centers[i]) < dist2(p, centers[best]): best = i. Then assign.append(best)
hint: Update: for each center i, collect mine = the points with assign[j] == i. No points → new.append(tuple(centers[i]))
hint: Otherwise build the mean one coordinate at a time: for dim in range(len(mine[0])): add up p[dim] over mine, then mean.append(total / len(mine))
hint: After the update loop (still inside the step loop): centers = new. At the very end: return centers, assign
---
# Finding groups nobody labelled

⏱️ About 60 minutes

> **Warm-up:** you have the listening habits of 10,000 users and no labels. How could a program discover "types" of listeners?

**k-means** finds `k` groups (clusters) in unlabelled data. Each cluster has a **center**. Repeat:

1. **Assign** every point to its nearest center.
2. **Update** every center to the mean of its points.

Each round can only lower the total squared distance from points to their centers, so it converges, though maybe to a local optimum; that's why libraries restart several times from different starts (k-means++ picks smart starting centers). You have to choose `k`; the "elbow" of the error-vs-k curve is a common heuristic.

Related unsupervised tools you'll meet:

- **PCA**: finds the directions of largest variance (eigenvectors of the covariance matrix) to compress or plot high-dimensional data.
- **t-SNE / UMAP**: 2D maps of embeddings, for example to look at how an LLM's embeddings group words.
- Clustering **embeddings** (LLMs 1, lesson 11) is how you group documents or support tickets by meaning today.

## 🔬 Take the distance apart

`dist2(p, q)` is **given**. It measures how far apart two points are, squared:

<div class="formula">dist2 = ( <span class="k1">p₁ − q₁</span> )² + ( <span class="k2">p₂ − q₂</span> )²</div>

For p = (1, 2) and q = (4, 6):

1. <span class="k1">p₁ − q₁</span> = 1 − 4 = −3, squared: **9**.
2. <span class="k2">p₂ − q₂</span> = 2 − 6 = −4, squared: **16**.
3. 9 + 16 = **25**. (The real distance is √25 = 5, the long side of a 3-4-5 triangle. Skipping the square root doesn't change which center is nearest, so k-means doesn't bother.)

**The mean of some points** is the mean of each coordinate on its own: the mean of (0, 0) and (2, 4) is ((0 + 2) / 2, (0 + 4) / 2) = **(1, 2)**.

### 👀 Worked example: one round by hand

Points (0, 0), (2, 0), (10, 0). Centers (1, 0) and (9, 0).

**Assign:**

| point | dist2 to center 0 | dist2 to center 1 | nearest |
|---|---|---|---|
| (0, 0) | 1 | 81 | 0 |
| (2, 0) | 1 | 49 | 0 |
| (10, 0) | 81 | 1 | 1 |

So `assign` = `[0, 0, 1]`.

**Update:**

1. Center 0's points: (0, 0) and (2, 0). Mean: ((0 + 2) / 2, (0 + 0) / 2) = **(1.0, 0.0)**.
2. Center 1's points: just (10, 0). Mean: **(10.0, 0.0)**.

The next round starts with these new centers.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for step in range(iters):` | "iters times" | repeats assign + update |
| `best = 0` then `if ... < dist2(p, centers[best]):` | | best-so-far, looking for the smallest distance. `<` keeps the lower index on a tie. |
| `assign[j] == i` | | "point j belongs to center i" |
| `mine[0]` | | the first point of the group; `len(mine[0])` is how many coordinates it has (2 here) |
| `for dim in range(len(mine[0])):` | "for each coordinate" | `dim` = 0 (the x) then 1 (the y) |
| `p[dim]` | | that coordinate of point p |
| `tuple(mean)` | "tuple of mean" | turns the list `[1.0, 0.0]` into the tuple `(1.0, 0.0)`, the form the check wants |
| `centers = new` | | the new centers replace the old ones for the next round |

## 🎯 Your quest

`dist2` (squared distance) is given. Write `kmeans(points, centers, iters)`:

- Run `iters` rounds of assign + update.
- Assign each point to the index of the nearest center (lowest index on ties).
- A center with no points keeps its position.
- Return `(centers, assignments)` after the last round, with centers as tuples and `assignments` from the last assign step.

Replace `return centers, [0] * len(points)` with these lines. Watch the spaces: the update part (line 10 on) is still inside the `for step` loop.

1. `assign = []`
2. `for step in range(iters):`
3. `    assign = []`
4. `    for p in points:`
5. `        best = 0`
6. `        for i in range(len(centers)):`
7. `            if dist2(p, centers[i]) < dist2(p, centers[best]):`
8. `                best = i`
9. `        assign.append(best)`
10. `    new = []`
11. `    for i in range(len(centers)):`
12. `        mine = []`
13. `        for j in range(len(points)):`
14. `            if assign[j] == i:`
15. `                mine.append(points[j])`
16. `        if len(mine) == 0:`
17. `            new.append(tuple(centers[i]))`
18. `        else:`
19. `            mean = []`
20. `            for dim in range(len(mine[0])):`
21. `                total = 0`
22. `                for p in mine:`
23. `                    total = total + p[dim]`
24. `                mean.append(total / len(mine))`
25. `            new.append(tuple(mean))`
26. `    centers = new`
27. `return centers, assign`

Lines 3 to 9 are the assign table above, lines 10 to 25 the update.

## Review

<details><summary>Formula for Gini impurity?</summary>1 − Σ p_k².</details>
<details><summary>What does gradient boosting add with each new tree?</summary>A small tree that fits the errors of the trees so far.</details>
