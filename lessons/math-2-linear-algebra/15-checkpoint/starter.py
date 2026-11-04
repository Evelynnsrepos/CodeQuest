def matmul(A, B):
    cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def transpose(A):
    return [list(c) for c in zip(*A)]


def mlp_batch(X, W1, b1, W2, b2):
    return X


def mlp_flops(batch, d_in, d_hidden, d_out):
    return 0


def shapes(batch, d_in, d_hidden, d_out):
    return ()


X = [[1, 0, 2], [0, 1, -1]]
W1 = [[1, 1, 0], [0, -1, 1], [2, 0, 0]]
b1 = [0, 0, -1]
W2 = [[1, 0, 1], [0, 1, -1]]
b2 = [0.5, 0]
print(mlp_batch(X, W1, b1, W2, b2))
print(mlp_flops(32, 4096, 14336, 4096), shapes(4, 3, 5, 2))
