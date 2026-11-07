---
title: QLoRA, fine-tuning on a 12 GB card
minutes: 50
xp: 45
hint: module_shapes: h = config["hidden_size"], head_dim = h // config["num_attention_heads"], kv = config["num_key_value_heads"] * head_dim, i = config["intermediate_size"]
hint: Then shapes = {} and one line per module, like shapes["k_proj"] = (h, kv) and shapes["down_proj"] = (i, h). return shapes
hint: lora_trainable: shapes = module_shapes(config), per_layer = 0, for t in targets: d_in, d_out = shapes[t] and per_layer = per_layer + r * (d_in + d_out)
hint: lora_trainable ends: return per_layer * config["num_hidden_layers"]
---
# LoRA on a 4-bit base model

⏱️ About 50 minutes

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

## 🔬 Take the formula apart

Each LoRA'd module costs r · (d_in + d_out) (lesson 5). Add that over the chosen modules, then multiply by the number of layers:

<div class="formula">trainable = <span class="k1">Σ over targets</span> r · (d_in + d_out) <span class="k2">× layers</span></div>

**Where the sizes come from** (Llama 3.1 8B):
- `head_dim` = 4096 ÷ 32 heads = **128**. `//` is division that drops the remainder, so the answer is a whole number.
- k and v are smaller (grouped-query attention): 8 key-value heads × 128 = **1024**.

**Numbers, attention only**, r = 16, one layer:
1. q_proj: 16 × (4096 + 4096) = 131,072
2. k_proj: 16 × (4096 + 1024) = 81,920
3. v_proj: the same, 81,920
4. o_proj: 131,072
5. One layer: 425,984. × 32 layers = **13,631,488**, about 0.17% of 8 billion.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `config["hidden_size"]` | | read a setting from the dictionary |
| `4096 // 32` | "4096 floor-divided by 32" | `128`. Whole-number division. |
| `shapes = {}` then `shapes["q_proj"] = (h, h)` | | an empty dictionary, then one entry at a time. `(h, h)` is a pair. |
| `d_in, d_out = shapes[t]` | | takes the pair apart |
| `for t in targets:` | | each module name in the list |

### 👀 Worked example: a tiny model

`{"hidden_size": 8, "num_attention_heads": 2, "num_key_value_heads": 1, "intermediate_size": 16, "num_hidden_layers": 2}`, r = 1, targets `["q_proj", "k_proj"]`:

1. head_dim = 8 // 2 = 4, kv = 1 × 4 = 4.
2. q_proj (8, 8): 1 × 16 = 16. k_proj (8, 4): 1 × 12 = 12.
3. Per layer 28, × 2 layers = **56**.

## 🎯 Your quest

`module_shapes(config)`: replace `return {}` with:

1. `    h = config["hidden_size"]`
2. `    head_dim = h // config["num_attention_heads"]`
3. `    kv = config["num_key_value_heads"] * head_dim`
4. `    i = config["intermediate_size"]`
5. `    shapes = {}`
6. `    shapes["q_proj"] = (h, h)`
7. `    shapes["k_proj"] = (h, kv)`
8. `    shapes["v_proj"] = (h, kv)`
9. `    shapes["o_proj"] = (h, h)`
10. `    shapes["gate_proj"] = (h, i)`
11. `    shapes["up_proj"] = (h, i)`
12. `    shapes["down_proj"] = (i, h)`
13. `    return shapes`

`lora_trainable(config, r, targets)`: replace `return 0` with:

1. `    shapes = module_shapes(config)`
2. `    per_layer = 0`
3. `    for t in targets:`
4. `        d_in, d_out = shapes[t]`
5. `        per_layer = per_layer + r * (d_in + d_out)`
6. `    return per_layer * config["num_hidden_layers"]`

Run it: attention only is 13.6M (0.17%), all seven 41.9M (0.52%). Even "all seven" trains about half a percent of the model.

## Review

<details><summary>Why does LoRA initialize B to zeros?</summary>So B·A = 0 at the start and the model begins exactly as the base model.</details>
<details><summary>How do you merge a LoRA adapter?</summary>W_merged = W + (α/r)·B·A, an ordinary matrix with no extra cost at inference.</details>
