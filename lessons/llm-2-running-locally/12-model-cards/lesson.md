---
title: Reading a model card and config.json
xp: 40
---
# Know a model before you download it

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

## Python you need

`config.get("head_dim", default)` returns the default when the key is missing. `a // b` divides and drops the remainder.

## Your quest

1. `head_dim(config)`: `config["head_dim"]` if present, else hidden size ÷ attention heads (whole number).
2. `estimate_params(config)`: the total from the formulas above.
3. `kv_bytes_per_token(config)`: 2 × layers × kv heads × head_dim × 2 bytes (16-bit cache).

The check compares your estimates against Llama 3.1 8B and Qwen3-8B.

## Review

<details><summary>What does an SSE stream end with?</summary>The line data: [DONE], which is not JSON.</details>
<details><summary>What is a delta in a streamed chunk?</summary>Only the new piece of text since the previous chunk.</details>
