import math


def matvec(M, v):
    return [sum(m * x for m, x in zip(row, v)) for row in M]


def normalize(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


def power_iteration(C, steps=100):
    v = normalize([1.0] * len(C))
    for _ in range(steps):
        v = normalize(matvec(C, v))
    lam = sum(a * b for a, b in zip(v, matvec(C, v)))
    return v, lam


def explained(C):
    return power_iteration(C)[1] / sum(C[i][i] for i in range(len(C)))


def pca_1d(rows):
    n, d = len(rows), len(rows[0])
    means = [sum(r[j] for r in rows) / n for j in range(d)]
    X = [[r[j] - means[j] for j in range(d)] for r in rows]
    C = [[sum(x[i] * x[j] for x in X) / (n - 1) for j in range(d)] for i in range(d)]
    v, _ = power_iteration(C)
    if max(v, key=abs) < 0:
        v = [-x for x in v]
    return [sum(a * b for a, b in zip(x, v)) for x in X]


print(power_iteration([[2, 1], [1, 2]]), explained([[2, 1], [1, 2]]))
print([round(x, 2) for x in pca_1d([[1, 1], [2, 2.1], [3, 2.9], [4, 4.2]])])
