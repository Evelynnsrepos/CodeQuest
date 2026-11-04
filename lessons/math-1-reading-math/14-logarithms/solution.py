import math


def log_base(x, b):
    return math.log(x) / math.log(b)


def bits_needed(n):
    return math.ceil(log_base(n, 2))


def log_prob(ps):
    return sum(math.log(p) for p in ps)


print(log_base(8, 2), log_base(1_000_000, 10), bits_needed(128000))
print(log_prob([0.1, 0.05, 0.2]), math.log(0.001))
