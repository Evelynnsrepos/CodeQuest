import math


def layer_norm(x, gamma, beta, eps=1e-5):
    d = len(x)
    mean = sum(x) / d
    var = sum((v - mean) ** 2 for v in x) / d
    return [(v - mean) / math.sqrt(var + eps) * g + b for v, g, b in zip(x, gamma, beta)]


def rms_norm(x, gamma, eps=1e-5):
    rms = math.sqrt(sum(v * v for v in x) / len(x) + eps)
    return [v / rms * g for v, g in zip(x, gamma)]


x = [2.0, 4.0, 6.0, 8.0]
print("layer_norm:", [round(v, 3) for v in layer_norm(x, [1.0] * 4, [0.0] * 4)])
print("rms_norm:  ", [round(v, 3) for v in rms_norm(x, [1.0] * 4)])
