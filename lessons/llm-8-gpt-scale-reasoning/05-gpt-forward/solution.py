import math
import random


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matvec(W, x):
    return [dot(row, x) for row in W]


def softmax(xs):
    m = max(xs)
    e = [math.exp(v - m) for v in xs]
    s = sum(e)
    return [v / s for v in e]


def rms_norm(x, eps=1e-5):
    rms = math.sqrt(sum(v * v for v in x) / len(x) + eps)
    return [v / rms for v in x]


def gelu(x):
    return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))


def rope(x, pos, base=10000):
    out = []
    for i in range(len(x) // 2):
        a = pos * base ** (-2 * i / len(x))
        out += [x[2 * i] * math.cos(a) - x[2 * i + 1] * math.sin(a), x[2 * i] * math.sin(a) + x[2 * i + 1] * math.cos(a)]
    return out


def causal_attention(Q, K, V):
    out = []
    for i, q in enumerate(Q):
        w = softmax([dot(q, K[j]) / math.sqrt(len(q)) for j in range(i + 1)])
        out.append([sum(w[j] * V[j][c] for j in range(i + 1)) for c in range(len(V[0]))])
    return out


def random_params(vocab, d, layers, seed=0):
    rng = random.Random(seed)
    m = lambda rows, cols: [[rng.gauss(0, 0.5) for _ in range(cols)] for _ in range(rows)]
    return {"wte": m(vocab, d),
            "layers": [{"Wq": m(d, d), "Wk": m(d, d), "Wv": m(d, d), "Wo": m(d, d), "W1": m(4 * d, d), "W2": m(d, 4 * d)}
                       for _ in range(layers)]}


def gpt_forward(tokens, P):
    x = [list(P["wte"][t]) for t in tokens]
    for L in P["layers"]:
        h = [rms_norm(r) for r in x]
        Q = [rope(matvec(L["Wq"], r), i) for i, r in enumerate(h)]
        K = [rope(matvec(L["Wk"], r), i) for i, r in enumerate(h)]
        V = [matvec(L["Wv"], r) for r in h]
        a = causal_attention(Q, K, V)
        x = [[u + v for u, v in zip(xi, matvec(L["Wo"], ai))] for xi, ai in zip(x, a)]
        x = [[u + v for u, v in zip(xi, matvec(L["W2"], [gelu(z) for z in matvec(L["W1"], rms_norm(xi))]))] for xi in x]
    last = rms_norm(x[-1])
    return softmax([dot(row, last) for row in P["wte"]])


P = random_params(vocab=6, d=4, layers=2)
probs = gpt_forward([0, 3, 5], P)
print("next-token probabilities:", [round(p, 3) for p in probs])
