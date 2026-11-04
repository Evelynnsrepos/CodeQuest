---
title: A reply is a loop
xp: 25
---
# Autoregressive generation

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

## Your quest

`MODEL` is a toy language model: for each last token it gives the probabilities of the next token. (A real model looks at *all* previous tokens, not just the last one; this "bigram" shortcut keeps the table small.)

Write `generate(prompt, max_tokens)`. Start from a copy of the prompt list, then repeat up to `max_tokens` times:

1. Look up the distribution for the last token: `MODEL[tokens[-1]]`.
2. Pick the token with the highest probability: `max(dist, key=dist.get)`.
3. If it is `"<eos>"`, stop. Otherwise append it.

Return the token list.

Expected output:

```
['Once', ' upon', ' a', ' time', ' there', ' was', ' a', ' time']
['Once', ' upon', ' a']
['The', ' end', '.']
```

## Review

<details><summary>What is perplexity, in one sentence?</summary>e to the power of the average negative log-prob: how many equally likely choices the model was effectively picking between.</details>
<details><summary>Why work with log-probabilities instead of probabilities?</summary>Multiplying many small probabilities underflows to 0. Logs turn the product into a sum, which stays in a safe range.</details>
