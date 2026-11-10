import math


def matvec(W, x):
    """W is a list of rows; returns W·x."""
    out = []
    for row in W:
        total = 0
        for i in range(len(x)):
            total = total + row[i] * x[i]
        out.append(total)
    return out


def rms_norm(x, eps=1e-5):
    total = 0
    for v in x:
        total = total + v * v
    rms = math.sqrt(total / len(x) + eps)
    out = []
    for v in x:
        out.append(v / rms)
    return out


def gelu(x):
    # return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))
    return x


def mlp_block(x, W1, W2):
    # hidden = matvec(W1, rms_norm(x))
    # h = []
    # for v in hidden:
    #     h.append(gelu(v))
    # y = matvec(W2, h)
    # out = []
    # for i in range(len(x)):
    #     out.append(x[i] + y[i])
    # return out
    return x


W1 = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, -1.0]]   # 2 -> 4 (4x wider)
W2 = [[1.0, 0.0, 0.5, 0.0], [0.0, 1.0, 0.0, 0.5]]        # 4 -> 2
print("gelu:", [round(gelu(v), 4) for v in [-2.0, -0.5, 0.0, 0.5, 2.0]])
print("block:", [round(v, 4) for v in mlp_block([1.0, -1.0], W1, W2)])
