import math


def estimate_tokens(text):
    return math.ceil(len(text) / 4)


def cost(input_tokens, output_tokens, in_price, out_price):
    return (input_tokens * in_price + output_tokens * out_price) / 1_000_000


print(estimate_tokens("unbelievable"), cost(20_000, 1_000, 3, 15))
