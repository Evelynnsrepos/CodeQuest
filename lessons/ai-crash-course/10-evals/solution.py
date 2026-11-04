import math


def accuracy(preds, gold):
    return sum(p.strip().lower() == g.strip().lower() for p, g in zip(preds, gold)) / len(gold)


def win_interval(wins, n):
    p = wins / n
    e = 2 * math.sqrt(p * (1 - p) / n)
    return (p - e, p + e)


def is_better(wins, n):
    return win_interval(wins, n)[0] > 0.5


print(accuracy(["Paris", "berlin ", "Rome"], ["paris", "Berlin", "Madrid"]), win_interval(60, 100), is_better(6, 10))
