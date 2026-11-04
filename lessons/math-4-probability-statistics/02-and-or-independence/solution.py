def p_and(pa, pb):
    return pa * pb


def p_or(pa, pb, pab):
    return pa + pb - pab


def p_all(p, n):
    return p ** n


def p_at_least_one(p, n):
    return 1 - (1 - p) ** n


print(p_and(0.5, 0.5), p_or(13 / 52, 4 / 52, 1 / 52), p_all(0.95, 20), p_at_least_one(0.05, 10))
