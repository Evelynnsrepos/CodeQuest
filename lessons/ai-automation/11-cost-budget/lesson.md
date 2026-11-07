---
title: A cost budget
minutes: 30
xp: 30
hint: call_cost, line 1: tokens = math.ceil(len(prompt) / 4)
hint: call_cost, line 2: return tokens / 1000000 * price_in + reply_tokens / 1000000 * price_out
hint: how_many_fit: spent = 0 and count = 0, then for prompt in prompts: and inside it cost = call_cost(prompt, reply_tokens, price_in, price_out)
hint: Still in the loop: if spent + cost > budget: break. Then spent = spent + cost and count = count + 1. After the loop: return count
---
# Know the price before the bill

⏱️ About 30 minutes · two small functions

> **Warm-up:** a cloud model costs "$3 per million input tokens". Your script sends 500 emails of about 2,000 characters. Is that 5 cents or 50 dollars?

**In one sentence:** estimate tokens from characters, turn tokens into money, and stop the run when the budget is used up.

## 🪜 Step 1: characters to tokens

A **token** is a piece of a word. For English text, one token is about **4 characters** on average (a rule of thumb, German and code use more tokens). So:

`tokens ≈ characters ÷ 4`

The `≈` means "about equal". 2,000 characters ÷ 4 = **500 tokens**. Round **up** (lesson 1's `math.ceil`), because a part of a token is still a whole token on the bill.

## 🪜 Step 2: tokens to money

Prices are given **per million tokens** (1,000,000; in Python you write `1000000`, without the commas). Input (your prompt) and output (the reply) have different prices. To get the cost of one call, find what share of a million you used, then multiply by the price:

`cost = input tokens ÷ 1,000,000 × input price + output tokens ÷ 1,000,000 × output price`

Example: 500 input tokens at $3, and a 100-token reply at $15:

- input: 500 ÷ 1,000,000 = 0.0005, × 3 = **$0.0015**
- output: 100 ÷ 1,000,000 = 0.0001, × 15 = **$0.0015**
- one email: 0.0015 + 0.0015 = **$0.003**
- 500 emails: 500 × 0.003 = **$1.50**

So neither 5 cents nor 50 dollars. That's why you estimate instead of guessing. A local model costs $0 in money, but the same counting tells you how long a run takes.

## 🪜 Step 3: stop at the budget

Add up the cost before each call. If the next call would go **over** the budget, stop and don't make it.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len(prompt)` | "length of prompt" | how many characters the text has: `len("abcde")` is `5` |
| `math.ceil(5 / 4)` | "ceiling of 5 divided by 4" | 5 ÷ 4 = 1.25, rounded **up**: `2` |
| `1000000` | "one million" | a million. Python numbers can't have commas in them. |
| `a / 1000000 * 3` | "a divided by a million, times 3" | Python does `/` and `*` from left to right, like you'd read it |
| `for prompt in prompts:` | "for each prompt in prompts" | goes through the list in order |
| `if spent + cost > budget:` | "if spent plus cost is more than the budget" | `>` means "is bigger than" |
| `break` | "break" | **stops the whole loop** right now (unlike `continue`, which only skips one item) |
| `spent = spent + cost` | "spent becomes spent plus cost" | a running total |

### 👀 Worked example 1: one call

`call_cost("x" * 2000, 100, 3, 15)`. `"x" * 2000` is a text of 2,000 x's.

1. `tokens = math.ceil(len(prompt) / 4)` = ceil(2000 / 4) = **500**.
2. `tokens / 1000000 * price_in` = 500 / 1000000 × 3 = 0.0005 × 3 = **0.0015**.
3. `reply_tokens / 1000000 * price_out` = 100 / 1000000 × 15 = 0.0001 × 15 = **0.0015**.
4. Return 0.0015 + 0.0015 = **0.003** dollars.

### 👀 Worked example 2: a budget loop with other things

How many coffees can you buy with €10, in order, without going over?

```python
def coffees(prices, money):
    spent = 0
    count = 0
    for price in prices:
        if spent + price > money:
            break
        spent = spent + price
        count = count + 1
    return count

print(coffees([3, 4, 5, 1], 10))
```

1. Price 3: 0 + 3 = 3, not more than 10. `spent` = 3, `count` = 1.
2. Price 4: 3 + 4 = 7, fine. `spent` = 7, `count` = 2.
3. Price 5: 7 + 5 = 12, more than 10 → `break`. The loop stops. (The cheap 1 at the end is never looked at: we stop at the first one that doesn't fit, like a real run would.)
4. Returns **2**.

`how_many_fit` is the same loop, with `call_cost(...)` as the price.

## 🎯 Your quest

**Part 1:** `call_cost(prompt, reply_tokens, price_in, price_out)`. Replace `return 0` with:

1. `tokens = math.ceil(len(prompt) / 4)`
2. `return tokens / 1000000 * price_in + reply_tokens / 1000000 * price_out`

**Part 2:** `how_many_fit(prompts, reply_tokens, price_in, price_out, budget)`. Replace `return len(prompts)` with:

1. `spent = 0`
2. `count = 0`
3. `for prompt in prompts:`
4. `    cost = call_cost(prompt, reply_tokens, price_in, price_out)`
5. `    if spent + cost > budget:`
6. `        break`
7. `    spent = spent + cost`
8. `    count = count + 1`
9. `return count`

**Remember:** characters ÷ 4, ÷ a million, × the price, stop before the budget.

## Review

<details><summary>Lesson 10: what is the default for dry_run, and why?</summary>True, so forgetting the setting does nothing instead of changing things.</details>
<details><summary>What is the difference between break and continue?</summary>break stops the whole loop. continue only skips the rest of this round and goes on with the next item.</details>
