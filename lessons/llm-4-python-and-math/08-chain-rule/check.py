sg, dsg, cg, ce = ns.get("sigmoid"), ns.get("dsigmoid"), ns.get("ce_grad"), ns["cross_entropy"]
assert sg and dsg and cg, "Keep sigmoid, dsigmoid and ce_grad."
assert abs(sg(0) - 0.5) < 1e-12, f"sigmoid(0) returned {sg(0)!r}, expected 0.5."
assert abs(sg(2) - 1 / (1 + 2.718281828459045 ** -2)) < 1e-9, f"sigmoid(2) returned {sg(2)!r}."
h = 1e-5
for z in [-2.0, 0.0, 1.5]:
    num = (sg(z + h) - sg(z - h)) / (2 * h)
    assert abs(dsg(z) - num) < 1e-6, f"dsigmoid({z}) returned {dsg(z)!r}, but the numerical slope is {num:.6f}."
logits, t = [0.5, -1.0, 2.0, 0.0], 2
g = cg(logits, t)
assert len(g) == 4, f"ce_grad should return one number per logit, got {g!r}."
for i in range(4):
    up, down = list(logits), list(logits)
    up[i] += h
    down[i] -= h
    num = (ce(up, t) - ce(down, t)) / (2 * h)
    assert abs(g[i] - num) < 1e-6, f"ce_grad entry {i} is {g[i]:.6f}, but the numerical gradient is {num:.6f}."
assert abs(sum(g)) < 1e-9, "The entries of the softmax + cross-entropy gradient always add up to 0."
