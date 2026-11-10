---
title: Reading a model card and config.json
minutes: 45
xp: 40
hint: head_dim: if "head_dim" in config: return config["head_dim"]. Otherwise return config["hidden_size"] // config["num_attention_heads"]
hint: estimate_params: q = h * config["num_attention_heads"] * hd and kv = h * config["num_key_value_heads"] * hd, then attention = q + kv + kv + q
hint: mlp = 3 * h * config["intermediate_size"], total = config["num_hidden_layers"] * (attention + mlp), embeddings = config["vocab_size"] * h
hint: if config["tie_word_embeddings"]: total = total + embeddings, else: total = total + 2 * embeddings
hint: kv_bytes_per_token: return 2 * config["num_hidden_layers"] * config["num_key_value_heads"] * head_dim(config) * 2
---
# Know a model before you download it

⏱️ About 45 minutes

> **Warm-up:** you find a new model on Hugging Face. Which five facts do you want to know before you click download?

**The model card** (`README.md` on the model page) tells you:

- **Base or instruct**, and what it was tuned for (chat, code, reasoning, tool use)
- **License**: Apache 2.0 and MIT are permissive; Llama, Gemma and others have their own terms with conditions. It matters once you publish a fine-tune (your capstone).
- **Context length** it was trained for, and whether longer contexts need special settings
- **Recommended sampling** settings (temperature, top-p, min-p…). Use them.
- **Chat template** and special features: thinking mode, tool calling format
- **Benchmarks**: treat them as marketing. Models are sometimes tuned to the tests. Your own prompts are the real benchmark.

**`config.json`** (under *Files and versions*) gives the hard numbers. For Llama 3.1 8B:

```json
{"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
 "num_key_value_heads": 8, "intermediate_size": 14336, "vocab_size": 128256,
 "max_position_embeddings": 131072, "tie_word_embeddings": false}
```

From these you can compute the parameter count yourself. Every layer has:

```
attention:  Q  hidden × (heads × head_dim)        K, V  hidden × (kv_heads × head_dim) each
            O  (heads × head_dim) × hidden
MLP:        gate, up, down: 3 × hidden × intermediate
```

where `head_dim = hidden_size / num_attention_heads` unless the config lists `head_dim`. On top come the embedding table (`vocab × hidden`) and the output table (another `vocab × hidden`, unless `tie_word_embeddings` is true, then they share one). Norm weights are tiny; ignore them.

For the GGUF version, check the files list of the GGUF repo: it shows each quant's real size, which you can compare with your estimate.

## 🔬 Count Llama 3.1 8B by hand

A weight table of shape `rows × columns` holds rows × columns numbers. Each layer has these tables:

| Table | Shape | Llama 3.1 8B |
|---|---|---|
| head_dim | hidden ÷ heads | 4,096 ÷ 32 = **128** |
| Q (queries) | hidden × (heads × head_dim) | 4,096 × (32 × 128) = 16,777,216 |
| K (keys) | hidden × (kv_heads × head_dim) | 4,096 × (8 × 128) = 4,194,304 |
| V (values) | the same as K | 4,194,304 |
| O (output) | the same size as Q | 16,777,216 |
| **attention** | Q + K + V + O | **41,943,040** |
| **MLP** | 3 × hidden × intermediate | 3 × 4,096 × 14,336 = **176,160,768** |

One layer: 41,943,040 + 176,160,768 = 218,103,808. Times 32 layers = **6,979,321,856**.

The embedding table: vocab × hidden = 128,256 × 4,096 = 525,336,576. `tie_word_embeddings` is false, so there's a separate output table of the same size: 2 × 525,336,576 = 1,050,673,152.

Total: 6,979,321,856 + 1,050,673,152 = **8,029,995,008**, about 8.03 billion. That's the "8B".

`//` (two slashes) divides and **drops the remainder**: 7 // 2 = 3. Used for head_dim, which must be a whole number.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"head_dim" in config` | | `True` if the dictionary has that key |
| `config["hidden_size"]` | | looks up a number from the config |
| `a // b` | "a floor-divided by b" | division without the remainder: a whole number |
| `q + kv + kv + q` | | Q + K + V + O (K and V are the same size, Q and O too) |
| `n * (a + b)` | | the brackets first, then times n |
| `if config["tie_word_embeddings"]:` | | true when the config says `true` |
| `total = total + x` | | adds to the total |

### 👀 Worked example: counting tiles in a house

Every floor has a kitchen and two bathrooms; the house also has a garden, and maybe a garage the same size as the garden.

```python
def tiles(house):
    side = house["width"] // house["rooms"]
    kitchen = side * side
    bath = side * 2
    per_floor = kitchen + bath + bath
    total = house["floors"] * per_floor
    garden = house["width"] * 10
    if house["garage_shared"]:
        total = total + garden
    else:
        total = total + 2 * garden
    return total

print(tiles({"width": 9, "rooms": 2, "floors": 3, "garage_shared": False}))   # 276
```

1. side = 9 // 2 = **4** (not 4.5).
2. kitchen = 16, bath = 8, per floor = 16 + 8 + 8 = 32.
3. 3 floors × 32 = 96.
4. garden = 9 × 10 = 90. Not shared, so add it twice: 96 + 2 × 90 = **276**.

`estimate_params` is built exactly like this.

## 🎯 Your quest

**Part 1:** `head_dim(config)`. Replace `return 0` with:

1. `if "head_dim" in config:`
2. `    return config["head_dim"]`
3. `return config["hidden_size"] // config["num_attention_heads"]`

**Part 2:** `estimate_params(config)`. The first two lines (`h` and `hd`) are there. Make the rest read:

1. `q = h * config["num_attention_heads"] * hd`
2. `kv = h * config["num_key_value_heads"] * hd`
3. `attention = q + kv + kv + q`
4. `mlp = 3 * h * config["intermediate_size"]`
5. `total = config["num_hidden_layers"] * (attention + mlp)`
6. `embeddings = config["vocab_size"] * h`
7. `if config["tie_word_embeddings"]:`
8. `    total = total + embeddings`
9. `else:`
10. `    total = total + 2 * embeddings`
11. `return total`

**Part 3:** `kv_bytes_per_token(config)` (the formula from lesson 5). Replace `return 0` with:

- `return 2 * config["num_hidden_layers"] * config["num_key_value_heads"] * head_dim(config) * 2`

The check compares your estimates against Llama 3.1 8B and Qwen3-8B.

## Review

<details><summary>What does an SSE stream end with?</summary>The line data: [DONE], which is not JSON.</details>
<details><summary>What is a delta in a streamed chunk?</summary>Only the new piece of text since the previous chunk.</details>
