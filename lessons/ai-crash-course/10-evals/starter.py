import math


def accuracy(preds, gold):
    # right = 0
    # for i in range(len(gold)):
    #     if preds[i].strip().lower() == gold[i].strip().lower(): right = right + 1
    # return right / len(gold)
    return 0.0


def win_interval(wins, n):
    # p = wins / n
    # margin = 2 * math.sqrt(p * (1 - p) / n)
    # return (p - margin, p + margin)
    return (0.0, 0.0)


def is_better(wins, n):
    # low = win_interval(wins, n)[0]
    # return low > 0.5
    return False


print(accuracy(["Paris", "berlin ", "Rome"], ["paris", "Berlin", "Madrid"]), win_interval(60, 100), is_better(6, 10))
