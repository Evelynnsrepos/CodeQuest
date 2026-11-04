---
title: Why tokens are word pieces
xp: 15
---
# Subword tokens

> **Warm-up:** why not just give every word its own token? And why not use single letters?

Both extremes fail:

| Choice | Problem |
|---|---|
| One token per **word** | Millions of words, names, typos and code identifiers. The vocabulary explodes, and any word it never saw is unknown. |
| One token per **letter** | Every text becomes very long. The model must spend effort rebuilding words from letters, and each extra token costs compute and context space. |

Real tokenizers sit in between: **subwords**. Frequent strings (`" the"`, `" function"`) get one token. Rare strings get split into smaller known pieces, and in the worst case into single bytes, so **no text is ever "unknown"**.

That has consequences you will notice in practice:

- Languages that were rare in the tokenizer's training text get split into more pieces. German usually costs more tokens per word than English, so the same context window holds less German text.
- Models are bad at counting letters ("how many r's in strawberry?") because they never see the letters, only chunks like `"str" + "aw" + "berry"`.
- Numbers are often split oddly (`"2025"` might be `"202" + "5"`), which is one reason plain LLMs make arithmetic mistakes.

Real tokenizers are built with **BPE** (next lesson). Here we use a simpler **greedy longest-match** tokenizer: at each position, take the longest vocabulary entry that matches.

## Your quest

`tokenize(text)` is written for you. Don't change it.

1. Finish `tokens_per_word(text)`: return the number of tokens divided by the number of words. `text.split()` gives you the list of words, and `len(...)` counts a list.
2. Set `german_costs_more` to `True` or `False` based on what your program prints.

Look closely at how `Die` at the very start gets split. The vocabulary only knows `" Die"` *with* a space, so the first word falls apart into letters. Real tokenizers have the same quirk: the first word of a text often tokenizes differently from the same word in the middle.

## Review

<details><summary>What does the model actually receive when you send a message?</summary>A list of token IDs: integer positions in the model's vocabulary. Never letters or words.</details>
<details><summary>Are "how" and " how" the same token?</summary>No. The leading space is part of the token, so they have different IDs.</details>
