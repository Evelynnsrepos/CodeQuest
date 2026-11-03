def shape(A):
    return (0, 0)


def entry(A, i, j):
    return A[0][0]


def column(A, j):
    return []


A = [[1, 2, 3], [4, 5, 6]]
print(shape(A), entry(A, 1, 2), entry(A, 2, 3), column(A, 3))
