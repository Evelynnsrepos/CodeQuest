def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def project(a, b):
    k = dot(a, b) / dot(b, b)
    return [k * x for x in b]


def reject(a, b):
    return [x - p for x, p in zip(a, project(a, b))]


def remove_direction(vectors, d):
    return [reject(v, d) for v in vectors]


print(project([3, 4], [2, 0]), reject([3, 4], [2, 0]))
