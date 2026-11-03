def gini(labels):
    return 0.0


def best_split(xs, labels):
    return (None, 1.0)


ages = [22, 25, 31, 35, 41, 48, 52, 60]
bought = ["no", "no", "no", "yes", "yes", "yes", "no", "yes"]
print("gini of all:", round(gini(bought), 3))
print("best split:", best_split(ages, bought))
