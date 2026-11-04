def tokens(text):
    return 0


def tokens_left(window, parts, reserve):
    return window


def request_cost(cached, new, price_per_million, cache_factor=0.1):
    return 0


print(tokens("hello world, this is a test"), tokens_left(200000, [3000, 12000, 2000, 150000], 20000), request_cost(160000, 2000, 3))
