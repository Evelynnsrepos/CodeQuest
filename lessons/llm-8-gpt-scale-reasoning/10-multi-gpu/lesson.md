---
title: Training on many GPUs
minutes: 40
xp: 50
hint: all_reduce_mean: n = len(grads_per_gpu), out = [], for i in range(len(grads_per_gpu[0])): total = 0, add g[i] for each g, out.append(total / n)
hint: zero_memory_gb: if stage == 0: per_param = 16, elif stage == 1: 4 + 12 / gpus, elif stage == 2: 2 + 14 / gpus, else: 16 / gpus
hint: zero_memory_gb ends: return params * per_param / 1e9
---
# One GPU isn't enough

⏱️ About 40 minutes

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

## 🔬 Take the table apart

The 16 bytes per parameter (LLMs 5, lesson 13) are 2 (weights) + 2 (gradients) + 12 (FP32 copy + Adam's m and v). ZeRO splits ("shards") parts of them across n GPUs, so each GPU keeps only 1/n of those parts:

- Stage 1: optimizer state (12) is split → 4 + 12/n
- Stage 2: + gradients (2) → 2 + 14/n
- Stage 3: + weights → 16/n, everything split

Numbers, 8B parameters on 8 GPUs, stage 1: 4 + 12/8 = 5.5 bytes. 8 × 10⁹ × 5.5 = 44 × 10⁹ bytes = **44 GB** per GPU.

**All-reduce mean**: every GPU computed gradients on different data; they average them so all GPUs take the same step. For position 0: (0.2 + 0.4 + 0.0 + 0.2) / 4 = **0.2**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `grads_per_gpu[0]` | | the first GPU's list; its length = number of gradients |
| `g[i]` | | gradient i from one GPU |
| `if … elif … elif … else:` | | exactly one branch runs |
| `stage == 0` | "stage equals 0" | `==` compares |

### 👀 Worked example: averaging two GPUs

```python
grads = [[1.0, 4.0], [3.0, 0.0]]
out = []
for i in range(2):
    total = 0
    for g in grads:
        total = total + g[i]
    out.append(total / 2)
print(out)     # [2.0, 2.0]
```

## 🎯 Your quest

`all_reduce_mean(grads_per_gpu)`: replace `return grads_per_gpu[0]` with:

1. `    n = len(grads_per_gpu)`
2. `    out = []`
3. `    for i in range(len(grads_per_gpu[0])):`
4. `        total = 0`
5. `        for g in grads_per_gpu:`
6. `            total = total + g[i]`
7. `        out.append(total / n)`
8. `    return out`

`zero_memory_gb(params, gpus, stage)`: replace `return 0.0` with:

1. `    if stage == 0:`
2. `        per_param = 16`
3. `    elif stage == 1:`
4. `        per_param = 4 + 12 / gpus`
5. `    elif stage == 2:`
6. `        per_param = 2 + 14 / gpus`
7. `    else:`
8. `        per_param = 16 / gpus`
9. `    return params * per_param / 1e9`

It prints 128, 44, 30 and 16 GB per GPU.

## Review

<details><summary>What does near-duplicate detection compare?</summary>Sets of n-word shingles, with Jaccard similarity (MinHash + LSH at scale).</details>
<details><summary>Why remove benchmark questions from training data?</summary>Otherwise the evaluation measures memorization (contamination), not ability.</details>
