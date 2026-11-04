import math


def variance(d):
    return 0


def std(d):
    return 0


def data_std(xs):
    return 0


die = {k: 1 / 6 for k in range(1, 7)}
print(variance(die), std(die), data_std([69, 70, 71]), data_std([40, 70, 100]))
