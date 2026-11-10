---
title: What's inside a model file? safetensors
minutes: 35
xp: 25
hint: read_header, line 1: n = int.from_bytes(data[0:8], "little")
hint: read_header, line 2: return json.loads(data[8:8 + n].decode("utf-8"))
hint: count_params: for name in header: and inside it if name == "__metadata__": continue
hint: Still in the loop: size = 1, then for number in header[name]["shape"]: size = size * number, then total = total + size
---
# The training format: safetensors

⏱️ About 35 minutes

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

## 🔬 Bytes and shapes, with numbers

A **byte** is the smallest piece of a file: a whole number from 0 to 255. Big numbers need several bytes. "Little-endian" just says in which order those bytes are written (smallest part first). Python reads them for you with `int.from_bytes`.

A tensor's **shape** says how its numbers are arranged. Shape `[1000, 64]` is a table with 1,000 rows and 64 columns, so it holds 1,000 × 64 = **64,000** numbers. Shape `[64]` is one row of 64 numbers. To count the numbers, **multiply all the numbers in the shape**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `data[0:8]` | "data from 0 up to 8" | a **slice**: the bytes at positions 0 to 7 (8 is not included) |
| `int.from_bytes(b, "little")` | | turns those bytes into one whole number |
| `data[8:8 + n]` | | the `n` bytes right after the first 8: the JSON header |
| `.decode("utf-8")` | "decode as text" | turns bytes into normal text |
| `json.loads(text)` | "JSON load string" | turns JSON text into Python dictionaries and lists |
| `for name in header:` | | goes through the dictionary's keys: the tensor names |
| `continue` | | skip the rest of this round, go to the next name |
| `header[name]["shape"]` | | the shape list of that tensor, like `[1000, 64]` |
| `size = size * number` | | a running **product**: like a running total, but multiplying. Start at 1, not 0 (0 times anything is 0). |

### 👀 Worked example: how many eggs in the boxes?

Each box has a shape: rows × columns of eggs. Skip the label.

```python
boxes = {"small": [2, 3], "big": [4, 5, 2], "label": "eggs"}
total = 0
for name in boxes:
    if name == "label":
        continue
    size = 1
    for number in boxes[name]:
        size = size * number
    total = total + size
print(total)   # 46
```

1. "small": size = 1 × 2 × 3 = **6**. total = 6.
2. "big": size = 1 × 4 × 5 × 2 = **40**. total = 46.
3. "label": skipped by `continue`.

## 🎯 Your quest

The starter builds a tiny fake safetensors file for you to read.

**Part 1:** `read_header(data)`. Make it read:

1. `n = int.from_bytes(data[0:8], "little")`
2. `return json.loads(data[8:8 + n].decode("utf-8"))`

**Part 2:** `count_params(header)`. Between `total = 0` and `return total`:

1. `for name in header:`
2. `    if name == "__metadata__":`
3. `        continue`
4. `    size = 1`
5. `    for number in header[name]["shape"]:`
6. `        size = size * number`
7. `    total = total + size`

It should print 68,160 parameters: 64,000 + 4,096 + 64.

## Review

<details><summary>Why does a model "forget" the start of a long chat?</summary>The earliest messages no longer fit in the context window and are dropped from the input, so the model never sees them.</details>
<details><summary>What is a chat template?</summary>The exact format with special tokens that turns a conversation into one string, as the model was trained on.</details>
<details><summary>How many numbers does a tensor with shape [3, 4, 5] hold?</summary>3 × 4 × 5 = 60.</details>
