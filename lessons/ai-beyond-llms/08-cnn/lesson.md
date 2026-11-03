---
title: Convolutions: how computers learned to see
xp: 50
---
# One small filter, slid everywhere

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

## Your quest

1. `conv2d(image, kernel)`: no padding, stride 1, as above. Both are lists of rows.
2. `max_pool(image, size)`: non-overlapping `size×size` blocks (assume the sides divide evenly); return the grid of maxima.

## Review

<details><summary>Why do RNN gradients vanish over long sequences?</summary>Backprop multiplies by a factor below 1 at every step, so it shrinks exponentially.</details>
<details><summary>Why can transformers train faster than RNNs on the same hardware?</summary>All positions are processed in parallel instead of one after another.</details>
