import math


def info_nce(sims, pos, tau):
    z = [s / tau for s in sims]
    m = max(z)
    lse = m + math.log(sum(math.exp(v - m) for v in z))
    return lse - z[pos]


def clip_loss(S, tau):
    n = len(S)
    rows = sum(info_nce(S[i], i, tau) for i in range(n))
    cols = sum(info_nce([S[i][j] for i in range(n)], j, tau) for j in range(n))
    return (rows + cols) / (2 * n)


print(info_nce([0.9, 0.1, 0.2], 0, 1.0), info_nce([0.9, 0.1, 0.2], 0, 0.1), clip_loss([[0.9, 0.1], [0.2, 0.8]], 0.1))
