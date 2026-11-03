---
title: Scaling up: PyTorch, precision and training memory
xp: 45
---
# Why you can run an 8B model but not fully train one

> **Warm-up:** an 8B model at Q4 runs comfortably in your 12 GB. How much memory do you think *training* all of its weights would need?

Your micrograd handles one number at a time. **PyTorch** does the same thing on **tensors** (n-dimensional arrays) on the GPU: `loss.backward()` walks the graph exactly like your `backward()`, just over millions of numbers per operation. Same five-step loop, same ideas; only the scale changes. And scale is all about memory.

**Training memory per parameter** with AdamW in the standard mixed-precision recipe:

| What | Bytes per parameter |
|---|---|
| weights in BF16 (used in forward/backward) | 2 |
| gradients in BF16 | 2 |
| FP32 master copy of the weights | 4 |
| Adam's `m` and `v` in FP32 | 8 |
| **total** | **16** |

So full fine-tuning of an 8B model needs ~128 GB **before** counting **activations** (the intermediate values saved during the forward pass for use in backward, which grow with batch size × sequence length). That's several data-centre GPUs. Tricks that help: **gradient checkpointing** (recompute activations instead of storing them), **gradient accumulation** (small batches), 8-bit optimizers, and sharding across GPUs (FSDP, DeepSpeed ZeRO).

**BF16** (bfloat16) has the same range as FP32 with less precision, which makes it the standard training format: FP16's smaller range causes overflow, and FP32 is twice the memory.

The way out on a 12 GB card is to **not train most weights at all**. **QLoRA** (Module 6) stores the frozen base model in 4 bits (~0.5 bytes per parameter) and trains only small added matrices, typically 0.1–1% of the parameters, at the full 16 bytes each:

```
QLoRA memory ≈ params × 0.5  +  trainable params × 16  +  activations
```

A rough parameter count for a GPT-style model with `L` layers and width `d` (attention 4d², MLP 8d² per layer):

```
params ≈ 12 · L · d²   (+ vocab × d for the embeddings)
```

## Your quest

1. `gpt_params(layers, d, vocab)`: `12·L·d² + vocab·d`.
2. `full_finetune_gb(params)`: 16 bytes per parameter, in GB (1e9 bytes).
3. `qlora_gb(params, trainable)`: `params × 0.5 + trainable × 16` bytes, in GB.
4. Set `full_8b_fits` and `qlora_8b_fits` (True / False) for an 8B model on 12 GB, with 40M trainable LoRA parameters and about 3 GB of activations.

## Review

<details><summary>What does a causal mask do?</summary>It stops each position from attending to later positions, so the model can't see the token it must predict.</details>
<details><summary>Why can a transformer learn from every position of a sequence in one pass?</summary>The causal mask makes each position's prediction depend only on earlier tokens, so all T predictions are valid training examples at once.</details>
