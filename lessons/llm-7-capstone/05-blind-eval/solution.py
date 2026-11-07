import math
import random


def make_pairs(base, tuned, seed):
    rng = random.Random(seed)
    pairs = []
    for i in range(len(base)):
        if rng.random() < 0.5:
            pairs.append({"A": tuned[i], "B": base[i], "tuned": "A"})
        else:
            pairs.append({"A": base[i], "B": tuned[i], "tuned": "B"})
    return pairs


def score(pairs, judgments):
    n = len(pairs)
    wins = 0
    for i in range(n):
        j = judgments[i]
        if j == "tie":
            wins = wins + 0.5
        elif j == pairs[i]["tuned"]:
            wins = wins + 1
    p = wins / n
    margin = 1.96 * math.sqrt(p * (1 - p) / n)
    return (round(p, 3), round(p - margin, 3), round(p + margin, 3))


base = ["b1", "b2", "b3", "b4"]
tuned = ["t1", "t2", "t3", "t4"]
pairs = make_pairs(base, tuned, seed=7)
for p in pairs:
    print(p)
print(score(pairs, ["A", "B", "tie", "A"]))
