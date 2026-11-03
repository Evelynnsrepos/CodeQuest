def product(xs):
    total = 1
    for x in xs:
        total *= x
    return total


def factorial(n):
    return product(range(1, n + 1))


def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


print(product([0.1, 0.05, 0.2]), factorial(5), choose(4, 2))
