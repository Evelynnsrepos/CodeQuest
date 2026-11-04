import math


def call_cost(prompt, reply_tokens, price_in, price_out):
    return 0


def how_many_fit(prompts, reply_tokens, price_in, price_out, budget):
    return len(prompts)


email = "x" * 2000
print(call_cost(email, 100, 3, 15))
print(how_many_fit([email] * 500, 100, 3, 15, budget=1.0))
