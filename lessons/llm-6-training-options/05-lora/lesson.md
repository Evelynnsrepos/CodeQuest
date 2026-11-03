---
title: LoRA, the math
xp: 55
---
# Low-Rank Adaptation

> **Warm-up:** a weight matrix in an 8B model is 4096 × 4096 ≈ 16.8M numbers. Fine-tuning changes it to `W + ΔW`. Does `ΔW` really need 16.8M free numbers?

The LoRA paper (Hu et al., 2021) bet that it doesn't: the change needed to adapt a model has **low rank**, meaning it can be written as the product of two thin matrices:

```
ΔW = B · A          A: r × d_in      B: d_out × r      r (the rank) ≪ d, e.g. 8–64
h  = W·x + (α / r) · B·(A·x)          W stays frozen; only A and B are trained
```

For `d_in = d_out = 4096` and `r = 16`: `16 · (4096 + 4096) = 131,072` trainable numbers instead of 16.8M, **0.8%**. Across a whole model that's typically 0.1–1% of the parameters, so the optimizer state (LLMs 5, lesson 13) shrinks by the same factor.

The details that make it work:

- **Initialization:** `A` random, **`B` all zeros**. So at step 0, `B·A = 0` and the model behaves exactly like the original. Training starts from the base model, not from noise.
- **Scaling** `α / r` (`lora_alpha / r`): lets you change `r` without retuning the learning rate. Common choices: `α = r` or `α = 2r`.
- **Where:** usually all attention projections (`q_proj, k_proj, v_proj, o_proj`) and the MLP (`gate_proj, up_proj, down_proj`). Covering the MLP matters for learning new behaviour.
- **Merging:** after training, `W_merged = W + (α / r)·B·A` is an ordinary matrix of the same shape. The merged model runs **at full speed with no extra parameters**, which is how you'll get it into GGUF (lesson 10). Unmerged, the small **adapter** file (a few MB to a few hundred MB) can be swapped on and off one base model.

## Your quest

`matmul` and `matvec` are given (lists of rows).

1. `lora_params(d_in, d_out, r)`: trainable numbers for one LoRA-adapted matrix.
2. `lora_forward(W, A, B, x, alpha, r)`: `W·x + (alpha / r) · B·(A·x)`.
3. `merge(W, A, B, alpha, r)`: the merged weight matrix `W + (alpha / r) · B·A`.

The check confirms that the merged matrix gives exactly the same output as the adapter.

## Review

<details><summary>What does -100 mean in a labels list?</summary>Ignore this position in the loss; used to train only on the assistant's tokens.</details>
<details><summary>Why must the fine-tune learn to emit the end token?</summary>Otherwise the model never learns when to stop and keeps generating.</details>
