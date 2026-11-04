def evaluate(coeffs, x):
    return sum(c * x ** n for n, c in enumerate(coeffs))


def derive(coeffs):
    return [n * c for n, c in enumerate(coeffs)][1:]


p = [7, 5, 3]
print(evaluate(p, 2), derive(p), evaluate(derive(p), 2))
