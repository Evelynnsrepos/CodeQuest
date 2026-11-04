---
title: Training on many GPUs
xp: 50
---
# One GPU isn't enough

> **Warm-up:** full training of an 8B model needs about 16 bytes per parameter (LLMs 5, lesson 13). How many GB is that, and how does it compare to an 80 GB GPU?

128 GB: too much for one GPU, before even counting activations. Large-scale training combines several kinds of parallelism:

- **Data parallel (DDP):** every GPU holds a full copy of the model and processes a different slice of the batch. After the backward pass, an **all-reduce** averages the gradients across GPUs, so every copy takes the same step and stays identical. Averaging over GPUs is exactly the same as one big batch.
- **ZeRO / FSDP** (DeepSpeed, PyTorch FSDP): data parallel, but instead of every GPU storing everything, they **shard** (split) the state across the `n` GPUs. With mixed precision, per parameter: 2 bytes bf16 weights, 2 bytes gradients, 12 bytes optimizer state (fp32 master weights + Adam's m and v).

| Stage | What is sharded | Bytes per parameter per GPU |
|---|---|---|
| 0 (plain DDP) | nothing | 16 |
| 1 | optimizer state | 4 + 12/n |
| 2 | + gradients | 2 + 14/n |
| 3 (= FSDP full shard) | + weights | 16/n |

- **Tensor parallel:** split each matrix across GPUs inside a layer (needs very fast links like NVLink).
- **Pipeline parallel:** different layers on different GPUs, with micro-batches flowing through like an assembly line.

Llama 3 405B was trained on 16,384 H100 GPUs combining all four ("4D parallelism"). For you: the libraries (Accelerate, DeepSpeed, FSDP) do this with config flags, and a rented multi-GPU box is the realistic way to try it.

## Your quest

1. `all_reduce_mean(grads_per_gpu)`: a list of equal-length gradient lists, one per GPU. Return their element-wise average.
2. `zero_memory_gb(params, gpus, stage)`: GB (1e9 bytes) per GPU from the table (activations not included).

## Review

<details><summary>What does near-duplicate detection compare?</summary>Sets of n-word shingles, with Jaccard similarity (MinHash + LSH at scale).</details>
<details><summary>Why remove benchmark questions from training data?</summary>Otherwise the evaluation measures memorization (contamination), not ability.</details>
