---
title: Token budget and max_seq_length
xp: 40
---
# How long are your examples?

> **Warm-up:** what happens to an example that's longer than `max_seq_length`? Which part gets lost?

It's cut from the end, which is where the **answer** is. A too-small `max_seq_length` silently trains on half-answers and teaches the model to stop mid-sentence. A too-large one wastes memory on padding and activations (which grow with sequence length, LLMs 5 lesson 13).

So measure. With the model's real tokenizer you'd count exactly:

```python
tok = AutoTokenizer.from_pretrained("Qwen/Qwen3-4B")
n = len(tok.apply_chat_template(example["messages"], tokenize=True))
```

Without it, a rough rule for English is **about 4 characters per token** (German a bit fewer characters per token, code different again). Add the chat template's overhead: special tokens and role names cost roughly 10 tokens per message.

Then:

- look at the **longest** examples (fix or drop extreme outliers by hand),
- choose `max_seq_length` at or above the longest example you keep, rounded up to a power of two (512, 1024, 2048…), which kernels handle efficiently,
- compute **total training tokens** for the time and cost estimate (LLMs 6, lesson 11).

## Your quest

1. `estimate_tokens(example)`: for `{"prompt", "answer"}`, `ceil(characters of prompt and answer ÷ 4)` plus `20` for the template (two messages).
2. `choose_max_len(examples)`: the smallest power of two that is ≥ the largest estimate, but at least 256.
3. `too_long(examples, max_len)`: the list of examples whose estimate is above `max_len`.

## Review

<details><summary>Why shuffle with a fixed seed before splitting?</summary>So the split is random but reproducible: the same seed gives the same train/val/test sets every time.</details>
<details><summary>Why deduplicate across the split?</summary>A test example that also appears in training makes the evaluation measure memorization.</details>
