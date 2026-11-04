import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def d_square_of_linear(a, b, x):
    return 2 * (a * x + b) * a


def d_sigmoid_of_linear(w, b, x):
    s = sigmoid(w * x + b)
    return s * (1 - s) * w


def chain(slopes):
    out = 1
    for s in slopes:
        out *= s
    return out


print(d_square_of_linear(3, 1, 2), d_sigmoid_of_linear(2, 0, 0), chain([14, 3]))
