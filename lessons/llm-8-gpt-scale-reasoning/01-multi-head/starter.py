import math


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


def causal_attention(Q, K, V):
    """One head. Q, K, V are lists of rows (one row per position). Position i only sees positions 0..i."""
    out = []
    for i in range(len(Q)):
        scores = []
        for j in range(i + 1):
            scores.append(dot(Q[i], K[j]) / math.sqrt(len(Q[i])))
        w = softmax(scores)
        row = []
        for c in range(len(V[0])):
            total = 0
            for j in range(i + 1):
                total = total + w[j] * V[j][c]
            row.append(total)
        out.append(row)
    return out


def split_heads(rows, n_heads):
    # w = len(rows[0]) // n_heads
    # heads = []
    # for h in range(n_heads):
    #     head = []
    #     for row in rows:
    #         head.append(row[h * w:(h + 1) * w])
    #     heads.append(head)
    # return heads
    return []


def multi_head(Q, K, V, n_heads):
    # Qs = split_heads(Q, n_heads)
    # Ks = split_heads(K, n_heads)
    # Vs = split_heads(V, n_heads)
    # outputs = []
    # for h in range(n_heads):
    #     outputs.append(causal_attention(Qs[h], Ks[h], Vs[h]))
    # result = []
    # for i in range(len(Q)):
    #     row = []
    #     for h in range(n_heads):
    #         row = row + outputs[h][i]
    #     result.append(row)
    # return result
    return []


Q = [[1.0, 0.0, 0.0, 1.0], [0.0, 1.0, 1.0, 0.0], [1.0, 1.0, 0.0, 0.0]]
K = [[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [1.0, 1.0, 1.0, 1.0]]
V = [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]]
print(split_heads(Q, 2))
for row in multi_head(Q, K, V, 2):
    print([round(x, 3) for x in row])
