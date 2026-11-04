def partial(f, point, i, h=1e-5):
    return 0


def loss_partials(w, b, x, y):
    return (0, 0)


L = lambda w, b: (w * 2 + b - 7) ** 2
print(partial(L, [1, 1], 0), partial(L, [1, 1], 1), loss_partials(1, 1, 2, 7))
