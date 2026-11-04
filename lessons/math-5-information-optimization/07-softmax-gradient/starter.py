import math


def softmax(z):
    m = max(z)
    es = [math.exp(v - m) for v in z]
    s = sum(es)
    return [e / s for e in es]


def ce_from_logits(z, target):
    return 0


def ce_grad(z, target):
    return [0] * len(z)


print(ce_from_logits([2, 1, 0], 0), ce_grad([2, 1, 0], 0))
