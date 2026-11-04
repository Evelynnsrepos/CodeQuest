import math


def binom_pmf(k, n, p):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def p_value_at_least(k, n, p):
    return sum(binom_pmf(j, n, p) for j in range(k, n + 1))


def significant(p_value, alpha=0.05):
    return p_value < alpha


print(binom_pmf(15, 20, 0.5), p_value_at_least(15, 20, 0.5), p_value_at_least(60, 100, 0.5), significant(0.028))
