import math
import random


def make_pairs(base, tuned, seed):
    rng = random.Random(seed)
    pairs = []
    for b, t in zip(base, tuned):
        if rng.random() < 0.5:
            pairs.append({"A": t, "B": b, "tuned": "A"})
        else:
            pairs.append({"A": b, "B": t, "tuned": "B"})
    return pairs


def score(pairs, judgments):
    n = len(pairs)
    wins = 0
    for p, j in zip(pairs, judgments):
        if j == "tie":
            wins += 0.5
        elif j == p["tuned"]:
            wins += 1
    p = wins / n
    margin = 1.96 * math.sqrt(p * (1 - p) / n)
    return (round(p, 3), round(p - margin, 3), round(p + margin, 3))


base = ["b1", "b2", "b3", "b4"]
tuned = ["t1", "t2", "t3", "t4"]
pairs = make_pairs(base, tuned, seed=7)
for p in pairs:
    print(p)
print(score(pairs, ["A", "B", "tie", "A"]))
