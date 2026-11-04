import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def softmax(xs):
    m = max(xs)
    e = [math.exp(x - m) for x in xs]
    s = sum(e)
    return [x / s for x in e]


def causal_attention(Q, K, V):
    """One head. Q, K, V are lists of rows (one row per position). Position i only sees positions 0..i."""
    out = []
    for i, q in enumerate(Q):
        scores = [dot(q, K[j]) / math.sqrt(len(q)) for j in range(i + 1)]
        w = softmax(scores)
        out.append([sum(w[j] * V[j][c] for j in range(i + 1)) for c in range(len(V[0]))])
    return out


def split_heads(rows, n_heads):
    w = len(rows[0]) // n_heads
    return [[row[h * w:(h + 1) * w] for row in rows] for h in range(n_heads)]


def multi_head(Q, K, V, n_heads):
    heads = [causal_attention(q, k, v) for q, k, v in zip(split_heads(Q, n_heads), split_heads(K, n_heads), split_heads(V, n_heads))]
    return [sum((head[i] for head in heads), []) for i in range(len(Q))]


Q = [[1.0, 0.0, 0.0, 1.0], [0.0, 1.0, 1.0, 0.0], [1.0, 1.0, 0.0, 0.0]]
K = [[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [1.0, 1.0, 1.0, 1.0]]
V = [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]]
print(split_heads(Q, 2))
for row in multi_head(Q, K, V, 2):
    print([round(x, 3) for x in row])
