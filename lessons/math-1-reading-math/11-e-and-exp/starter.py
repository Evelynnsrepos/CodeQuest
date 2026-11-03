import math


def compound(n):
    return 0.0


def sigmoid(z):
    return 0.0


def decay(start, k, t):
    return start


for n in [1, 2, 12, 365, 1_000_000]:
    print(n, round(compound(n), 6))
print(sigmoid(0), round(sigmoid(5), 4), round(decay(1e-3, 0.1, 10), 6))
