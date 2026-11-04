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

<svg viewBox="0 0 560 230" width="100%" style="max-width:560px" role="img" aria-label="LoRA: the big weight matrix W stays frozen; two small matrices B and A, with rank r, are trained, and the output is W x plus B A x"><defs><marker id="ah4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs><text x="70" y="20" font-size="12" fill="currentColor" text-anchor="middle" font-weight="normal">frozen</text><rect x="20" y="30" width="100" height="100" rx="6" fill="currentColor" fill-opacity=".08" stroke="currentColor" stroke-opacity=".5" stroke-width="2"/><text x="70" y="78" font-size="22" fill="currentColor" text-anchor="middle" font-weight="normal">W</text><text x="70" y="98" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">d × d</text><text x="70" y="150" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">4096 × 4096</text><text x="70" y="166" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">= 16.8 M numbers</text><text x="160" y="85" font-size="26" fill="currentColor" text-anchor="middle" font-weight="normal">+</text><text x="260" y="20" font-size="12" fill="#30a46c" text-anchor="middle" font-weight="normal">trained</text><rect x="190" y="30" width="16" height="100" rx="3" fill="#30a46c" fill-opacity=".25" stroke="#30a46c" stroke-width="2"/><text x="198" y="146" font-size="16" fill="currentColor" text-anchor="middle" font-weight="normal">B</text><text x="198" y="162" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">d × r</text><text x="222" y="85" font-size="20" fill="currentColor" text-anchor="middle" font-weight="normal">×</text><rect x="236" y="62" width="100" height="16" rx="3" fill="#30a46c" fill-opacity=".25" stroke="#30a46c" stroke-width="2"/><text x="286" y="100" font-size="16" fill="currentColor" text-anchor="middle" font-weight="normal">A</text><text x="286" y="116" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">r × d</text><text x="262" y="192" font-size="12" fill="#30a46c" text-anchor="middle" font-weight="normal">r = 16: 2 · 4096 · 16 = 131 k numbers (0.8%)</text><line x1="350" y1="80" x2="400" y2="80" stroke="currentColor" stroke-width="1.6" marker-end="url(#ah4)"/><rect x="404" y="50" width="140" height="60" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="474.0" y="78.0" font-size="14" fill="currentColor" text-anchor="middle">output</text><text x="474.0" y="94.0" font-size="11" fill="currentColor" opacity=".75" text-anchor="middle">W·x + B·A·x</text><text x="474" y="140" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">B starts at 0,</text><text x="474" y="156" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">so at first the output</text><text x="474" y="172" font-size="11" fill="currentColor" text-anchor="middle" font-weight="normal">is exactly W·x</text></svg>

## Your quest

`matmul` and `matvec` are given (lists of rows).

1. `lora_params(d_in, d_out, r)`: trainable numbers for one LoRA-adapted matrix.
2. `lora_forward(W, A, B, x, alpha, r)`: `W·x + (alpha / r) · B·(A·x)`.
3. `merge(W, A, B, alpha, r)`: the merged weight matrix `W + (alpha / r) · B·A`.

The check confirms that the merged matrix gives exactly the same output as the adapter.

## Review

<details><summary>What does -100 mean in a labels list?</summary>Ignore this position in the loss; used to train only on the assistant's tokens.</details>
<details><summary>Why must the fine-tune learn to emit the end token?</summary>Otherwise the model never learns when to stop and keeps generating.</details>
