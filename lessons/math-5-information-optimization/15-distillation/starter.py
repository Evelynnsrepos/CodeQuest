import math


def soft_targets(z, T):
    return z


def distill_loss(zt, zs, T):
    return 0


print(soft_targets([4, 1, 0], 1), soft_targets([4, 1, 0], 4), distill_loss([4, 1, 0], [2, 1, 1], 4))
