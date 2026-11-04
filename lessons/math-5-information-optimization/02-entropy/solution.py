import math


def entropy(ps, base=2):
    return -sum(p * math.log(p, base) for p in ps if p > 0)


def max_entropy(n, base=2):
    return math.log(n, base)


print(entropy([0.5, 0.5]), entropy([0.9, 0.1]), entropy([1, 0]), max_entropy(6))
