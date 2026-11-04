import math


def softmax(z):
    return z


def cross_entropy(z, t):
    return 0.0


print([round(p, 3) for p in softmax([2.0, 1.0, 0.1])])
print(round(cross_entropy([2.0, 1.0, 0.1], 0), 3), round(cross_entropy([2.0, 1.0, 0.1], 2), 3))
