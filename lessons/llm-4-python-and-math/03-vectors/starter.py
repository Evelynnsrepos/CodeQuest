import math


def add(a, b):
    # out = []
    # for i in range(len(a)):
    #     out.append(a[i] + b[i])
    # return out
    return []


def scale(c, a):
    # out = []
    # for x in a:
    #     out.append(c * x)
    # return out
    return []


def dot(a, b):
    # total = 0
    # for i in range(len(a)):
    #     total = total + a[i] * b[i]
    # return total
    return 0


def norm(a):
    # return math.sqrt(dot(a, a))
    return 0


def rms_norm(a):
    # rms = math.sqrt(dot(a, a) / len(a))
    # out = []
    # for x in a:
    #     out.append(x / rms)
    # return out
    return []


print(add([1, 2], [3, 4]))
print(scale(2, [1, -1]))
print(dot([1, 2, 3], [4, 5, 6]))
print(norm([3, 4]))
print([round(x, 3) for x in rms_norm([3, 4])])
