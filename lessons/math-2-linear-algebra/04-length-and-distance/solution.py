import math


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def normalize(v):
    n = norm(v)
    if n == 0:
        raise ValueError("the zero vector has no direction")
    return [x / n for x in v]


def distance(a, b):
    return norm([x - y for x, y in zip(a, b)])


def clip(g, max_norm):
    n = norm(g)
    if n > max_norm:
        return [x * max_norm / n for x in g]
    return g


print(norm([3, 4]), normalize([3, 4]), distance([1, 1], [4, 5]), clip([30, 40], 1.0))
