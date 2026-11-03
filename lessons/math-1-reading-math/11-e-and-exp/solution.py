import math


def compound(n):
    return (1 + 1 / n) ** n


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def decay(start, k, t):
    return start * math.exp(-k * t)


for n in [1, 2, 12, 365, 1_000_000]:
    print(n, round(compound(n), 6))
print(sigmoid(0), round(sigmoid(5), 4), round(decay(1e-3, 0.1, 10), 6))
