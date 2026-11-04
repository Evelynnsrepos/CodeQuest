import statistics


def correlation(xs, ys):
    return 0.0


def r_squared(xs, ys):
    return 0.0


def most_correlated(columns, target):
    return None


hours, score = [1, 2, 3, 4, 5], [50, 55, 65, 70, 80]
print(correlation(hours, score), correlation([h * 60 for h in hours], score))
