import math


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def kl_via_entropy(p, q):
    cross = -sum(pi * math.log(qi) for pi, qi in zip(p, q) if pi > 0)
    ent = -sum(pi * math.log(pi) for pi in p if pi > 0)
    return cross - ent


print(kl([0.5, 0.5], [0.9, 0.1]), kl([0.9, 0.1], [0.5, 0.5]), kl_via_entropy([0.5, 0.5], [0.9, 0.1]))
