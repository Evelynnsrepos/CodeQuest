def forward_diff(f, x, h):
    return 0


def central_diff(f, x, h=1e-5):
    return 0


def tangent(f, x):
    return (0, 0)


sq = lambda x: x * x
print(forward_diff(sq, 3, 0.01), central_diff(sq, 3), tangent(sq, 3))
