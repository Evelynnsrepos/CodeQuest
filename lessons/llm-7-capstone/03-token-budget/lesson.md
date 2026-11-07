---
title: Token budget and max_seq_length
minutes: 40
xp: 40
hint: estimate_tokens: characters = len(example["prompt"]) + len(example["answer"]), return math.ceil(characters / 4) + 20
hint: choose_max_len: find the longest estimate with a best-so-far loop, then size = 256 and while size < longest: size = size * 2
hint: too_long: result = [], for ex in examples: if estimate_tokens(ex) > max_len: result.append(ex), return result
---
# How long are your examples?

⏱️ About 40 minutes

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

## 🔬 Take the formulas apart

<div class="formula">tokens ≈ <span class="k1">⌈characters ÷ 4⌉</span> + <span class="k2">20</span></div>
- English text averages about <span class="k1">4 characters per token</span>. ⌈ ⌉ rounds up.
- <span class="k2">20</span> extra for the chat template's special tokens around two messages.

"Hi" + "Hey!" = 2 + 4 = 6 characters → ⌈6 ÷ 4⌉ = ⌈1.5⌉ = 2 → 2 + 20 = **22** tokens.

**Powers of two** are 1, 2, 4, 8, … each double the last: 256, 512, 1024, 2048. The smallest one ≥ 306 is **512** (256 is too small).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len(example["prompt"])` | | number of characters |
| `math.ceil(x / 4)` | | round up |
| `while size < longest:` | "while size is less than longest" | repeats the indented line **as long as** the condition is true |
| `size = size * 2` | | double it |

### 👀 Worked example: the while loop

```python
size = 256
while size < 1000:
    size = size * 2
print(size)     # 1024
```

1. 256 < 1000 → 512.
2. 512 < 1000 → 1024.
3. 1024 < 1000? No → the loop stops.

## 🎯 Your quest

`estimate_tokens(example)`: replace `return 0` with:

1. `    characters = len(example["prompt"]) + len(example["answer"])`
2. `    return math.ceil(characters / 4) + 20`

`choose_max_len(examples)`: replace `return 256` with:

1. `    longest = 0`
2. `    for ex in examples:`
3. `        tokens = estimate_tokens(ex)`
4. `        if tokens > longest:`
5. `            longest = tokens`
6. `    size = 256`
7. `    while size < longest:`
8. `        size = size * 2`
9. `    return size`

`too_long(examples, max_len)`: replace `return []` with:

1. `    result = []`
2. `    for ex in examples:`
3. `        if estimate_tokens(ex) > max_len:`
4. `            result.append(ex)`
5. `    return result`

It prints 72, 306 and 22 tokens, `max_seq_length: 512`, and the RoPE example as too long for 256.

## Review

<details><summary>Why shuffle with a fixed seed before splitting?</summary>So the split is random but reproducible: the same seed gives the same train/val/test sets every time.</details>
<details><summary>Why deduplicate across the split?</summary>A test example that also appears in training makes the evaluation measure memorization.</details>
