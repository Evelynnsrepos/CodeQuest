---
title: A reply is a loop
minutes: 35
xp: 25
hint: Inside the for loop, first: dist = MODEL[tokens[-1]]
hint: Best-so-far loop: best = None and best_p = -1, then for token in dist: if dist[token] > best_p: best = token and best_p = dist[token]
hint: After the inner loop (still inside the outer one): if best == "<eos>": break
hint: Last line inside the outer loop: tokens.append(best)
---
# Autoregressive generation

⏱️ About 35 minutes

> **Warm-up:** the model only predicts *one* token. So how does LM Studio get a whole paragraph out of it?

With a loop. This is called **autoregressive** generation:

```
tokens = your prompt
repeat:
    probabilities = model(tokens)        # one forward pass
    next = pick a token from probabilities
    if next is the end-of-sequence token: stop
    tokens.append(next)                  # the reply becomes part of the input
```

A 300-token reply is 300 trips through the whole model. A few consequences:

- **Prompt processing vs generation.** LM Studio first reads your whole prompt in one big parallel pass (that's the "time to first token"), then generates one token at a time (the tokens/s number). Long prompts make the first part slower; long answers make the second part slower.
- **The KV cache.** Re-reading every earlier token on every step would be wasteful, so runners keep intermediate results for earlier tokens in memory, the **KV cache**. It grows with every token and is why a long context needs extra VRAM (Module 2).
- **Stopping.** Generation stops when the model outputs a special **end-of-sequence** token (`<eos>`, `<|im_end|>`, `<|eot_id|>`, depending on the model), or when it hits the max-tokens limit you set. A model that "never stops talking" usually has a wrong chat template or stop token.
- **No take-backs.** Each token is final once chosen. A bad early pick can derail the rest, which is part of why models sometimes talk themselves into wrong answers.

Picking the most likely token every time is called **greedy decoding**. It's what you get with temperature 0 (next lessons).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `list(prompt)` | "list of prompt" | a **copy** of the list, so you don't change the caller's prompt |
| `for _ in range(max_tokens):` | "repeat max-tokens times" | `range(5)` runs 5 times. The `_` means "I don't need the counter". |
| `tokens[-1]` | "tokens at minus one" | the **last** item of a list. `-1` counts from the end. |
| `MODEL[" a"]` | | the dictionary of next tokens after `" a"`: `{" time": 0.7, " hill": 0.3}` |
| `for token in dist:` | | goes through the keys: `" time"`, then `" hill"` |
| `dist[token]` | | the probability of that token |
| `>` | "is more than" | |
| `break` | "break" | stops the loop right now |

### 👀 Worked example: the best so far

Finding the biggest value in a dictionary is the "best so far" loop: remember the best one you've seen, and replace it whenever you find a better one.

```python
scores = {"Ana": 7, "Ben": 9, "Cleo": 4}
best = None
best_score = -1
for name in scores:
    if scores[name] > best_score:
        best = name
        best_score = scores[name]
print(best)   # Ben
```

1. Start: `best` = None, `best_score` = −1 (lower than any real score, so the first one always wins).
2. Ana: 7 > −1 → best = Ana, 7.
3. Ben: 9 > 7 → best = Ben, 9.
4. Cleo: 4 > 9? No. Keep Ben.

Probabilities are never below 0, so −1 works as the starting value here too.

## 🎯 Your quest

`MODEL` is a toy language model: for each last token it gives the probabilities of the next token. (A real model looks at *all* previous tokens, not just the last one; this "bigram" shortcut keeps the table small.)

Write `generate(prompt, max_tokens)`. The first line, the loop line and the `return` are there. Replace the `pass` line with these lines (8 spaces in front, 12 and 16 for the deeper ones):

1. `dist = MODEL[tokens[-1]]`
2. `best = None`
3. `best_p = -1`
4. `for token in dist:`
5. `    if dist[token] > best_p:`
6. `        best = token`
7. `        best_p = dist[token]`
8. `if best == "<eos>":`
9. `    break`
10. `tokens.append(best)`

Lines 2 to 7 are worked example's best-so-far loop. Lines 8 and 9 stop the reply at the end token, without adding it.

Expected output:

```
['Once', ' upon', ' a', ' time', ' there', ' was', ' a', ' time']
['Once', ' upon', ' a']
['The', ' end', '.']
```

## Review

<details><summary>What is perplexity, in one sentence?</summary>e to the power of the average negative log-prob: how many equally likely choices the model was effectively picking between.</details>
<details><summary>Why work with log-probabilities instead of probabilities?</summary>Multiplying many small probabilities underflows to 0. Logs turn the product into a sum, which stays in a safe range.</details>
<details><summary>What does tokens[-1] give?</summary>The last item in the list.</details>
