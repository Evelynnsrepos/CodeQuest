def solve(a, b, c):
    return (c - b) / a


def check(a, b, c, x):
    return abs(a * x + b - c) < 1e-9


def max_tokens(budget, model_size, per_token):
    return solve(per_token, model_size, budget)


print(solve(2, 1, 9), check(2, 1, 9, 4), max_tokens(12, 5, 0.0002))
