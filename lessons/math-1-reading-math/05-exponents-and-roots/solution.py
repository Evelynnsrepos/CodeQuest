import math


def levels(bits):
    return 2 ** bits


def power_rules_hold(x, a, b):
    first = abs(x ** a * x ** b - x ** (a + b)) < 1e-9
    second = abs((x ** a) ** b - x ** (a * b)) < 1e-9
    return first and second


def rms(xs):
    return math.sqrt(sum(x ** 2 for x in xs) / len(xs))


print(levels(4), levels(8), power_rules_hold(2, 3, 2), rms([3, 4]))
