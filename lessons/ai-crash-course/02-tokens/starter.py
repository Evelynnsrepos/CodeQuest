import math


def estimate_tokens(text):
    # Count the characters with len(text), divide by 4, round up with math.ceil
    return 0


def cost(input_tokens, output_tokens, in_price, out_price):
    # Step 1: input_dollars = input_tokens * in_price / 1_000_000
    # Step 2: output_dollars = output_tokens * out_price / 1_000_000
    # Step 3: return input_dollars + output_dollars
    return 0.0


print(estimate_tokens("unbelievable"), cost(20_000, 1_000, 3, 15))
