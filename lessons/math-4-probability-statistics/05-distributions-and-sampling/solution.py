def from_samples(samples):
    out = {}
    for s in samples:
        out[s] = out.get(s, 0) + 1
    return {k: v / len(samples) for k, v in out.items()}


def cdf(d, x):
    total = 0
    for k, p in d.items():
        total += p
        if k == x:
            return total
    return total


def sample(d, u):
    total = 0
    for k, p in d.items():
        total += p
        if u < total:
            return k
    return k  # u at the very end: rounding


d = {"cat": 0.5, "dog": 0.3, "fish": 0.2}
print(from_samples([1, 3, 3, 6]), cdf(d, "dog"), [sample(d, u) for u in (0.12, 0.65, 0.93)])
