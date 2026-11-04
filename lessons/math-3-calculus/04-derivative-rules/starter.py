def evaluate(coeffs, x):
    return 0


def derive(coeffs):
    return coeffs


p = [7, 5, 3]
print(evaluate(p, 2), derive(p), evaluate(derive(p), 2))
