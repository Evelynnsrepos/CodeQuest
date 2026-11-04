import statistics


def fences(xs, k=1.5):
    return (0, 0)


def outliers(xs, k=1.5):
    return []


def z_outliers(xs, limit=3):
    return []


prices = [3.2, 2.9, 3.5, 3.1, 99999, 3.3]
print(fences(prices), outliers(prices), z_outliers(prices))
