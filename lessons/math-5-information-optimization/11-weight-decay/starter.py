def l2_penalty(ws, lam):
    return 0


def l2_grad(ws, lam):
    return [0 for w in ws]


def decay(ws, lr, lam):
    return ws


print(l2_penalty([3, -4], 0.1), l2_grad([3, -4], 0.1), decay([1.0], 0.001, 0.1))
