def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def relu_layer(W, b, x):
    return [max(0, v + bi) for v, bi in zip(matvec(W, x), b)]


def hadamard(a, b):
    return [x * y for x, y in zip(a, b)]


def layer_params(d_in, d_out):
    return d_in * d_out + d_out


print(relu_layer([[1, -1], [2, 0]], [0, -4], [3, 5]))
print(hadamard([1, 2, 3], [4, 5, 6]), f"{layer_params(4096, 14336):,}")
