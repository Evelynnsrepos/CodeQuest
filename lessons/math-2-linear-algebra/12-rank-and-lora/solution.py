def matmul(A, B):
    cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def outer(u, v):
    return [[ui * vj for vj in v] for ui in u]


def lora_params(d, k, r):
    return d * r + r * k


def lora_weight(W0, B, A, alpha, r):
    BA = matmul(B, A)
    return [[w + alpha / r * x for w, x in zip(wrow, brow)] for wrow, brow in zip(W0, BA)]


print(outer([1, 2], [3, 0, 1]))
print(f"{lora_params(4096, 4096, 16):,} vs {4096 * 4096:,}")
print(lora_weight([[1, 0], [0, 1]], [[1], [2]], [[0.5, 0.5]], 16, 8))
