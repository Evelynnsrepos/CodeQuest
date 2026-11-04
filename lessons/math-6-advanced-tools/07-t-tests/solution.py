import math
import statistics

T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306,
       9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
       16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074,
       23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048, 29: 2.045, 30: 2.042}


def welch(a, b):
    # df = (va/na + vb/nb)² / ((va/na)² / (na − 1) + (vb/nb)² / (nb − 1)),  va = sample variance of a
    va, vb = statistics.variance(a) / len(a), statistics.variance(b) / len(b)
    t = (statistics.mean(a) - statistics.mean(b)) / math.sqrt(va + vb)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    return t, df


def significant(a, b):
    t, df = welch(a, b)
    d = int(df)
    return abs(t) > (T95[d] if d <= 30 else 1.96)


A, B = [72, 75, 70, 74, 69], [68, 70, 66, 71, 65]
print(welch(A, B), significant(A, B))
