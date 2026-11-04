import math


def weights(scores):
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    return [e / sum(exps) for e in exps]


def attend(scores, values):
    w = weights(scores)
    return [sum(wi * v[d] for wi, v in zip(w, values)) for d in range(len(values[0]))]


print([round(w, 2) for w in weights([0.0, 2.6, 0.0, 1.4])])
print([round(x, 2) for x in attend([0.0, 2.6, 0.0, 1.4], [[1, 0], [0, 1], [1, 1], [0.5, 0]])])
