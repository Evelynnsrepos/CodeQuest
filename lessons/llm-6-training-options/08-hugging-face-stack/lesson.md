---
title: The Hugging Face stack, Unsloth and Axolotl
xp: 45
---
# The tools you'll actually use

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

## Your quest

Write `make_lora_config(r, include_mlp=True)` and `make_sft_config(epochs, lr, per_device, accumulation)` returning plain dictionaries with exactly the keys used above:

- LoRA: `r`, `lora_alpha` (= `2 * r`), `lora_dropout` (0.05), `target_modules` (the four attention modules, plus the three MLP modules if `include_mlp`), `task_type` (`"CAUSAL_LM"`).
- SFT: `output_dir` (`"out"`), `num_train_epochs`, `learning_rate`, `per_device_train_batch_size`, `gradient_accumulation_steps`, `lr_scheduler_type` (`"cosine"`), `warmup_ratio` (0.05), `bf16` (`True`).

## Review

<details><summary>How do you compute the effective batch size?</summary>Per-device batch × gradient accumulation steps × number of GPUs.</details>
<details><summary>What's a typical LoRA learning rate, and why is it higher than for full fine-tuning?</summary>About 1e-4 to 2e-4; the LoRA matrices start at zero and are small, so they tolerate bigger steps.</details>
