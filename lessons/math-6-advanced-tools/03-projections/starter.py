def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def project(a, b):
    return a


def reject(a, b):
    return a


def remove_direction(vectors, d):
    return vectors


print(project([3, 4], [2, 0]), reject([3, 4], [2, 0]))
