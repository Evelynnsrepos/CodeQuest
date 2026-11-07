import math


def layer_norm(x, gamma, beta, eps=1e-5):
    # d = len(x)
    # mean = sum(x) / d
    # var = 0
    # for v in x:
    #     var = var + (v - mean) ** 2
    # var = var / d
    # out = []
    # for i in range(d):
    #     out.append((x[i] - mean) / math.sqrt(var + eps) * gamma[i] + beta[i])
    # return out
    return x


def rms_norm(x, gamma, eps=1e-5):
    # total = 0
    # for v in x:
    #     total = total + v * v
    # rms = math.sqrt(total / len(x) + eps)
    # out = []
    # for i in range(len(x)):
    #     out.append(x[i] / rms * gamma[i])
    # return out
    return x


x = [2.0, 4.0, 6.0, 8.0]
print("layer_norm:", [round(v, 3) for v in layer_norm(x, [1.0] * 4, [0.0] * 4)])
print("rms_norm:  ", [round(v, 3) for v in rms_norm(x, [1.0] * 4)])
