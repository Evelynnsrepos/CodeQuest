def l2_penalty(ws, lam):
    return lam / 2 * sum(w * w for w in ws)


def l2_grad(ws, lam):
    return [lam * w for w in ws]


def decay(ws, lr, lam):
    return [w * (1 - lr * lam) for w in ws]


print(l2_penalty([3, -4], 0.1), l2_grad([3, -4], 0.1), decay([1.0], 0.001, 0.1))
