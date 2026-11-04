def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matvec(A, x):
    return x


def rotate90(v):
    return v


print(matvec([[1, 2], [3, 4]], [5, 6]), rotate90([1, 0]), rotate90([0, 1]))
