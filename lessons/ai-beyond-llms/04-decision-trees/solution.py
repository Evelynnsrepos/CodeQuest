def gini(labels):
    n = len(labels)
    total = 0
    for k in set(labels):
        share = labels.count(k) / n
        total = total + share ** 2
    return 1 - total


def best_split(xs, labels):
    n = len(xs)
    best_t = None
    best_score = None
    for t in sorted(set(xs)):
        left = []
        right = []
        for i in range(n):
            if xs[i] <= t:
                left.append(labels[i])
            else:
                right.append(labels[i])
        if len(left) == 0 or len(right) == 0:
            continue
        score = len(left) / n * gini(left) + len(right) / n * gini(right)
        if best_score is None or score < best_score:
            best_t = t
            best_score = score
    return (best_t, round(best_score, 4))


ages = [22, 25, 31, 35, 41, 48, 52, 60]
bought = ["no", "no", "no", "yes", "yes", "yes", "no", "yes"]
print("gini of all:", round(gini(bought), 3))
print("best split:", best_split(ages, bought))
