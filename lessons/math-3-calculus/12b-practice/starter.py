def slope_at(f, x):
    return 0


def power_rule(c, n, x):
    return 0


def chain_square(a, b, x):
    return 0


def relu_slope(x):
    return 0


def gd_step(w, slope, lr):
    return w


print(slope_at(lambda x: x ** 3, 2), power_rule(5, 3, 2), chain_square(3, 1, 1), relu_slope(-2), gd_step(0, -6, 0.1))
