import math


def softmax_t(scores, t):
    scaled = [s / t for s in scores]
    m = max(scaled)
    exps = [math.exp(s - m) for s in scaled]
    total = sum(exps)
    return [e / total for e in exps]


print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 1)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 0.2)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 5)])
