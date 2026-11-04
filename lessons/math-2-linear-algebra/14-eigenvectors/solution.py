import math


def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(dot(v, v))


def is_eigenvector(A, v):
    Av = matvec(A, v)
    lam = dot(v, Av) / dot(v, v)
    return all(abs(a - lam * b) < 1e-9 for a, b in zip(Av, v))


def power_iteration(A, steps):
    v = [1.0] * len(A)
    for _ in range(steps):
        Av = matvec(A, v)
        n = norm(Av)
        v = [x / n for x in Av]
    return (dot(v, matvec(A, v)), v)


A = [[2, 1], [1, 2]]
print(is_eigenvector(A, [1, 1]), is_eigenvector(A, [1, -1]), is_eigenvector(A, [1, 0]))
lam, v = power_iteration([[3, 1], [0, 1]], 50)
print(round(lam, 4), [round(x, 4) for x in v])
