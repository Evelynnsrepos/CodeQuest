import statistics


def fences(xs, k=1.5):
    q1, _, q3 = statistics.quantiles(xs, n=4)
    iqr = q3 - q1
    return (q1 - k * iqr, q3 + k * iqr)


def outliers(xs, k=1.5):
    low, high = fences(xs, k)
    return [i for i, x in enumerate(xs) if x < low or x > high]


def z_outliers(xs, limit=3):
    m, s = statistics.mean(xs), statistics.pstdev(xs)
    return [i for i, x in enumerate(xs) if s and abs(x - m) / s > limit]


prices = [3.2, 2.9, 3.5, 3.1, 99999, 3.3]
print(fences(prices), outliers(prices), z_outliers(prices))
