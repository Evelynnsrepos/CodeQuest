import math


def kl(p, q):
    return 0


def kl_via_entropy(p, q):
    return 0


print(kl([0.5, 0.5], [0.9, 0.1]), kl([0.9, 0.1], [0.5, 0.5]), kl_via_entropy([0.5, 0.5], [0.9, 0.1]))
