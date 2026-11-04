import math


def second_derivative(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def max_stable_lr(curvature):
    return 2 / curvature


def is_convex(f, xs):
    return all(second_derivative(f, x) >= -1e-6 for x in xs)


L = lambda w: (w - 3) ** 2
print(second_derivative(L, 0), max_stable_lr(2), is_convex(L, [-5, 0, 5]), is_convex(math.sin, [0, 1, 2, 3]))
