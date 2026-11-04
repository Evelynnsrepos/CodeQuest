def add(v, w):
    return [a + b for a, b in zip(v, w)]


def scale(c, v):
    return [c * a for a in v]


def lin_comb(coeffs, vectors):
    total = [0] * len(vectors[0])
    for c, v in zip(coeffs, vectors):
        total = add(total, scale(c, v))
    return total


print(add([3, 1], [1, 2]), scale(2, [3, 1]), lin_comb([0.5, 2], [[2, 4], [1, -1]]))
