---
title: GGUF, the format LM Studio runs
minutes: 25
xp: 25
hint: First: if data[0:4] != b"GGUF": and under it raise ValueError("not a GGUF file")
hint: Then: result = {} and result["version"] = int.from_bytes(data[4:8], "little")
hint: Same for the other two: data[8:16] is tensor_count, data[16:24] is metadata_kv_count. Then return result
---
# GGUF

⏱️ About 25 minutes

> **Warm-up:** when you download a model in LM Studio, you get *one* file, not a folder. Where did the tokenizer, chat template and config go?

**GGUF** is the file format of **llama.cpp**, the inference engine inside LM Studio (on Linux and Windows), Ollama, Lemonade's llama.cpp backend, and many others. It packs everything into one file:

- **metadata** as key–value pairs: architecture, layer count, context length, the tokenizer's vocabulary and merges, the chat template (`tokenizer.chat_template`), even the quantization type
- the **tensors**, usually **quantized** (stored with fewer bits, next lesson)

The file starts with a fixed header (all integers little-endian):

```
bytes 0–3    magic       the four letters "GGUF"
bytes 4–7    version     uint32 (currently 3)
bytes 8–15   tensor_count       uint64
bytes 16–23  metadata_kv_count  uint64
then the metadata key–value pairs, the tensor descriptions, and the tensor data
```

People convert safetensors to GGUF with llama.cpp's `convert_hf_to_gguf.py`, then shrink it with `llama-quantize`. You will do both yourself in the capstone. Most of the time, though, someone has already done it: Hugging Face accounts like `lmstudio-community`, `bartowski` and `unsloth` publish GGUF versions of new models within hours.

**On your machine:** LM Studio keeps its models in `~/.lmstudio/models/` (on Linux; check *My Models* in the app for the exact path). You can peek at a real header with:

```bash
head -c 24 ~/.lmstudio/models/<publisher>/<model>/<file>.gguf | xxd
```

The first four bytes print as `GGUF`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `b"GGUF"` | "the bytes G G U F" | a **bytes** value. The `b` in front means "raw bytes from a file", not normal text. |
| `data[0:4]` | "data from 0 up to 4" | the first 4 bytes (positions 0, 1, 2, 3) |
| `!=` | "is not equal to" | true when the two sides differ |
| `raise ValueError("...")` | "raise a value error" | stops with your own error message |
| `int.from_bytes(data[4:8], "little")` | | turns the bytes at positions 4 to 7 into one whole number |
| `result["version"] = x` | | puts `x` into the dictionary under the key `"version"` |

The header table above tells you which bytes hold what. "bytes 8–15" means positions 8 up to and **including** 15, which is the slice `data[8:16]` (a slice stops before its end number).

### 👀 Worked example: reading a ticket

A pretend ticket file: 4 bytes `TIX!`, then 2 bytes for the seat, then 4 bytes for the price.

```python
def read_ticket(data):
    if data[0:4] != b"TIX!":
        raise ValueError("not a ticket")
    result = {}
    result["seat"] = int.from_bytes(data[4:6], "little")
    result["price"] = int.from_bytes(data[6:10], "little")
    return result
```

1. Check the first 4 bytes. If they're not `TIX!`, stop with an error.
2. Bytes 4 and 5 → the seat number.
3. Bytes 6 to 9 → the price.
4. Return the dictionary, like `{"seat": 12, "price": 30}`.

## 🎯 Your quest

Write `read_gguf_header(data)`. Replace the comment and `return {}` with:

1. `if data[0:4] != b"GGUF":`
2. `    raise ValueError("not a GGUF file")`
3. `result = {}`
4. `result["version"] = int.from_bytes(data[4:8], "little")`
5. `result["tensor_count"] = int.from_bytes(data[8:16], "little")`
6. `result["metadata_kv_count"] = int.from_bytes(data[16:24], "little")`
7. `return result`

Never trust a file's name; check its contents. That's what lines 1 and 2 do.

## Review

<details><summary>What does a safetensors file contain, in order?</summary>8 bytes with the header length, a JSON header listing each tensor's dtype, shape and offsets, then the raw tensor data.</details>
<details><summary>Why did safetensors replace pickle files?</summary>Loading a pickle can execute arbitrary code; safetensors is pure data.</details>
<details><summary>What is top-p sampling?</summary>Keep the smallest set of most-likely tokens whose probabilities add up to at least p, renormalize, then sample.</details>
<details><summary>Which slice holds "bytes 8 to 15"?</summary>data[8:16]: a slice stops before its end number.</details>
