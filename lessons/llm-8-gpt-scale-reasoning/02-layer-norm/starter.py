import math


def layer_norm(x, gamma, beta, eps=1e-5):
    return x


def rms_norm(x, gamma, eps=1e-5):
    return x


x = [2.0, 4.0, 6.0, 8.0]
print("layer_norm:", [round(v, 3) for v in layer_norm(x, [1.0] * 4, [0.0] * 4)])
print("rms_norm:  ", [round(v, 3) for v in rms_norm(x, [1.0] * 4)])
