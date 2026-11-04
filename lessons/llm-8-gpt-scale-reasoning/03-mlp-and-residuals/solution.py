import math


def matvec(W, x):
    """W is a list of rows; returns W·x."""
    return [sum(w * v for w, v in zip(row, x)) for row in W]


def rms_norm(x, eps=1e-5):
    rms = math.sqrt(sum(v * v for v in x) / len(x) + eps)
    return [v / rms for v in x]


def gelu(x):
    return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))


def mlp_block(x, W1, W2):
    h = [gelu(v) for v in matvec(W1, rms_norm(x))]
    return [a + b for a, b in zip(x, matvec(W2, h))]


W1 = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, -1.0]]   # 2 -> 4 (4x wider)
W2 = [[1.0, 0.0, 0.5, 0.0], [0.0, 1.0, 0.0, 0.5]]        # 4 -> 2
print("gelu:", [round(gelu(v), 4) for v in [-2.0, -0.5, 0.0, 0.5, 2.0]])
print("block:", [round(v, 4) for v in mlp_block([1.0, -1.0], W1, W2)])
