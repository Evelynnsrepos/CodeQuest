---
title: Chat templates and training only on answers
minutes: 30
xp: 40
hint: build_labels: for role, tokens in segments: input_ids = input_ids + tokens
hint: Still in the loop: if role == "assistant": labels = labels + tokens, else: labels = labels + [-100] * len(tokens)
hint: trained_fraction: count = 0, for x in labels: if x != -100: count = count + 1. Then return count / len(labels)
---
# What the model actually learns from

⏱️ About 30 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for role, tokens in segments:` | | each segment is a pair like `("user", [1, 21, 2])` |
| `input_ids + tokens` | | `+` on lists glues them end to end |
| `[-100] * 3` | | `[-100, -100, -100]`: a list repeated |
| `len(tokens)` | | how many tokens that segment has |
| `x != -100` | "x is not minus 100" | true for the trained positions |

### 👀 Worked example: two short segments

segments = `[("user", [5, 6, 7]), ("assistant", [8, 9])]`:

1. User: input_ids = [5, 6, 7], labels = [-100, -100, -100].
2. Assistant: input_ids = [5, 6, 7, 8, 9], labels = [-100, -100, -100, 8, 9].
3. Trained: 2 positions out of 5 → **0.4** (40%).

## 🎯 Your quest

**Part 1:** `build_labels(segments)`. Between the first line and `return input_ids, labels`, add:

1. `    for role, tokens in segments:`
2. `        input_ids = input_ids + tokens`
3. `        if role == "assistant":`
4. `            labels = labels + tokens`
5. `        else:`
6. `            labels = labels + [-100] * len(tokens)`

**Part 2:** `trained_fraction(labels)`. Replace `return 0` with:

1. `    count = 0`
2. `    for x in labels:`
3. `        if x != -100:`
4. `            count = count + 1`
5. `    return count / len(labels)`

The example has 17 tokens and 5 of them are the assistant's, so it prints `29% of positions are trained`.

## Review

<details><summary>What is JSONL?</summary>One complete JSON object per line, nothing else.</details>
<details><summary>Name three qualities of a good fine-tuning dataset.</summary>For example: clean and consistent, covers the real variety of requests, deduplicated, with a held-out split.</details>
