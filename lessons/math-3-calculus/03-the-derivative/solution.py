def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h


def central_diff(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def tangent(f, x):
    m = central_diff(f, x)
    return (m, f(x) - m * x)


sq = lambda x: x * x
print(forward_diff(sq, 3, 0.01), central_diff(sq, 3), tangent(sq, 3))
