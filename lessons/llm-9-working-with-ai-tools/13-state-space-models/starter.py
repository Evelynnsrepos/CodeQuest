import math


def ssm_scan(xs, a, b, c):
    # h = 0.0
    # ys = []
    # for x in xs:
    #     h = a * h + b * x
    #     ys.append(c * h)
    # return ys
    return []


def kv_numbers(tokens, kv_heads, d_head):
    # return 2 * kv_heads * d_head * tokens
    return 0


def break_even_tokens(d_inner, d_state, kv_heads, d_head):
    # return math.ceil(d_inner * d_state / (2 * kv_heads * d_head))
    return 0


print(ssm_scan([1, 0, 0, 1], 0.5, 1, 2), kv_numbers(32768, 8, 128), break_even_tokens(8192, 16, 8, 128))
