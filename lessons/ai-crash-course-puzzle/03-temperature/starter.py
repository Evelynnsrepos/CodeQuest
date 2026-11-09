import math


def softmax_t(scores, t):
    scaled = []
    for s in scores:
        ___
    biggest = max(scaled)
    exps = []
    for s in scaled:
        ___
    ___
    probs = []
    for e in exps:
        ___
    return probs


# These lines just show your result rounded to 2 decimals. You don't need to change them.
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 1)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 0.2)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 5)])
