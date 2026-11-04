def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def relu_layer(W, b, x):
    return x


def hadamard(a, b):
    return 0


def layer_params(d_in, d_out):
    return 0


print(relu_layer([[1, -1], [2, 0]], [0, -4], [3, 5]))
print(hadamard([1, 2, 3], [4, 5, 6]), f"{layer_params(4096, 14336):,}")
