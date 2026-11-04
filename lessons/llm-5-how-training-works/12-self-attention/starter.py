import math


def matmul(A, B):
    cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def softmax(xs):
    m = max(xs)
    e = [math.exp(x - m) for x in xs]
    s = sum(e)
    return [v / s for v in e]


def causal_attention(X, Wq, Wk, Wv):
    Q, K, V = matmul(X, Wq), matmul(X, Wk), matmul(X, Wv)
    out = []
    return out


# 4 tokens, each a vector of size 3; head size 2
X = [[1.0, 0.0, 1.0], [0.0, 2.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 3.0]]
Wq = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
Wk = [[0.5, 0.0], [0.0, 0.5], [1.0, 0.0]]
Wv = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]
for t, vec in enumerate(causal_attention(X, Wq, Wk, Wv)):
    print(f"position {t}: {[round(x, 3) for x in vec]}")
