---
title: Convolutions: how computers learned to see
minutes: 50
xp: 50
hint: conv2d: k_h = len(kernel), k_w = len(kernel[0]), out_h = len(image) - k_h + 1, out_w = len(image[0]) - k_w + 1
hint: conv2d: for i in range(out_h): row = [], for j in range(out_w): total = 0, then two loops for a and b adding image[i + a][j + b] * kernel[a][b]
hint: Don't forget row.append(total) inside the j loop and out.append(row) inside the i loop
hint: max_pool: for i in range(0, len(image), size): and for j in range(0, len(image[0]), size): start biggest = image[i][j] and keep anything bigger
---
# One small filter, slid everywhere

⏱️ About 50 minutes

> **Warm-up:** a cat in the top-left of a photo and a cat in the bottom-right are both cats. Should a network have to learn "cat" separately for every position?

No. A **convolutional neural network (CNN)** slides the same small grid of weights (a **kernel** or filter, like 3×3) over the whole image. At each position it multiplies the overlapping pixels by the kernel and sums:

```
out[i][j] = Σ_a Σ_b image[i+a][j+b] · kernel[a][b]
```

Without padding, an `H×W` image and a `k×k` kernel give an `(H−k+1)×(W−k+1)` **feature map**. (Deep-learning libraries compute exactly this "cross-correlation" and call it convolution.)

- **Weight sharing:** a 3×3 kernel has 9 weights whatever the image size.
- **Layers of features:** early kernels learn edges and colours, later layers combine them into textures, eyes, wheels, cats.
- **Pooling:** **max pooling** keeps the largest value in each 2×2 block, halving the size and adding a little tolerance to shifts.

**AlexNet** (2012) won ImageNet by a huge margin with a CNN on two GPUs, starting the deep-learning boom. **ResNet** (2015) added residual connections to train 152 layers, which transformers later borrowed. CNNs are still used everywhere on phones and in real-time vision, and the U-Net CNN is the core of many diffusion models.

## 🔬 Take the formula apart

<div class="formula">out[<span class="k1">i</span>][<span class="k2">j</span>] = Σ<sub>a</sub> Σ<sub>b</sub> image[<span class="k1">i</span>+<span class="k3">a</span>][<span class="k2">j</span>+<span class="k4">b</span>] · kernel[<span class="k3">a</span>][<span class="k4">b</span>]</div>

| Piece | Means |
|---|---|
| <span class="k1">i</span>, <span class="k2">j</span> | the row and column where the kernel's top-left corner sits |
| <span class="k3">a</span>, <span class="k4">b</span> | the row and column **inside** the kernel |
| Σ<sub>a</sub> Σ<sub>b</sub> | "add up for every a and every b": every cell of the kernel |
| `·` | times |

**By hand**: image `[[1, 0, 2], [3, 1, 0], [0, 2, 1]]`, kernel `[[1, 1], [0, 0]]` (it adds the top two cells it covers).

1. Output size: (3 − 2 + 1) × (3 − 2 + 1) = 2 × 2.
2. out[0][0]: the kernel covers rows 0–1, columns 0–1: 1·1 + 0·1 + 3·0 + 1·0 = **1**.
3. out[0][1]: columns 1–2: 0·1 + 2·1 + 1·0 + 0·0 = **2**.
4. out[1][0]: rows 1–2, columns 0–1: 3·1 + 1·1 + 0·0 + 2·0 = **4**.
5. out[1][1]: rows 1–2, columns 1–2: 1·1 + 0·1 + 2·0 + 1·0 = **1**.
6. Result: `[[1, 2], [4, 1]]`.

**Max pooling** with size 2 on `[[1, 5, 0, 2], [3, 2, 4, 1]]`: the left 2×2 block holds 1, 5, 3, 2 → **5**; the right one holds 0, 2, 4, 1 → **4**. Result: `[[5, 4]]`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len(kernel)`, `len(kernel[0])` | | the number of rows, and the length of the first row (the columns) |
| `image[i + a][j + b]` | | row `i + a`, then column `j + b` inside it |
| `for a in range(k_h):` with `for b in range(k_w):` inside | | a loop inside a loop: every (a, b) pair, every cell of the kernel |
| `row = []` ... `out.append(row)` | | builds the output one row at a time |
| `range(0, 4, 2)` | | 0, 2: the top-left corners of the blocks |
| `if v > biggest: biggest = v` | | best-so-far, looking for the largest |

## 🎯 Your quest

1. `conv2d(image, kernel)`: no padding, stride 1, as above. Both are lists of rows.
2. `max_pool(image, size)`: non-overlapping `size×size` blocks (assume the sides divide evenly); return the grid of maxima.

**Part 1:** `conv2d`. Replace `return []` with:

1. `k_h = len(kernel)`
2. `k_w = len(kernel[0])`
3. `out_h = len(image) - k_h + 1`
4. `out_w = len(image[0]) - k_w + 1`
5. `out = []`
6. `for i in range(out_h):`
7. `    row = []`
8. `    for j in range(out_w):`
9. `        total = 0`
10. `        for a in range(k_h):`
11. `            for b in range(k_w):`
12. `                total = total + image[i + a][j + b] * kernel[a][b]`
13. `        row.append(total)`
14. `    out.append(row)`
15. `return out`

**Part 2:** `max_pool`. Replace `return []` with:

1. `out = []`
2. `for i in range(0, len(image), size):`
3. `    row = []`
4. `    for j in range(0, len(image[0]), size):`
5. `        biggest = image[i][j]`
6. `        for a in range(size):`
7. `            for b in range(size):`
8. `                if image[i + a][j + b] > biggest:`
9. `                    biggest = image[i + a][j + b]`
10. `        row.append(biggest)`
11. `    out.append(row)`
12. `return out`

## Review

<details><summary>Why do RNN gradients vanish over long sequences?</summary>Backprop multiplies by a factor below 1 at every step, so it shrinks exponentially.</details>
<details><summary>Why can transformers train faster than RNNs on the same hardware?</summary>All positions are processed in parallel instead of one after another.</details>
