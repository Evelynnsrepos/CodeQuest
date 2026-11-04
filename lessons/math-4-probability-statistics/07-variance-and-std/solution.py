import math


def variance(d):
    mu = sum(x * p for x, p in d.items())
    return sum((x - mu) ** 2 * p for x, p in d.items())


def std(d):
    return math.sqrt(variance(d))


def data_std(xs):
    mu = sum(xs) / len(xs)
    return math.sqrt(sum((x - mu) ** 2 for x in xs) / len(xs))


die = {k: 1 / 6 for k in range(1, 7)}
print(variance(die), std(die), data_std([69, 70, 71]), data_std([40, 70, 100]))
