def shape(A):
    return (len(A), len(A[0]))


def entry(A, i, j):
    return A[i - 1][j - 1]


def column(A, j):
    return [row[j - 1] for row in A]


A = [[1, 2, 3], [4, 5, 6]]
print(shape(A), entry(A, 1, 2), entry(A, 2, 3), column(A, 3))
