import math


def alpha_bars(betas):
    out, prod = [], 1.0
    for b in betas:
        prod *= 1 - b
        out.append(prod)
    return out


def add_noise(x0, eps, abar):
    return [math.sqrt(abar) * x + math.sqrt(1 - abar) * e for x, e in zip(x0, eps)]


def predict_x0(xt, eps_hat, abar):
    return [(x - math.sqrt(1 - abar) * e) / math.sqrt(abar) for x, e in zip(xt, eps_hat)]


def guided(eps_uncond, eps_cond, w):
    return [u + w * (c - u) for u, c in zip(eps_uncond, eps_cond)]


betas = [0.1, 0.2, 0.3, 0.4]
abars = alpha_bars(betas)
print("alpha_bar:", [round(a, 4) for a in abars])
x0, eps = [1.0, -0.5], [0.3, 0.8]
if abars:
    xt = add_noise(x0, eps, abars[-1])
    print("noisy:", [round(v, 3) for v in xt])
    print("recovered with the right noise:", [round(v, 3) for v in predict_x0(xt, eps, abars[-1])])
print("guided noise:", [round(v, 3) for v in guided([0.1, 0.2], [0.3, 0.1], 7.5)])
