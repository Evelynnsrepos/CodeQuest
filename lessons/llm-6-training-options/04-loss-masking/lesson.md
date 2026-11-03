---
title: Chat templates and training only on answers
xp: 40
---
# What the model actually learns from

> **Warm-up:** a training example has a long user question and a short answer. If the loss counts every token, what is the model mostly being trained to do?

To predict *user questions*, which isn't what you want. During SFT, each example is rendered with the model's **chat template** (LLMs 1, lesson 10) into one token sequence, and the usual next-token cross-entropy is computed at each position. But the loss is **masked** so only the **assistant's tokens** count:

```
tokens:  <|im_start|>user\nExplain LoRA<|im_end|>\n<|im_start|>assistant\nLoRA trains ...<|im_end|>
labels:  -100  -100  -100 ...           -100        -100 ...               LoRA trains ...<|im_end|>
```

`-100` is PyTorch's convention for "ignore this position" in cross-entropy. TRL calls this `assistant_only_loss` / "completion only" training; Unsloth calls it `train_on_responses_only`. Settings have moved between versions, so check the docs of the version you install.

Details that bite people:

- **Use the base model's own template.** Fine-tuning Qwen with a Llama template teaches it a new format from scratch and wastes your data.
- **Train on the end token too** (`<|im_end|>`). If the model never learns to emit it, your fine-tune will never stop talking.
- **Sequence length.** Examples longer than `max_seq_length` get cut, which can chop off the answer. Check your longest example's token count.
- **Packing** puts several short examples into one sequence for speed; it needs care so examples don't attend to each other.

## Your quest

An example is given as a list of `(role, tokens)` segments, already rendered.

1. `build_labels(segments)`: return `(input_ids, labels)`: `input_ids` is all tokens concatenated; `labels` is the same tokens for `"assistant"` segments and `-100` for every other token.
2. `trained_fraction(labels)`: the share of positions that are **not** `-100`.

## Review

<details><summary>What is JSONL?</summary>One complete JSON object per line, nothing else.</details>
<details><summary>Name three qualities of a good fine-tuning dataset.</summary>For example: clean and consistent, covers the real variety of requests, deduplicated, with a held-out split.</details>
