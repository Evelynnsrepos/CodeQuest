def tokens(text):
    return len(text) // 4


def tokens_left(window, parts, reserve):
    used = 0
    for part in parts:
        used = used + part
    return window - used - reserve


def request_cost(cached, new, price_per_million, cache_factor=0.1):
    paid_tokens = cached * cache_factor + new
    return paid_tokens * price_per_million / 1_000_000


print(tokens("hello world, this is a test"), tokens_left(200000, [3000, 12000, 2000, 150000], 20000), request_cost(160000, 2000, 3))
