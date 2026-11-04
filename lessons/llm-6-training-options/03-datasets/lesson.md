---
title: Dataset formats: JSONL and chat messages
xp: 40
---
# What a fine-tuning dataset looks like

> **Warm-up:** to teach a model your writing style, what would one training example look like? What goes in, and what should come out?

A supervised fine-tuning (**SFT**) dataset is a list of example conversations. It's almost always stored as **JSONL** ("JSON Lines"): one complete JSON object **per line**, nothing else. That makes huge files easy to stream, split and append to.

Two shapes you'll meet:

**Instruction format** (from Stanford's Alpaca dataset): flat fields.

```json
{"instruction": "Summarize the text.", "input": "LoRA freezes the base model and ...", "output": "LoRA trains small matrices ..."}
```

**Chat / messages format**: the same `messages` list you send to LM Studio. This is what modern tools (TRL, Unsloth, Axolotl) prefer, because the tool can apply the model's own chat template.

```json
{"messages": [{"role": "system", "content": "You write like Evelynn."},
              {"role": "user", "content": "Explain the KV cache."},
              {"role": "assistant", "content": "ok so basically ..."}]}
```

(You'll also see **ShareGPT** format, `{"conversations": [{"from": "human", "value": ...}]}`, which tools can convert.)

What makes a dataset good matters far more than its size:

- **Quality over quantity.** 300 clean, consistent examples beat 30,000 sloppy ones. Read every example; your model will copy mistakes faithfully.
- **Consistency.** If half your answers start with "Sure!" and half don't, the model learns a coin flip.
- **Coverage.** Include the variety of requests it will really see, including short ones and edge cases.
- **Hold out** 10% (or at least 20 prompts) for validation and evaluation before you start (LLMs 5, lesson 8).
- **Deduplicate**, and keep private data out unless the model will stay private.

## Python you need

`json.dumps(obj)` gives one line of JSON (no `indent`!). `"\n".join(lines)` joins lines. Inside a loop, `continue` skips ahead.

## Your quest

1. `alpaca_to_chat(record, system=None)`: return `{"messages": [...]}` with an optional system message, a user message (the instruction, plus `"\n\n"` and the input if the input isn't empty) and an assistant message (the output).
2. `to_jsonl(records)`: one `json.dumps` line per record, joined with newlines.
3. `validate_line(line)`: return `None` if the line is a valid chat example, else a short error text. Valid means: it parses as JSON, has a `"messages"` list with at least 2 entries, every role is `"system"`, `"user"` or `"assistant"`, every content is a non-empty string, and the **last** message is from the assistant.

## Review

<details><summary>Rule of thumb: RAG or fine-tuning?</summary>RAG for knowledge, fine-tuning for behaviour (style, format, narrow skills).</details>
<details><summary>Why is fine-tuning a poor way to add facts?</summary>The model learns style faster than content, can't cite sources, hallucinates half-remembered facts and needs retraining for every update.</details>
