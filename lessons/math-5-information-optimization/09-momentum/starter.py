def ema(values, beta):
    return []


def momentum_step(theta, v, g, lr, beta):
    return theta, v


def speedup(beta):
    return 1


print(ema([1, 1, 1], 0.9), momentum_step([0.0], [1.0], [1.0], 0.1, 0.9), speedup(0.9))
