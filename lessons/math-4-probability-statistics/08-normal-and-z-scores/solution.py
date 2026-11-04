import math


def z_score(x, mu, sigma):
    return (x - mu) / sigma


def normal_pdf(x, mu, sigma):
    z = z_score(x, mu, sigma)
    return math.exp(-z * z / 2) / (sigma * math.sqrt(2 * math.pi))


def standardize(xs):
    mu = sum(xs) / len(xs)
    sigma = math.sqrt(sum((x - mu) ** 2 for x in xs) / len(xs))
    return [(x - mu) / sigma for x in xs]


print(z_score(185, 170, 10), normal_pdf(0, 0, 1), standardize([2, 4, 4, 4, 5, 5, 7, 9]))
