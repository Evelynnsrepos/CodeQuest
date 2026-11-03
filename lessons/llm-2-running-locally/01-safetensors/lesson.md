---
title: What's inside a model file? safetensors
xp: 25
---
# The training format: safetensors

> **Warm-up:** if you open a model folder on Hugging Face (say `Qwen/Qwen3-8B`), which files do you expect to find, and which one holds the weights?

A model on Hugging Face is a folder of files:

| File | What it holds |
|---|---|
| `config.json` | The architecture: layers, hidden size, heads, vocabulary size, context length |
| `tokenizer.json`, `tokenizer_config.json` | The tokenizer's vocabulary and merges, and the **chat template** |
| `model-00001-of-00004.safetensors` … | The weights, often split into several shards |
| `README.md` | The model card |

**safetensors** is the standard format for releasing and training models (PyTorch, Hugging Face `transformers`). It replaced Python "pickle" files, which could run arbitrary code when loaded. A safetensors file can't: it is only data.

Its layout is deliberately simple:

```
[ 8 bytes: header length N, little-endian integer ]
[ N bytes: JSON header                            ]
[ the raw numbers of every tensor, back to back   ]
```

The JSON header lists every **tensor** (a named block of weights) with its data type and **shape**:

```json
{"model.embed_tokens.weight": {"dtype": "BF16", "shape": [151936, 4096], "data_offsets": [0, 1244659712]},
 "__metadata__": {"format": "pt"}}
```

A tensor with shape `[151936, 4096]` holds 151,936 × 4,096 numbers. Each `BF16` number takes 2 bytes, `F32` takes 4.

safetensors weights are full precision (usually BF16) and you can't load them in LM Studio's llama.cpp engine directly. That's what GGUF (next lesson) is for. You'll come back to safetensors in Module 6, because fine-tuning happens in this format.

## Python you need

`int.from_bytes(data[0:8], "little")` turns 8 bytes into a number. `data[8:8 + n]` slices bytes. `json.loads(text)` turns JSON text into Python dictionaries and lists; `.decode("utf-8")` turns bytes into text.

## Your quest

1. Write `read_header(data)`: read the header length from the first 8 bytes, then parse the JSON that follows and return it.
2. Write `count_params(header)`: add up, for every tensor, the product of its shape. Skip the `"__metadata__"` entry. `math.prod(shape)` multiplies a list.

The starter builds a tiny fake safetensors file for you to read.

## Review

<details><summary>Why does a model "forget" the start of a long chat?</summary>The earliest messages no longer fit in the context window and are dropped from the input, so the model never sees them.</details>
<details><summary>What is a chat template?</summary>The exact format with special tokens that turns a conversation into one string, as the model was trained on.</details>
