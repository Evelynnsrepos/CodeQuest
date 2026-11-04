import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def forward(w, b, x, y):
    return (0, 0, 0)


def backward(w, b, x, y):
    return (0, 0)


print(forward(0.5, 0, 2, 1), backward(0.5, 0, 2, 1))
