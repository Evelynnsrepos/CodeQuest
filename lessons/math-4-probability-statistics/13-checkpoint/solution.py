import math


def report(wins, n):
    rate = wins / n
    e = 1.96 * math.sqrt(rate * (1 - rate) / n)
    p_value = sum(math.comb(n, j) for j in range(wins, n + 1)) * 0.5 ** n
    return {"rate": rate, "low": rate - e, "high": rate + e, "p_value": p_value,
            "better": p_value < 0.05 and rate - e > 0.5}


print(report(60, 100))
print(report(6, 10))
