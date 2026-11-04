import math

T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306,
       9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
       16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074,
       23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048, 29: 2.045, 30: 2.042}
# 95% t-values by "degrees of freedom" (n - 1). Above 30, 1.96 is close enough.


def proportion_ci(wins, n):
    p = wins / n
    e = 1.96 * math.sqrt(p * (1 - p) / n)
    return (p - e, p + e)


def sample_std(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def mean_ci(xs):
    m = sum(xs) / len(xs)
    e = T95.get(len(xs) - 1, 1.96) * sample_std(xs) / math.sqrt(len(xs))
    return (m - e, m + e)


print(proportion_ci(60, 100), sample_std([70, 72, 68, 75, 65]), mean_ci([70, 72, 68, 75, 65]))
