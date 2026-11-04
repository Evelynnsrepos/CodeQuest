import math


def call_cost(prompt, reply_tokens, price_in, price_out):
    tokens = math.ceil(len(prompt) / 4)
    return tokens / 1e6 * price_in + reply_tokens / 1e6 * price_out


def how_many_fit(prompts, reply_tokens, price_in, price_out, budget):
    spent, count = 0, 0
    for prompt in prompts:
        cost = call_cost(prompt, reply_tokens, price_in, price_out)
        if spent + cost > budget:
            break
        spent += cost
        count += 1
    return count


email = "x" * 2000
print(call_cost(email, 100, 3, 15))
print(how_many_fit([email] * 500, 100, 3, 15, budget=1.0))
