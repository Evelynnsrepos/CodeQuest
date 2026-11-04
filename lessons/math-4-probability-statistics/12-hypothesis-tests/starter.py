import math


def binom_pmf(k, n, p):
    return 0


def p_value_at_least(k, n, p):
    return 1


def significant(p_value, alpha=0.05):
    return False


print(binom_pmf(15, 20, 0.5), p_value_at_least(15, 20, 0.5), p_value_at_least(60, 100, 0.5), significant(0.028))
