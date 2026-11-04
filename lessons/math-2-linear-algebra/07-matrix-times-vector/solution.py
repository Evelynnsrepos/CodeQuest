def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matvec(A, x):
    if len(A[0]) != len(x):
        raise ValueError("columns of A must equal the length of x")
    return [dot(row, x) for row in A]


def rotate90(v):
    return matvec([[0, -1], [1, 0]], v)


print(matvec([[1, 2], [3, 4]], [5, 6]), rotate90([1, 0]), rotate90([0, 1]))
