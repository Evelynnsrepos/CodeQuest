import math


def matvec(M, v):
    return [sum(m * x for m, x in zip(row, v)) for row in M]


def power_iteration(C, steps=100):
    return [1.0] * len(C), 0.0


def explained(C):
    return 0.0


def pca_1d(rows):
    return []


print(power_iteration([[2, 1], [1, 2]]), explained([[2, 1], [1, 2]]))
print([round(x, 2) for x in pca_1d([[1, 1], [2, 2.1], [3, 2.9], [4, 4.2]])])
