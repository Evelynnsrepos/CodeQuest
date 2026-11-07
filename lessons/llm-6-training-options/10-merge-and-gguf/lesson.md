---
title: Merging adapters and converting to GGUF
minutes: 30
xp: 45
hint: Build the file names first: f16 = name + "-F16.gguf" and quantized = name + "-" + quant + ".gguf"
hint: Glue each command with +, and don't forget the spaces inside the quotes: "llama-quantize " + f16 + " " + quantized + " " + quant
hint: return [convert, shrink, load], a list of the three texts
hint: merge_dtype: merging into the 4-bit base bakes in quantization error, so use "bf16"
---
# From adapter to LM Studio

⏱️ About 30 minutes

> **Warm-up:** training gave you a folder with a 160 MB adapter. LM Studio wants one GGUF file. List the steps in between.

The path from a trained LoRA to a model in LM Studio:

```
base model (safetensors) + adapter
   │  1. merge (peft)
   ▼
merged model (safetensors, BF16)
   │  2. convert (llama.cpp: convert_hf_to_gguf.py)
   ▼
model-F16.gguf
   │  3. quantize (llama.cpp: llama-quantize)
   ▼
model-Q4_K_M.gguf
   │  4. import (lms import, or copy into ~/.lmstudio/models/<publisher>/<name>/)
   ▼
LM Studio
```

**1. Merge.** Load the base model in **BF16** (not 4-bit!), attach the adapter and fold it in: `W + (α/r)·B·A` from lesson 5.

```python
base = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-4B", torch_dtype=torch.bfloat16)
model = PeftModel.from_pretrained(base, "out/adapter").merge_and_unload()
model.save_pretrained("merged")
AutoTokenizer.from_pretrained("Qwen/Qwen3-4B").save_pretrained("merged")   # keeps the chat template
```

Merging into the 4-bit QLoRA base would bake quantization error into every weight *before* you quantize again for GGUF. Merge into BF16, then quantize once.

**2–3. Convert and quantize** with llama.cpp (`git clone` it; the converter is a Python script, `llama-quantize` is a built program, also in nixpkgs' `llama-cpp`):

```bash
python convert_hf_to_gguf.py merged --outfile my-model-F16.gguf --outtype f16
llama-quantize my-model-F16.gguf my-model-Q4_K_M.gguf Q4_K_M
```

**4. Load it.** `lms import my-model-Q4_K_M.gguf`, then check the chat template LM Studio picked up, and test with the prompts you held out.

Alternatives: Unsloth can do merge + convert + quantize in one call (`save_pretrained_gguf`); and llama.cpp can load an **unmerged** adapter converted with `convert_lora_to_gguf.py`, applied at load time with `--lora`. Script names and flags change occasionally; `--help` is your friend.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `name + "-F16.gguf"` | | glues texts: `"my-model" + "-F16.gguf"` → `"my-model-F16.gguf"` |
| `"lms import " + quantized` | | note the space before the closing quote, so the words don't stick together |
| `return [a, b, c]` | | a list of three texts |

### 👀 Worked example: the commands for "my-model"

With `merged_dir = "merged"`, `name = "my-model"`, `quant = "Q4_K_M"`:

1. f16 = `"my-model-F16.gguf"`, quantized = `"my-model-Q4_K_M.gguf"`
2. `python convert_hf_to_gguf.py merged --outfile my-model-F16.gguf --outtype f16`
3. `llama-quantize my-model-F16.gguf my-model-Q4_K_M.gguf Q4_K_M`
4. `lms import my-model-Q4_K_M.gguf`

These are exactly the three lines from the text above.

## 🎯 Your quest

**Part 1:** `gguf_commands(merged_dir, name, quant)`. Replace `return []` with:

1. `    f16 = name + "-F16.gguf"`
2. `    quantized = name + "-" + quant + ".gguf"`
3. `    convert = "python convert_hf_to_gguf.py " + merged_dir + " --outfile " + f16 + " --outtype f16"`
4. `    shrink = "llama-quantize " + f16 + " " + quantized + " " + quant`
5. `    load = "lms import " + quantized`
6. `    return [convert, shrink, load]`

**Part 2:** set `merge_dtype` to `"bf16"` or `"4bit"`: what should the base model be loaded as before merging? (Reread the paragraph about baking in quantization error.)

## Review

<details><summary>Write the DPO loss.</summary>−log σ(β·[(log π(chosen) − log π_ref(chosen)) − (log π(rejected) − log π_ref(rejected))])</details>
<details><summary>Why does DPO not need a reward model?</summary>It optimizes the preference objective directly with a classification-style loss; the implicit reward is β times the log-probability change versus the reference.</details>
