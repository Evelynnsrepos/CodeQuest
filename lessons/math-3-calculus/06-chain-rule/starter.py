import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def d_square_of_linear(a, b, x):
    return 0


def d_sigmoid_of_linear(w, b, x):
    return 0


def chain(slopes):
    return 0


print(d_square_of_linear(3, 1, 2), d_sigmoid_of_linear(2, 0, 0), chain([14, 3]))
