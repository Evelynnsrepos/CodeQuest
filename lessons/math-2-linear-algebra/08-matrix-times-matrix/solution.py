def can_multiply(shape_a, shape_b):
    return shape_a[1] == shape_b[0]


def matmul(A, B):
    if not can_multiply((len(A), len(A[0])), (len(B), len(B[0]))):
        raise ValueError("inner sizes must match")
    cols = [[row[j] for row in B] for j in range(len(B[0]))]
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def matmul_flops(m, n, p):
    return 2 * m * n * p


print(can_multiply((32, 4096), (4096, 1024)), can_multiply((2, 3), (2, 3)))
print(matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(f"{matmul_flops(32, 4096, 1024):,} FLOPs")
