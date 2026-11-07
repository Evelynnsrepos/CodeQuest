import math


def alpha_bars(betas):
    out = []
    prod = 1.0
    for b in betas:
        prod = prod * (1 - b)
        out.append(prod)
    return out


def add_noise(x0, eps, abar):
    out = []
    for i in range(len(x0)):
        out.append(math.sqrt(abar) * x0[i] + math.sqrt(1 - abar) * eps[i])
    return out


def predict_x0(xt, eps_hat, abar):
    out = []
    for i in range(len(xt)):
        out.append((xt[i] - math.sqrt(1 - abar) * eps_hat[i]) / math.sqrt(abar))
    return out


def guided(eps_uncond, eps_cond, w):
    out = []
    for i in range(len(eps_cond)):
        u = eps_uncond[i]
        out.append(u + w * (eps_cond[i] - u))
    return out


betas = [0.1, 0.2, 0.3, 0.4]
abars = alpha_bars(betas)
print("alpha_bar:", [round(a, 4) for a in abars])
x0, eps = [1.0, -0.5], [0.3, 0.8]
if abars:
    xt = add_noise(x0, eps, abars[-1])
    print("noisy:", [round(v, 3) for v in xt])
    print("recovered with the right noise:", [round(v, 3) for v in predict_x0(xt, eps, abars[-1])])
print("guided noise:", [round(v, 3) for v in guided([0.1, 0.2], [0.3, 0.1], 7.5)])
