import math


def surprise_bits(p):
    return -math.log2(p)


def surprise_nats(p):
    return -math.log(p)


def joint_surprise(ps):
    return sum(surprise_bits(p) for p in ps)


print(surprise_bits(0.5), surprise_bits(1 / 6), surprise_nats(0.5), joint_surprise([0.5, 0.5]))
