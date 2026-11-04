def slope_at(f, x):
    h = 1e-5
    return (f(x + h) - f(x - h)) / (2 * h)


def power_rule(c, n, x):
    return c * n * x ** (n - 1)


def chain_square(a, b, x):
    return 2 * (a * x + b) * a


def relu_slope(x):
    return 1 if x > 0 else 0


def gd_step(w, slope, lr):
    return w - lr * slope


print(slope_at(lambda x: x ** 3, 2), power_rule(5, 3, 2), chain_square(3, 1, 1), relu_slope(-2), gd_step(0, -6, 0.1))
