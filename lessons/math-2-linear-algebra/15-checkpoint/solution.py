def matmul(A, B):
    cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def transpose(A):
    return [list(c) for c in zip(*A)]


def mlp_batch(X, W1, b1, W2, b2):
    H = [[max(0, v + b) for v, b in zip(row, b1)] for row in matmul(X, transpose(W1))]
    return [[v + b for v, b in zip(row, b2)] for row in matmul(H, transpose(W2))]


def mlp_flops(batch, d_in, d_hidden, d_out):
    return 2 * batch * d_in * d_hidden + 2 * batch * d_hidden * d_out


def shapes(batch, d_in, d_hidden, d_out):
    return ((batch, d_in), (d_hidden, d_in), (batch, d_hidden), (d_out, d_hidden), (batch, d_out))


X = [[1, 0, 2], [0, 1, -1]]
W1 = [[1, 1, 0], [0, -1, 1], [2, 0, 0]]
b1 = [0, 0, -1]
W2 = [[1, 0, 1], [0, 1, -1]]
b2 = [0.5, 0]
print(mlp_batch(X, W1, b1, W2, b2))
print(mlp_flops(32, 4096, 14336, 4096), shapes(4, 3, 5, 2))
