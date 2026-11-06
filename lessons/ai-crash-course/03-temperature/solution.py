import math


def softmax_t(scores, t):
    scaled = []
    for s in scores:
        scaled.append(s / t)
    biggest = max(scaled)
    exps = []
    for s in scaled:
        exps.append(math.exp(s - biggest))
    total = sum(exps)
    probs = []
    for e in exps:
        probs.append(e / total)
    return probs


# These lines just show your result rounded to 2 decimals. You don't need to change them.
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 1)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 0.2)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 5)])
