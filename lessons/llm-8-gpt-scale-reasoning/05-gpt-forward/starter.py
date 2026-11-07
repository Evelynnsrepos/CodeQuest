import math
import random


def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total


def matvec(W, x):
    """W is a list of rows; returns W·x."""
    out = []
    for row in W:
        total = 0
        for i in range(len(x)):
            total = total + row[i] * x[i]
        out.append(total)
    return out


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
    return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))


def rope(x, pos, base=10000):
    d = len(x)
    out = []
    for i in range(d // 2):
        a = pos * base ** (-2 * i / d)
        x0 = x[2 * i]
        x1 = x[2 * i + 1]
        out.append(x0 * math.cos(a) - x1 * math.sin(a))
        out.append(x0 * math.sin(a) + x1 * math.cos(a))
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


def random_params(vocab, d, layers, seed=0):
    rng = random.Random(seed)

    def m(rows, cols):
        grid = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(rng.gauss(0, 0.5))
            grid.append(row)
        return grid

    wte = m(vocab, d)
    all_layers = []
    for n in range(layers):
        all_layers.append({"Wq": m(d, d), "Wk": m(d, d), "Wv": m(d, d), "Wo": m(d, d), "W1": m(4 * d, d), "W2": m(d, 4 * d)})
    return {"wte": wte, "layers": all_layers}


def gpt_forward(tokens, P):
    # x = []
    # for t in tokens:
    #     x.append(list(P["wte"][t]))
    # for L in P["layers"]:
    #     Q = []
    #     K = []
    #     V = []
    #     for i in range(len(x)):
    #         h = rms_norm(x[i])
    #         Q.append(rope(matvec(L["Wq"], h), i))
    #         K.append(rope(matvec(L["Wk"], h), i))
    #         V.append(matvec(L["Wv"], h))
    #     a = causal_attention(Q, K, V)
    #     for i in range(len(x)):
    #         o = matvec(L["Wo"], a[i])
    #         for c in range(len(x[i])):
    #             x[i][c] = x[i][c] + o[c]
    #     for i in range(len(x)):
    #         hidden = matvec(L["W1"], rms_norm(x[i]))
    #         g = []
    #         for z in hidden:
    #             g.append(gelu(z))
    #         m = matvec(L["W2"], g)
    #         for c in range(len(x[i])):
    #             x[i][c] = x[i][c] + m[c]
    # last = rms_norm(x[-1])
    # logits = []
    # for row in P["wte"]:
    #     logits.append(dot(row, last))
    # return softmax(logits)
    return []


P = random_params(vocab=6, d=4, layers=2)
probs = gpt_forward([0, 3, 5], P)
print("next-token probabilities:", [round(p, 3) for p in probs])
