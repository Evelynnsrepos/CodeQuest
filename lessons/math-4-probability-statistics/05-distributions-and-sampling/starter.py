def from_samples(samples):
    return {}


def cdf(d, x):
    return 0


def sample(d, u):
    return None


d = {"cat": 0.5, "dog": 0.3, "fish": 0.2}
print(from_samples([1, 3, 3, 6]), cdf(d, "dog"), [sample(d, u) for u in (0.12, 0.65, 0.93)])
