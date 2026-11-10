import math


def matmul(A, B):
    C = []
    for row in A:
        new_row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(row)):
                total = total + row[k] * B[k][j]
            new_row.append(total)
        C.append(new_row)
    return C


def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


def softmax(xs):
    m = max(xs)
    e = []
    for x in xs:
        e.append(math.exp(x - m))
    s = sum(e)
    out = []
    for x in e:
        out.append(x / s)
    return out


def causal_attention(X, Wq, Wk, Wv):
    Q, K, V = matmul(X, Wq), matmul(X, Wk), matmul(X, Wv)
    out = []
    # H = len(Q[0])
    # for t in range(len(X)):
    #     scores = []
    #     for s in range(t + 1):
    #         scores.append(dot(Q[t], K[s]) / math.sqrt(H))
    #     weights = softmax(scores)
    #     vec = []
    #     for h in range(len(V[0])):
    #         total = 0
    #         for s in range(t + 1):
    #             total = total + weights[s] * V[s][h]
    #         vec.append(total)
    #     out.append(vec)
    # return out
    return out


# 4 tokens, each a vector of size 3; head size 2
X = [[1.0, 0.0, 1.0], [0.0, 2.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 3.0]]
Wq = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
Wk = [[0.5, 0.0], [0.0, 0.5], [1.0, 0.0]]
Wv = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]
for t, vec in enumerate(causal_attention(X, Wq, Wk, Wv)):
    print(f"position {t}: {[round(x, 3) for x in vec]}")
