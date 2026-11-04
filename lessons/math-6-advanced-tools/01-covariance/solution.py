def covariance(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (len(xs) - 1)


def cov_matrix(columns):
    return [[covariance(a, b) for b in columns] for a in columns]


hours, score = [1, 2, 3, 4, 5], [50, 55, 65, 70, 80]
print(covariance(hours, score), cov_matrix([hours, score]))
