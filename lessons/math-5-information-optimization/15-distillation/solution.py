import math


def soft_targets(z, T):
    zz = [v / T for v in z]
    m = max(zz)
    es = [math.exp(v - m) for v in zz]
    s = sum(es)
    return [e / s for e in es]


def distill_loss(zt, zs, T):
    p, q = soft_targets(zt, T), soft_targets(zs, T)
    return T * T * sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


print(soft_targets([4, 1, 0], 1), soft_targets([4, 1, 0], 4), distill_loss([4, 1, 0], [2, 1, 1], 4))
