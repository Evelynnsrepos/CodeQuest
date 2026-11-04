import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def d_sigmoid(x):
    s = sigmoid(x)
    return s * (1 - s)


def d_ln(x):
    return 1 / x


def d_exp(x):
    return math.exp(x)


print(sigmoid(0), d_sigmoid(0), d_sigmoid(4), d_ln(4), d_exp(1))
