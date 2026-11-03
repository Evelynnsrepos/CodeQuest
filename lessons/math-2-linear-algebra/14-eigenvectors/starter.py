import math


def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(dot(v, v))


def is_eigenvector(A, v):
    return False


def power_iteration(A, steps):
    return (0.0, [])


A = [[2, 1], [1, 2]]
print(is_eigenvector(A, [1, 1]), is_eigenvector(A, [1, -1]), is_eigenvector(A, [1, 0]))
lam, v = power_iteration([[3, 1], [0, 1]], 50)
print(round(lam, 4), [round(x, 4) for x in v])
