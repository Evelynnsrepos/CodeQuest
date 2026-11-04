import math


def accuracy(preds, gold):
    return 0.0


def win_interval(wins, n):
    return (0.0, 0.0)


def is_better(wins, n):
    return False


print(accuracy(["Paris", "berlin ", "Rome"], ["paris", "Berlin", "Madrid"]), win_interval(60, 100), is_better(6, 10))
