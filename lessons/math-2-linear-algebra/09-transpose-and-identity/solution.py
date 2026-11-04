def transpose(A):
    return [list(col) for col in zip(*A)]


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def is_symmetric(A):
    return A == transpose(A)


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(identity(3), is_symmetric([[1, 7], [7, 2]]))
