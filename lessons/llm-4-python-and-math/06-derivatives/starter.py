def f(x):
    return 3 * x ** 2 - 4 * x + 7


def numeric_derivative(f, x):
    # h = 1e-5
    # return (f(x + h) - f(x - h)) / (2 * h)
    return 0


def df(x):
    # return 6 * x - 4
    return 0


minimum_x = None  # change None to: 2 / 3

for x in [-1, 0, 2, 5]:
    print(f"x={x}: numeric {numeric_derivative(f, x):.4f}, exact {df(x)}")
