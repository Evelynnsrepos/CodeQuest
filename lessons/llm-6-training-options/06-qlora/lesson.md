---
title: QLoRA, fine-tuning on a 12 GB card
xp: 45
---
# LoRA on a 4-bit base model

> **Warm-up:** LoRA shrinks the *trainable* part. What is still taking most of the memory?

The frozen base weights, in BF16: 16 GB for an 8B model. **QLoRA** (Dettmers et al., 2023) stores them in **4 bits** instead, and trains LoRA adapters on top. Three ideas from the paper:

- **NF4 (4-bit NormalFloat)**: trained weights are roughly normally distributed, so instead of 16 evenly spaced levels (LLMs 2, lesson 3), NF4 places its 16 levels at the quantiles of a normal distribution: more levels where weights are dense. Blocks of 64 weights share a scale.
- **Double quantization**: those per-block scales are themselves quantized, saving another ~0.4 bits per weight.
- **Paged optimizers**: optimizer state can spill to CPU RAM during memory spikes instead of crashing with out-of-memory.

During the forward and backward pass, each 4-bit block is **dequantized to BF16 on the fly** for the matmul; gradients flow *through* the frozen weights into the LoRA matrices, which stay in BF16. The paper showed QLoRA matches 16-bit LoRA quality on their benchmarks.

In code (Hugging Face `transformers` + `bitsandbytes`; names as of 2025, check current docs):

```python
from transformers import BitsAndBytesConfig
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                         bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-4B", quantization_config=bnb)
```

How many parameters does LoRA train? Every targeted matrix adds `r · (d_in + d_out)`. For Llama 3.1 8B (from its `config.json`):

```
q_proj 4096→4096   k_proj 4096→1024   v_proj 4096→1024   o_proj 4096→4096
gate_proj 4096→14336   up_proj 4096→14336   down_proj 14336→4096       × 32 layers
```

## Your quest

1. `module_shapes(config)`: a dictionary from module name to `(d_in, d_out)` for the seven modules above, computed from a config (use `head_dim = hidden_size // num_attention_heads`; `k_proj` and `v_proj` output `num_key_value_heads × head_dim`).
2. `lora_trainable(config, r, targets)`: total trainable parameters for LoRA rank `r` on the modules in `targets`, across all layers.
3. Run it and look at the share for "attention only" vs "all seven".

## Review

<details><summary>Why does LoRA initialize B to zeros?</summary>So B·A = 0 at the start and the model begins exactly as the base model.</details>
<details><summary>How do you merge a LoRA adapter?</summary>W_merged = W + (α/r)·B·A, an ordinary matrix with no extra cost at inference.</details>
