def matmul(A, B):
    cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def matvec(M, x):
    return [sum(m * xi for m, xi in zip(row, x)) for row in M]


def lora_params(d_in, d_out, r):
    return 0


def lora_forward(W, A, B, x, alpha, r):
    return []


def merge(W, A, B, alpha, r):
    return W


W = [[1.0, 0.0, 2.0], [0.0, 1.0, -1.0]]     # frozen: 3 inputs → 2 outputs
A = [[0.5, -0.5, 1.0]]                      # r × d_in = 1 × 3
B = [[2.0], [-1.0]]                         # d_out × r = 2 × 1
x = [1.0, 2.0, 3.0]
print("base output:   ", matvec(W, x))
print("with LoRA:     ", lora_forward(W, A, B, x, alpha=2, r=1))
print("merged output: ", matvec(merge(W, A, B, 2, 1), x))
print(f"one 4096×4096 matrix at r=16: {lora_params(4096, 4096, 16):,} trainable vs {4096 * 4096:,}")
