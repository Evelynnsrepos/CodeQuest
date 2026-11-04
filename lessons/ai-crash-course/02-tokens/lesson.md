---
title: Tokens and what they cost
xp: 20
---
# Models read pieces, not letters

> **Warm-up:** how many words is "unbelievable"? How many pieces would you cut it into?

LLMs don't see letters or whole words. They see **tokens**: common chunks of text. "unbelievable" might be `un` + `believ` + `able`. A rough rule for English: **1 token ≈ 4 characters ≈ ¾ of a word**. German and code use more tokens per word.

Tokens matter because everything is counted in them:

- the **context window** (how much the model can read at once, e.g. 128,000 tokens);
- the **price** of API models, quoted per **million** tokens, often with input cheaper than output;
- the **speed** (tokens per second).

**Go deeper:** LLMs 1, lessons 1–3 (you build a real tokenizer), LLMs 9 lesson 02 (context budgets and caching).

## Your quest

1. `estimate_tokens(text)`: `len(text) / 4`, rounded **up** to a whole number (`math.ceil`).
2. `cost(input_tokens, output_tokens, in_price, out_price)`: dollars, where prices are per million tokens.

**Remember:** about 4 characters per token; prices per million.
