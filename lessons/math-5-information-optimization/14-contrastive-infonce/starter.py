import math


def info_nce(sims, pos, tau):
    return 0


def clip_loss(S, tau):
    return 0


print(info_nce([0.9, 0.1, 0.2], 0, 1.0), info_nce([0.9, 0.1, 0.2], 0, 0.1), clip_loss([[0.9, 0.1], [0.2, 0.8]], 0.1))
