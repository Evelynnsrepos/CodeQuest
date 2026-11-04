import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def forward(w, b, x, y):
    z = w * x + b
    a = sigmoid(z)
    return (z, a, (a - y) ** 2)


def backward(w, b, x, y):
    z, a, L = forward(w, b, x, y)
    shared = 2 * (a - y) * a * (1 - a)
    return (shared * x, shared)


print(forward(0.5, 0, 2, 1), backward(0.5, 0, 2, 1))
