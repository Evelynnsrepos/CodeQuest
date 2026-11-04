def ema(values, beta):
    s, out = 0, []
    for x in values:
        s = beta * s + (1 - beta) * x
        out.append(s)
    return out


def momentum_step(theta, v, g, lr, beta):
    v = [beta * vi + gi for vi, gi in zip(v, g)]
    return [t - lr * vi for t, vi in zip(theta, v)], v


def speedup(beta):
    return 1 / (1 - beta)


print(ema([1, 1, 1], 0.9), momentum_step([0.0], [1.0], [1.0], 0.1, 0.9), speedup(0.9))
