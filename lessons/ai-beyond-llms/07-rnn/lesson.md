---
title: Recurrent networks, and why transformers won
xp: 50
---
# Reading one word at a time

> **Warm-up:** to read a sentence, you don't look at all words at once with fresh eyes each time; you carry an understanding forward. How could a network do that?

A **recurrent neural network (RNN)** keeps a **hidden state** `h`, a vector summarizing everything read so far. At each step `t` it mixes the new input `x_t` into it:

```
h_t = tanh(Wx·x_t + Wh·h_(t−1) + b)
```

The **same** weights are used at every step, so it handles any length. To predict the next word, a layer reads `h_t`. Before 2017, RNNs (especially LSTMs) powered Google Translate, speech recognition and text generation; Karpathy's 2015 *The Unreasonable Effectiveness of RNNs* is a classic read.

**The problem: vanishing gradients.** Backpropagation through time multiplies by `Wh` and the `tanh` derivative once per step. If that factor is below 1, the gradient after 50 steps is like `0.9⁵⁰ ≈ 0.005`: the network can't learn from words far back. Above 1, it explodes. **LSTMs** (1997) and GRUs add **gates** (learned sigmoids deciding what to forget, store and output) and an additive memory cell, the same "+" trick as residual connections, so information survives longer.

**Why transformers replaced them:** an RNN must process tokens one after another, so training can't be parallelized across the sequence; attention looks at all positions at once and connects any two tokens in one step.

**Possibly changing:** RNN-like models are back in a new form. **State space models** (Mamba, 2023) and RWKV have a fixed-size state (no growing KV cache) but can still train in parallel, and several recent models mix them with attention layers. Whether they replace pure transformers is still open.

## Your quest

`matvec` is given.

1. `rnn_step(x, h, Wx, Wh, b)`: return the new hidden state (apply `math.tanh` to each number).
2. `run_rnn(xs, Wx, Wh, b)`: start with `h` all zeros (length `len(b)`), apply `rnn_step` for each input, and return the list of all hidden states.

## Review

<details><summary>Define precision and recall.</summary>Precision: TP / (TP + FP). Recall: TP / (TP + FN).</details>
<details><summary>Why is accuracy misleading on imbalanced data?</summary>Always predicting the majority class scores high while catching nothing.</details>
