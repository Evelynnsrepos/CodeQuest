---
title: Why tokens are word pieces
minutes: 15
xp: 15
hint: tokens_per_word has one line: return len(tokenize(text)) / len(text.split())
hint: Press Run and compare the two numbers it prints. Is the German number bigger?
hint: Last line: german_costs_more = True (no quotes)
---
# Subword tokens

⏱️ About 15 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `tokenize(text)` | "tokenize text" | runs the given tokenizer: a list of tokens |
| `text.split()` | "text split" | cuts the text at spaces: `"The cat sat."` → `["The", "cat", "sat."]`, a list of words |
| `len(a_list)` | "length of" | how many items a list has |
| `a / b` | "a divided by b" | division |
| `len(tokenize(text))` | | read it from the inside out: first tokenize, then count the tokens |
| `True`, `False` | "true", "false" | Python's yes and no. No quotes: `"True"` with quotes would be text, not a yes. |

### 👀 Worked example: letters per word

Same shape: count one thing, count words, divide.

```python
def letters_per_word(text):
    return len(text.replace(" ", "")) / len(text.split())

print(letters_per_word("hi you"))   # 2.5
```

1. `text.replace(" ", "")` removes the spaces: `"hiyou"`, 5 letters.
2. `text.split()` is `["hi", "you"]`: 2 words.
3. 5 / 2 = **2.5** letters per word.

## 🎯 Your quest

`tokenize(text)` is written for you. Don't change it.

1. In `tokens_per_word`, replace `return 0  # ...` with:
   - `return len(tokenize(text)) / len(text.split())`
2. Press **Run**. It prints both token lists and both numbers. Which number is bigger?
3. In the last line, replace `None` with `True` if German needs more tokens per word, or `False` if not.

Look closely at how `Die` at the very start gets split. The vocabulary only knows `" Die"` *with* a space, so the first word falls apart into letters. Real tokenizers have the same quirk: the first word of a text often tokenizes differently from the same word in the middle.

## Review

<details><summary>What does the model actually receive when you send a message?</summary>A list of token IDs: integer positions in the model's vocabulary. Never letters or words.</details>
<details><summary>Are "how" and " how" the same token?</summary>No. The leading space is part of the token, so they have different IDs.</details>
