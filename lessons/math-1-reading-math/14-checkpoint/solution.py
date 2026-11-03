import math


def softmax(z):
    total = sum(math.exp(zj) for zj in z)
    return [math.exp(zi) / total for zi in z]


def cross_entropy(z, t):
    return -math.log(softmax(z)[t])


print([round(p, 3) for p in softmax([2.0, 1.0, 0.1])])
print(round(cross_entropy([2.0, 1.0, 0.1], 0), 3), round(cross_entropy([2.0, 1.0, 0.1], 2), 3))
