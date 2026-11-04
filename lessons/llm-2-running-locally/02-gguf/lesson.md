---
title: GGUF, the format LM Studio runs
xp: 25
---
# GGUF

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

## Your quest

Write `read_gguf_header(data)`. Return a dictionary with the keys `"version"`, `"tensor_count"` and `"metadata_kv_count"`.

- If the first 4 bytes aren't `b"GGUF"`, raise an error: `raise ValueError("not a GGUF file")`. (Never trust a file's name; check its contents.)
- Read each integer with `int.from_bytes(data[start:end], "little")`.

## Review

<details><summary>What does a safetensors file contain, in order?</summary>8 bytes with the header length, a JSON header listing each tensor's dtype, shape and offsets, then the raw tensor data.</details>
<details><summary>Why did safetensors replace pickle files?</summary>Loading a pickle can execute arbitrary code; safetensors is pure data.</details>
<details><summary>What is top-p sampling?</summary>Keep the smallest set of most-likely tokens whose probabilities add up to at least p, renormalize, then sample.</details>
