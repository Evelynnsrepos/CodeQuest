def det2(A):
    (a, b), (c, d) = A
    return a * d - b * c


def inverse2(A):
    det = det2(A)
    if det == 0:
        raise ValueError("singular matrix: no inverse")
    (a, b), (c, d) = A
    return [[d / det, -b / det], [-c / det, a / det]]


def solve2(A, b):
    inv = inverse2(A)
    return [inv[0][0] * b[0] + inv[0][1] * b[1], inv[1][0] * b[0] + inv[1][1] * b[1]]


A = [[2, 1], [1, 3]]
print(det2(A), inverse2(A), solve2(A, [5, 10]))
