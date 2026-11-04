def jacobian(f, x, h=1e-5):
    return []


def matmul(A, B):
    return A


def chain_jacobian(f, g, x):
    return []


f = lambda v: [v[0] * v[1], v[0] + v[1] ** 2]
print(jacobian(f, [2.0, 3.0]))
