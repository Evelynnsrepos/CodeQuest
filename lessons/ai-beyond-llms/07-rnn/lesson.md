---
title: Recurrent networks, and why transformers won
minutes: 40
xp: 50
hint: rnn_step: a = matvec(Wx, x) and c = matvec(Wh, h), then new_h = []
hint: rnn_step: for i in range(len(b)): new_h.append(math.tanh(a[i] + c[i] + b[i])). Then return new_h
hint: run_rnn: h = [0.0] * len(b) and states = [], then for x in xs: h = rnn_step(x, h, Wx, Wh, b) and states.append(h)
---
# Reading one word at a time

⏱️ About 40 minutes

> **Warm-up:** to read a sentence, you don't look at all words at once with fresh eyes each time; you carry an understanding forward. How could a network do that?

A **recurrent neural network (RNN)** keeps a **hidden state** `h`, a vector summarizing everything read so far. At each step `t` it mixes the new input `x_t` into it:

```
h_t = tanh(Wx·x_t + Wh·h_(t−1) + b)
```

The **same** weights are used at every step, so it handles any length. To predict the next word, a layer reads `h_t`. Before 2017, RNNs (especially LSTMs) powered Google Translate, speech recognition and text generation; Karpathy's 2015 *The Unreasonable Effectiveness of RNNs* is a classic read.

**The problem: vanishing gradients.** Backpropagation through time multiplies by `Wh` and the `tanh` derivative once per step. If that factor is below 1, the gradient after 50 steps is like `0.9⁵⁰ ≈ 0.005`: the network can't learn from words far back. Above 1, it explodes. **LSTMs** (1997) and GRUs add **gates** (learned sigmoids deciding what to forget, store and output) and an additive memory cell, the same "+" trick as residual connections, so information survives longer.

**Why transformers replaced them:** an RNN must process tokens one after another, so training can't be parallelized across the sequence; attention looks at all positions at once and connects any two tokens in one step.

**Possibly changing:** RNN-like models are back in a new form. **State space models** (Mamba, 2023) and RWKV have a fixed-size state (no growing KV cache) but can still train in parallel, and several recent models mix them with attention layers. Whether they replace pure transformers is still open.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">h_t</span> = tanh( <span class="k2">Wx·x_t</span> + <span class="k3">Wh·h_(t−1)</span> + <span class="k4">b</span> )</div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">h_t</span> | "h at step t" | the new memory after reading input number t |
| <span class="k3">h_(t−1)</span> | "h at step t minus one" | the memory from the step **before** |
| <span class="k2">Wx·x_t</span> | "W x times x t" | a matrix times a vector (LLMs 4, lesson 04): each **row** of Wx is dotted with x_t, giving one number per row |
| <span class="k4">b</span> | "b" | the bias, one number per hidden unit |
| `tanh` | "tanch" | squashes any number into −1 .. 1: tanh(0) = 0, tanh(1) = 0.76, tanh(2) = 0.96, tanh(−2) = −0.96 |

**One hidden unit, two steps**, with Wx = [[1.0]], Wh = [[0.5]], b = [0], inputs 1 then 0:

1. Start: h = [0].
2. Step 1, x = [1]: Wx·x = 1 × 1 = 1. Wh·h = 0.5 × 0 = 0. Add b: 1 + 0 + 0 = 1. tanh(1) = **0.762**.
3. Step 2, x = [0]: Wx·x = 0. Wh·h = 0.5 × 0.762 = 0.381. Add: 0 + 0.381 + 0 = 0.381. tanh(0.381) = **0.363**.

Even with an input of 0, the memory from step 1 is still there, just fainter. That's the whole idea.

**The vanishing gradient**, 0.9⁵⁰: the raised 50 means "0.9 times itself 50 times". 0.9 × 0.9 = 0.81, × 0.9 = 0.729, ... after 50 times: 0.005. A signal that loses 10% at every step is almost gone after 50.

## 🐍 Python you need

`matvec(W, x)` is **given**: it does the matrix-times-vector part and returns a list.

| You write | Say it | What it does |
|---|---|---|
| `a = matvec(Wx, x)` | | the list Wx·x |
| `for i in range(len(b)):` | | once per hidden unit |
| `math.tanh(v)` | "tanch of v" | the squash |
| `a[i] + c[i] + b[i]` | | adds the three lists number by number |
| `[0.0] * len(b)` | | a starting memory of zeros, one per hidden unit |
| `h = rnn_step(x, h, ...)` | | the new memory replaces the old one, and the next round uses it |

## 🎯 Your quest

`matvec` is given.

1. `rnn_step(x, h, Wx, Wh, b)`: return the new hidden state (apply `math.tanh` to each number).
2. `run_rnn(xs, Wx, Wh, b)`: start with `h` all zeros (length `len(b)`), apply `rnn_step` for each input, and return the list of all hidden states.

**Part 1:** `rnn_step`. Replace `return h` with:

1. `a = matvec(Wx, x)`
2. `c = matvec(Wh, h)`
3. `new_h = []`
4. `for i in range(len(b)):`
5. `    new_h.append(math.tanh(a[i] + c[i] + b[i]))`
6. `return new_h`

**Part 2:** `run_rnn`. Replace `return []` with:

1. `h = [0.0] * len(b)`
2. `states = []`
3. `for x in xs:`
4. `    h = rnn_step(x, h, Wx, Wh, b)`
5. `    states.append(h)`
6. `return states`

## Review

<details><summary>Define precision and recall.</summary>Precision: TP / (TP + FP). Recall: TP / (TP + FN).</details>
<details><summary>Why is accuracy misleading on imbalanced data?</summary>Always predicting the majority class scores high while catching nothing.</details>
