def f(x):
    return 3 * x ** 2 - 4 * x + 7


def numeric_derivative(f, x):
    return 0


def df(x):
    return 0


minimum_x = None

for x in [-1, 0, 2, 5]:
    print(f"x={x}: numeric {numeric_derivative(f, x):.4f}, exact {df(x)}")
