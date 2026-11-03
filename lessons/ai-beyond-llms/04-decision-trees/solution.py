def gini(labels):
    n = len(labels)
    return 1 - sum((labels.count(k) / n) ** 2 for k in set(labels))


def best_split(xs, labels):
    best = None
    n = len(xs)
    for t in sorted(set(xs)):
        left = [l for x, l in zip(xs, labels) if x <= t]
        right = [l for x, l in zip(xs, labels) if x > t]
        if not left or not right:
            continue
        score = len(left) / n * gini(left) + len(right) / n * gini(right)
        if best is None or score < best[1]:
            best = (t, score)
    return (best[0], round(best[1], 4))


ages = [22, 25, 31, 35, 41, 48, 52, 60]
bought = ["no", "no", "no", "yes", "yes", "yes", "no", "yes"]
print("gini of all:", round(gini(bought), 3))
print("best split:", best_split(ages, bought))
