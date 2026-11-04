import math


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(c, a):
    return [c * x for x in a]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def rms_norm(a):
    rms = math.sqrt(dot(a, a) / len(a))
    return [x / rms for x in a]


print(add([1, 2], [3, 4]))
print(scale(2, [1, -1]))
print(dot([1, 2, 3], [4, 5, 6]))
print(norm([3, 4]))
print([round(x, 3) for x in rms_norm([3, 4])])
