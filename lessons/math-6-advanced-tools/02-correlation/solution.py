import statistics


def covariance(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (len(xs) - 1)


def correlation(xs, ys):
    return covariance(xs, ys) / (statistics.stdev(xs) * statistics.stdev(ys))


def r_squared(xs, ys):
    return correlation(xs, ys) ** 2


def most_correlated(columns, target):
    return max(columns, key=lambda name: abs(correlation(columns[name], target)))


hours, score = [1, 2, 3, 4, 5], [50, 55, 65, 70, 80]
print(correlation(hours, score), correlation([h * 60 for h in hours], score))
