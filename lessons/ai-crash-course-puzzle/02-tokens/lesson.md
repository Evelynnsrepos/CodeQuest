---
title: Tokens, the pieces an LLM reads
minutes: 20
xp: 20
hint: estimate_tokens: the block with math.ceil (rounds up) and / 4
hint: input_dollars uses input_tokens and in_price; output_dollars uses output_tokens and out_price. Both divide by 1_000_000.
distractor: return math.floor(len(text) / 4)
distractor: input_dollars = input_tokens * out_price / 1_000_000
distractor: return input_dollars * output_dollars
---
# Tokens

⏱️ About 20 minutes · 🧩 4 gaps, 3 decoys

> **Warm-up:** how would you cut the word "unbelievable" into smaller pieces?

**In one sentence:** an LLM doesn't read letters or whole words, it reads **tokens**: chunks of text about 4 letters long, and you pay per token.

## 💡 The idea

"unbelievable" might become `un` + `believ` + `able`: 3 tokens. Common words are often one token; rare words get cut into several.

A good rule of thumb for English: **1 token ≈ 4 characters**. (A character is one letter, digit, space or symbol.)

Online AI services charge per **million** tokens, with separate prices for what you send (**input**) and what comes back (**output**). On your own computer tokens are free, but they still decide how fast it runs and how much text fits.

## 🔢 The maths, step by step

**Estimate tokens** for `"hello world"`:

1. Count the characters: h-e-l-l-o, space, w-o-r-l-d = **11**.
2. Divide by 4: 11 ÷ 4 = **2.75**.
3. Round **up**: you can't have 0.75 of a token, a started token is still a token → **3**.

**Cost** of 20,000 input tokens at $3 per million and 1,000 output tokens at $15 per million:

1. Input: 20,000 × 3 = 60,000. Then ÷ 1,000,000 = **$0.06**.
2. Output: 1,000 × 15 = 15,000. Then ÷ 1,000,000 = **$0.015**.
3. Add them: 0.06 + 0.015 = **$0.075**.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `import math` | "import math" | unlocks maths helpers (already written for you at the top) |
| `len(text)` | "length of text" | how many characters: `len("hello")` is `5` |
| `/` | "divided by" | `11 / 4` gives `2.75` |
| `math.ceil(2.75)` | "ceiling of 2.75" | rounds **up**: `3` |
| `math.floor(2.75)` | "floor of 2.75" | rounds **down**: `2` (that's a decoy!) |
| `1_000_000` | "one million" | the `_` are just for easy reading, like commas |
| `a + b` | "a plus b" | adds numbers |

## 👀 Worked example: price of apples

```python
def apple_cost(apples, price_per_dozen):
    return apples * price_per_dozen / 12
```

30 apples at 6 per dozen: 30 × 6 = 180, ÷ 12 = **15**. Your `cost` does the same twice (once for input, once for output, each "per million") and then adds.

## 🧩 Your puzzle

1. `estimate_tokens`: length ÷ 4, rounded **up**.
2. `input_dollars`: input tokens × the **input** price ÷ one million. (Decoy: the same line with `out_price`.)
3. `output_dollars`: output tokens × the **output** price ÷ one million.
4. Give back the two **added** (decoy: multiplied).

Run it: you should see `3 0.075`.

**Remember:** about 4 characters per token, prices are per million.
