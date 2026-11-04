import math


def softmax(z):
    m = max(z)
    es = [math.exp(v - m) for v in z]
    s = sum(es)
    return [e / s for e in es]


def ce_from_logits(z, target):
    return -math.log(softmax(z)[target])


def ce_grad(z, target):
    p = softmax(z)
    return [pi - (1 if i == target else 0) for i, pi in enumerate(p)]


print(ce_from_logits([2, 1, 0], 0), ce_grad([2, 1, 0], 0))
