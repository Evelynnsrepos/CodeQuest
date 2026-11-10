def matmul(A, B):
    C = []
    for row in A:
        new_row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(row)):
                total = total + row[k] * B[k][j]
            new_row.append(total)
        C.append(new_row)
    return C


def matvec(M, x):
    out = []
    for row in M:
        total = 0
        for k in range(len(row)):
            total = total + row[k] * x[k]
        out.append(total)
    return out


def lora_params(d_in, d_out, r):
    # return r * (d_in + d_out)
    return 0


def lora_forward(W, A, B, x, alpha, r):
    # base = matvec(W, x)
    # delta = matvec(B, matvec(A, x))
    # scale = alpha / r
    # out = []
    # for i in range(len(base)):
    #     out.append(base[i] + scale * delta[i])
    # return out
    return []


def merge(W, A, B, alpha, r):
    # BA = matmul(B, A)
    # scale = alpha / r
    # merged = []
    # for i in range(len(W)):
    #     row = []
    #     for j in range(len(W[0])):
    #         row.append(W[i][j] + scale * BA[i][j])
    #     merged.append(row)
    # return merged
    return W


W = [[1.0, 0.0, 2.0], [0.0, 1.0, -1.0]]     # frozen: 3 inputs → 2 outputs
A = [[0.5, -0.5, 1.0]]                      # r × d_in = 1 × 3
B = [[2.0], [-1.0]]                         # d_out × r = 2 × 1
x = [1.0, 2.0, 3.0]
print("base output:   ", matvec(W, x))
print("with LoRA:     ", lora_forward(W, A, B, x, alpha=2, r=1))
print("merged output: ", matvec(merge(W, A, B, 2, 1), x))
print(f"one 4096×4096 matrix at r=16: {lora_params(4096, 4096, 16):,} trainable vs {4096 * 4096:,}")
