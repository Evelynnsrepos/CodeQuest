---
title: Tokens and what they cost
xp: 20
hint: estimate_tokens has one line: return math.ceil(len(text) / 4)
hint: cost, step 1: input_dollars = input_tokens * in_price / 1_000_000
hint: cost, last line: return input_dollars + output_dollars
---
# Models read pieces, not letters

⏱️ About 20 minutes · two one-line functions

> **Warm-up:** how many words is "unbelievable"? How many pieces would you cut it into?

**In one sentence:** LLMs read text in chunks called **tokens**, and length, speed and price are all counted in tokens.

## 💡 The idea

LLMs don't see letters or whole words. They see **tokens**: common chunks of text. "unbelievable" might be `un` + `believ` + `able` = 3 tokens.

A rough rule for English: **1 token ≈ 4 characters** (a character is one letter, digit, space or punctuation mark). German and code need more tokens for the same amount of text.

Tokens matter because everything is counted in them:

- the **context window**: how much the model can read at once, e.g. 128,000 tokens;
- the **price** of online models, quoted **per million tokens**, with input (what you send) usually cheaper than output (what it writes);
- the **speed**: tokens per second.

**Go deeper:** LLMs 1, lessons 1–3 (you build a real tokenizer), LLMs 9 lesson 02 (context budgets).

## 🔢 The maths, one step at a time

### Estimating tokens

1. Count the characters. "unbelievable" has 12.
2. Divide by 4: 12 ÷ 4 = **3** tokens.
3. If it doesn't divide evenly, **round up**: "hello" has 5 characters, 5 ÷ 4 = 1.25. You can't have a quarter token, and part of a token still costs a whole one, so 1.25 becomes **2**.

"Round up" means: go to the next whole number above, unless it's already whole. 1.25 → 2, 1.9 → 2, 3.0 → 3.

### Price per million

"$3 per million tokens" means 1,000,000 tokens cost $3. For a different number of tokens:

1. tokens × price = what it would cost if the price were per token.
2. ÷ 1,000,000 = the real cost, because the price is for a million at once.

Example: 20,000 input tokens at $3 per million, plus 1,000 output tokens at $15 per million.

| Step | Input | Output |
|---|---|---|
| tokens × price | 20,000 × 3 = 60,000 | 1,000 × 15 = 15,000 |
| ÷ 1,000,000 | 0.06 dollars | 0.015 dollars |
| add both | 0.06 + 0.015 = **0.075 dollars** (7.5 cents) | |

<div class="quiz" data-answer="1" data-why="400 ÷ 4 characters per token = 100 tokens."><p><b>Predict first:</b> about how many tokens is a 400-character English paragraph?</p><button>40</button><button>100</button><button>400</button></div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len("hello")` | "length of hello" | counts the characters: `5` |
| `5 / 4` | "5 divided by 4" | `1.25`. `/` always gives a decimal number. |
| `import math` | "import math" | the first line of the file (already there). Loads Python's maths toolbox. |
| `math.ceil(1.25)` | "ceiling of 1.25" | rounds **up**: `2`. ("Ceiling", because you go up to the ceiling.) |
| `1_000_000` | "one million" | Python lets you write `_` inside numbers so you can read them. It's the same as `1000000`. |
| `( )` | brackets | do this part first, like in school maths |

You can put a function call inside another one. Python works from the inside out:

```python
math.ceil(len("hello") / 4)
# 1. len("hello")  → 5
# 2. 5 / 4         → 1.25
# 3. math.ceil(1.25) → 2
```

### 👀 Worked example: cost of a pizza order

You can store in-between results in boxes (variables) and add them at the end. That's easier to read than one long line:

```python
def pizza_cost(pizzas, drinks, pizza_price, drink_price):
    pizza_money = pizzas * pizza_price
    drink_money = drinks * drink_price
    return pizza_money + drink_money
```

`pizza_cost(2, 3, 9, 2)`: pizzas 2 × 9 = 18, drinks 3 × 2 = 6, total 18 + 6 = 24. Your `cost` is the same shape, with one extra `/ 1_000_000` on each part.

## 🎯 Your quest

1. `estimate_tokens(text)`: replace `return 0` with `return math.ceil(len(text) / 4)`. (Read it inside out: characters, ÷ 4, round up.)
2. `cost(input_tokens, output_tokens, in_price, out_price)`, three lines like `pizza_cost`:
   - `input_dollars = input_tokens * in_price / 1_000_000`
   - `output_dollars = output_tokens * out_price / 1_000_000`
   - `return input_dollars + output_dollars`

`cost(20_000, 1_000, 3, 15)` should give `0.075`, like the table above.

**Remember:** about 4 characters per token; prices are per million.
