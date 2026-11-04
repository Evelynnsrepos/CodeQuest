import math


def route(scores, k):
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    m = max(scores[i] for i in top)
    es = [math.exp(scores[i] - m) for i in top]
    s = sum(es)
    return [(i, e / s) for i, e in zip(top, es)]


def moe_output(scores, k, expert_outputs):
    out = [0.0] * len(expert_outputs[0])
    for i, g in route(scores, k):
        out = [o + g * v for o, v in zip(out, expert_outputs[i])]
    return out


def balance_loss(f, P, alpha=1.0):
    return alpha * len(f) * sum(fi * pi for fi, pi in zip(f, P))


print(route([2, 1, 0.5, -1], 2), balance_loss([0.5, 0.3, 0.1, 0.1], [0.4, 0.3, 0.2, 0.1]))
