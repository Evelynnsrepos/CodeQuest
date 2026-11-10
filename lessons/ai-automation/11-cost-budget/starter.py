import math


def call_cost(prompt, reply_tokens, price_in, price_out):
    # tokens = math.ceil(len(prompt) / 4)
    # return tokens / 1000000 * price_in + reply_tokens / 1000000 * price_out
    return 0


def how_many_fit(prompts, reply_tokens, price_in, price_out, budget):
    # spent = 0
    # count = 0
    # for prompt in prompts:
    #     cost = call_cost(prompt, reply_tokens, price_in, price_out)
    #     if spent + cost > budget:
    #         break
    #     spent = spent + cost
    #     count = count + 1
    # return count
    return len(prompts)


email = "x" * 2000
print(call_cost(email, 100, 3, 15))
print(how_many_fit([email] * 500, 100, 3, 15, budget=1.0))
