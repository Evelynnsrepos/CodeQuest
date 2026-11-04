---
title: A cost budget
xp: 30
---
# Know the price before the bill

⏱️ About 12 minutes · two small functions

> **Warm-up:** a cloud model costs "$3 per million input tokens". Your script sends 500 emails of about 2,000 characters. Is that 5 cents or 50 dollars?

**In one sentence:** estimate tokens from characters, turn tokens into money, and stop the run when the budget is used up.

## 🪜 Step 1: characters to tokens

A **token** is a piece of a word. For English text, one token is about **4 characters** on average (a rule of thumb, German and code use more tokens). So:

`tokens ≈ characters ÷ 4`

The `≈` means "about equal". 2,000 characters ÷ 4 = **500 tokens**. Round **up** (lesson 1's `math.ceil`), because a part of a token is still a whole token on the bill.

## 🪜 Step 2: tokens to money

Prices are given **per million tokens** (1,000,000, written `1e6` in Python). Input (your prompt) and output (the reply) have different prices. To get the cost of one call, find what share of a million you used, then multiply by the price:

`cost = input tokens ÷ 1,000,000 × input price + output tokens ÷ 1,000,000 × output price`

Example: 500 input tokens at $3, and a 100-token reply at $15:

- input: 500 ÷ 1,000,000 = 0.0005, × 3 = **$0.0015**
- output: 100 ÷ 1,000,000 = 0.0001, × 15 = **$0.0015**
- one email: 0.0015 + 0.0015 = **$0.003**
- 500 emails: 500 × 0.003 = **$1.50**

So neither 5 cents nor 50 dollars. That's why you estimate instead of guessing. A local model costs $0 in money, but the same counting tells you how long a run takes.

## 🪜 Step 3: stop at the budget

Add up the cost before each call. If the next call would go **over** the budget, stop and don't make it.

## 🎯 Your quest

1. `call_cost(prompt, reply_tokens, price_in, price_out)`: tokens for the prompt with `math.ceil(len(prompt) / 4)`, then the cost formula above. Prices are dollars per million tokens.
2. `how_many_fit(prompts, reply_tokens, price_in, price_out, budget)`: go through the prompts in order, add up `call_cost`, and return how many calls fit **without going over** `budget`.

<details><summary>💡 Hint 1</summary><code>tokens = math.ceil(len(prompt) / 4)</code> then <code>return tokens / 1e6 * price_in + reply_tokens / 1e6 * price_out</code></details>
<details><summary>💡 Hint 2</summary>Keep <code>spent = 0</code> and <code>count = 0</code>. For each prompt: <code>cost = call_cost(...)</code>; if <code>spent + cost > budget</code> stop (<code>break</code>); otherwise add it and count it.</details>

**Remember:** characters ÷ 4, ÷ a million, × the price, stop before the budget.

## Review

<details><summary>Lesson 10: what is the default for dry_run, and why?</summary>True, so forgetting the flag does nothing instead of changing things.</details>
