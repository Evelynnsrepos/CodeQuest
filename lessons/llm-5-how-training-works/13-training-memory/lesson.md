---
title: Scaling up: PyTorch, precision and training memory
minutes: 40
xp: 45
hint: gpt_params: return 12 * layers * d ** 2 + vocab * d
hint: full_finetune_gb: return params * 16 / 1e9
hint: qlora_gb: return (params * 0.5 + trainable * 16) / 1e9
hint: Fits? Add the activations (3 GB) to each answer and compare with 12. full_8b_fits = False, qlora_8b_fits = True
---
# Why you can run an 8B model but not fully train one

⏱️ About 40 minutes

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

## 🔬 Take the formulas apart

**Bytes and GB.** One byte is 8 bits. **1 GB** here is 10⁹ bytes (a billion; Python `1e9`). So "bytes ÷ 1e9" gives GB.

**Parameter count** <div class="formula">params ≈ <span class="k1">12</span> · <span class="k2">L</span> · <span class="k3">d²</span> + <span class="k4">vocab · d</span></div>
- <span class="k2">L</span> = number of layers, <span class="k3">d</span> = width (the size of each token vector). d² = d × d.
- <span class="k1">12</span>: each layer has about 4·d² weights in attention (Q, K, V and the output, each d × d) and 8·d² in the MLP. 4 + 8 = 12.
- <span class="k4">vocab · d</span>: the embedding table, one vector of size d per token.

Numbers, GPT-2 small (L = 12, d = 768, vocab = 50,257):
1. d² = 768 × 768 = 589,824
2. 12 × 12 × 589,824 = 84,934,656 (about 85M)
3. 50,257 × 768 = 38,597,376 (about 39M)
4. Total ≈ **124M**. The real GPT-2 small has 124M. ✅

**Full fine-tune** <div class="formula">GB = params × <span class="k1">16</span> / 10⁹</div>
<span class="k1">16</span> bytes per parameter (the table above). 8 × 10⁹ × 16 = 128 × 10⁹ bytes = **128 GB**.

**QLoRA** <div class="formula">GB = (params × <span class="k1">0.5</span> + trainable × <span class="k2">16</span>) / 10⁹</div>
- <span class="k1">0.5</span> byte per frozen weight (4 bits = half a byte).
- <span class="k2">16</span> bytes only for the few trainable ones.

8B model, 40M trainable: 8 × 10⁹ × 0.5 = 4 × 10⁹, plus 40 × 10⁶ × 16 = 0.64 × 10⁹. Total 4.64 × 10⁹ bytes ≈ **4.6 GB**.

**Does it fit in 12 GB?** Add about 3 GB of activations:
- Full: 128 + 3 = 131 GB. Far more than 12 → **False**.
- QLoRA: 4.6 + 3 ≈ 7.6 GB. Less than 12 → **True**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `d ** 2` | "d squared" | d × d |
| `params * 16 / 1e9` | | bytes, then GB |
| `(a + b) / 1e9` | | the brackets add first, then divide |
| `True`, `False` | | Python's yes and no. Capital first letter, no quotes. |

### 👀 Worked example: a tiny model

L = 2, d = 10, vocab = 30: 12 × 2 × 100 + 30 × 10 = 2,400 + 300 = **2,700** parameters. Full fine-tune memory: 2,700 × 16 = 43,200 bytes = 0.0000432 GB.

## 🎯 Your quest

Replace each `return 0`:

`gpt_params(layers, d, vocab)`: `    return 12 * layers * d ** 2 + vocab * d`

`full_finetune_gb(params)`: `    return params * 16 / 1e9`

`qlora_gb(params, trainable)`: `    return (params * 0.5 + trainable * 16) / 1e9`

Then answer with `True` or `False` (see "Does it fit" above):

1. `full_8b_fits = False`
2. `qlora_8b_fits = True`

## Review

<details><summary>What does a causal mask do?</summary>It stops each position from attending to later positions, so the model can't see the token it must predict.</details>
<details><summary>Why can a transformer learn from every position of a sequence in one pass?</summary>The causal mask makes each position's prediction depend only on earlier tokens, so all T predictions are valid training examples at once.</details>
