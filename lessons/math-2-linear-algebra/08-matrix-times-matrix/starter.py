def can_multiply(shape_a, shape_b):
    return True


def matmul(A, B):
    return A


def matmul_flops(m, n, p):
    return 0


print(can_multiply((32, 4096), (4096, 1024)), can_multiply((2, 3), (2, 3)))
print(matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(f"{matmul_flops(32, 4096, 1024):,} FLOPs")
