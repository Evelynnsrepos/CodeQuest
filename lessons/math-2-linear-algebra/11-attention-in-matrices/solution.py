import math


def matmul(A, B):
    cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols] for row in A]


def transpose(A):
    return [list(c) for c in zip(*A)]


def softmax(z):
    m = max(z)
    e = [math.exp(v - m) for v in z]
    return [v / sum(e) for v in e]


def causal_mask(T):
    return [[0.0 if j <= i else float("-inf") for j in range(T)] for i in range(T)]


def attention(Q, K, V, causal):
    d = len(Q[0])
    S = [[s / math.sqrt(d) for s in row] for row in matmul(Q, transpose(K))]
    if causal:
        M = causal_mask(len(Q))
        S = [[s + m for s, m in zip(srow, mrow)] for srow, mrow in zip(S, M)]
    A = [softmax(row) for row in S]
    return matmul(A, V)


Q = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
K = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
V = [[10.0, 0.0], [0.0, 10.0], [5.0, 5.0]]
print(causal_mask(3))
for row in attention(Q, K, V, True):
    print([round(v, 2) for v in row])
