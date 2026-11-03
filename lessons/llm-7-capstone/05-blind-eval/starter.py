import math
import random


def make_pairs(base, tuned, seed):
    return []


def score(pairs, judgments):
    return (0, 0, 0)


base = ["b1", "b2", "b3", "b4"]
tuned = ["t1", "t2", "t3", "t4"]
pairs = make_pairs(base, tuned, seed=7)
for p in pairs:
    print(p)
print(score(pairs, ["A", "B", "tie", "A"]))
