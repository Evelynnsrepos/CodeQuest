---
title: The Hugging Face stack, Unsloth and Axolotl
minutes: 30
xp: 45
hint: Start with targets = ["q_proj", "k_proj", "v_proj", "o_proj"], and if include_mlp: targets = targets + ["gate_proj", "up_proj", "down_proj"]
hint: Then config = {} and one line per key: config["r"] = r, config["lora_alpha"] = 2 * r, …, return config
hint: make_sft_config: the same, config = {} and eight lines like config["num_train_epochs"] = epochs
hint: True has a capital T and no quotes. "cosine" and "out" are text, so they have quotes.
---
# The tools you'll actually use

⏱️ About 30 minutes

> **Warm-up:** you've built every piece of a training run by hand. Which pieces would you want a library to handle for you?

All of them, at scale. The standard open-source stack (versions move fast; check each project's docs before copying code):

| Library | Job |
|---|---|
| `transformers` | load models and tokenizers by name (`AutoModelForCausalLM`, `AutoTokenizer`), apply chat templates |
| `datasets` | load and process JSONL and Hub datasets |
| `peft` | LoRA and friends: `LoraConfig`, `get_peft_model`, `merge_and_unload` |
| `bitsandbytes` | 4-bit and 8-bit quantization for QLoRA, 8-bit optimizers |
| `trl` | trainers: `SFTTrainer` (+ `SFTConfig`), `DPOTrainer`, reward modelling |
| `accelerate` | runs the same script on one GPU, many GPUs, or mixed precision |

On top of these:

- **Unsloth**: hand-optimized kernels and memory tricks that make LoRA/QLoRA training ~2× faster with less VRAM, plus ready-made notebooks and one-line GGUF export. The easiest start for single-GPU fine-tuning. It was NVIDIA-first; check its docs for the current state of AMD support.
- **Axolotl**: the same stack driven by one YAML config file; popular for reproducible runs.

A minimal SFT script with plain TRL looks like this (shape only; argument names change between versions):

```python
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

dataset = load_dataset("json", data_files={"train": "train.jsonl", "validation": "val.jsonl"})
peft_config = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05,
                         target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                                         "gate_proj", "up_proj", "down_proj"],
                         task_type="CAUSAL_LM")
args = SFTConfig(output_dir="out", num_train_epochs=2, learning_rate=2e-4,
                 per_device_train_batch_size=2, gradient_accumulation_steps=8,
                 lr_scheduler_type="cosine", warmup_ratio=0.05, logging_steps=5,
                 eval_strategy="steps", eval_steps=20, bf16=True)
trainer = SFTTrainer(model="Qwen/Qwen3-4B", args=args, peft_config=peft_config,
                     train_dataset=dataset["train"], eval_dataset=dataset["validation"])
trainer.train()
trainer.save_model("out/adapter")
```

Every line maps to something you've already built: the dataset (lesson 3), chat template and loss masking (lesson 4), LoRA (lesson 5), the knobs (lesson 7), AdamW with a cosine schedule (LLMs 5, lesson 9), the train/validation split (LLMs 5, lesson 8).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `config = {}` | | an empty dictionary |
| `config["r"] = r` | "config at r becomes r" | adds a key `"r"` with the value of the input `r` |
| `config["lora_alpha"] = 2 * r` | | a value can be computed |
| `targets + ["gate_proj"]` | | glues two lists |
| `if include_mlp:` | | only when the caller wants the MLP modules too |
| `return config` | | gives back the whole dictionary |

The key names must match **exactly** (they are what `LoraConfig(**config)` and `SFTConfig(**config)` expect).

### 👀 Worked example: a recipe dictionary

```python
def pancake(eggs, vegan=False):
    items = ["flour", "milk"]
    if not vegan:
        items = items + ["egg"]
    recipe = {}
    recipe["servings"] = eggs * 2
    recipe["items"] = items
    recipe["hot_pan"] = True
    return recipe

print(pancake(2))   # {'servings': 4, 'items': ['flour', 'milk', 'egg'], 'hot_pan': True}
```

## 🎯 Your quest

`make_lora_config(r, include_mlp=True)`: replace `return {}` with:

1. `    targets = ["q_proj", "k_proj", "v_proj", "o_proj"]`
2. `    if include_mlp:`
3. `        targets = targets + ["gate_proj", "up_proj", "down_proj"]`
4. `    config = {}`
5. `    config["r"] = r`
6. `    config["lora_alpha"] = 2 * r`
7. `    config["lora_dropout"] = 0.05`
8. `    config["target_modules"] = targets`
9. `    config["task_type"] = "CAUSAL_LM"`
10. `    return config`

`make_sft_config(epochs, lr, per_device, accumulation)`: replace `return {}` with:

1. `    config = {}`
2. `    config["output_dir"] = "out"`
3. `    config["num_train_epochs"] = epochs`
4. `    config["learning_rate"] = lr`
5. `    config["per_device_train_batch_size"] = per_device`
6. `    config["gradient_accumulation_steps"] = accumulation`
7. `    config["lr_scheduler_type"] = "cosine"`
8. `    config["warmup_ratio"] = 0.05`
9. `    config["bf16"] = True`
10. `    return config`

## Review

<details><summary>How do you compute the effective batch size?</summary>Per-device batch × gradient accumulation steps × number of GPUs.</details>
<details><summary>What's a typical LoRA learning rate, and why is it higher than for full fine-tuning?</summary>About 1e-4 to 2e-4; the LoRA update B·A starts at zero (only B is zeros; A is random) and stays small, so they tolerate bigger steps.</details>
