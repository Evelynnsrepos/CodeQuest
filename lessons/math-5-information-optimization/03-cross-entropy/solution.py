import math


def cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q) if pi > 0)


def ce_loss(q, target):
    return -math.log(q[target])


def batch_loss(qs, targets):
    return sum(ce_loss(q, t) for q, t in zip(qs, targets)) / len(qs)


print(cross_entropy([1, 0, 0], [0.7, 0.2, 0.1]), ce_loss([0.7, 0.2, 0.1], 0), batch_loss([[0.7, 0.3], [0.1, 0.9]], [0, 1]))
