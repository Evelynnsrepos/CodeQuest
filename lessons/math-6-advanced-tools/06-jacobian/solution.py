def jacobian(f, x, h=1e-5):
    cols = []
    for j in range(len(x)):
        up = list(x); up[j] += h
        down = list(x); down[j] -= h
        cols.append([(a - b) / (2 * h) for a, b in zip(f(up), f(down))])
    return [list(row) for row in zip(*cols)]


def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def chain_jacobian(f, g, x):
    return matmul(jacobian(g, f(x)), jacobian(f, x))


f = lambda v: [v[0] * v[1], v[0] + v[1] ** 2]
print(jacobian(f, [2.0, 3.0]))
