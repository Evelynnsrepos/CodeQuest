import math


def proportion_ci(wins, n):
    p = wins / n
    e = 1.96 * math.sqrt(p * (1 - p) / n)
    return (p - e, p + e)


def sample_std(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def mean_ci(xs):
    m = sum(xs) / len(xs)
    e = 1.96 * sample_std(xs) / math.sqrt(len(xs))
    return (m - e, m + e)


print(proportion_ci(60, 100), sample_std([70, 72, 68, 75, 65]), mean_ci([70, 72, 68, 75, 65]))
