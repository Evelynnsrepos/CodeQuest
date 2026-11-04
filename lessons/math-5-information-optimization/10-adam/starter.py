import math


def adam_step(theta, g, m, v, t, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    return theta, m, v


print(adam_step([1.0, 1.0], [0.5, 500.0], [0.0, 0.0], [0.0, 0.0], 1))
