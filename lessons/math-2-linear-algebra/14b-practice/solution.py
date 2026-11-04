import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def angle_deg(a, b):
    c = dot(a, b) / (math.sqrt(dot(a, a)) * math.sqrt(dot(b, b)))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def matvec(M, v):
    return [dot(row, v) for row in M]


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def perpendicular(a, b):
    return abs(dot(a, b)) < 1e-9


def layer_params(n_in, n_out):
    return n_out * n_in + n_out


print(angle_deg([1, 0], [1, 1]), matvec([[1, 2], [3, 4]], [1, 1]), distance([1, 2], [4, 6]), perpendicular([2, 1], [-1, 2]), layer_params(768, 3072))
