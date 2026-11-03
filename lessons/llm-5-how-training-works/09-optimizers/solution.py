import math


def adamw_step(params, grads, m, v, t, lr, wd):
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    for i in range(len(params)):
        g = grads[i]
        m[i] = beta1 * m[i] + (1 - beta1) * g
        v[i] = beta2 * v[i] + (1 - beta2) * g * g
        m_hat = m[i] / (1 - beta1 ** t)
        v_hat = v[i] / (1 - beta2 ** t)
        params[i] = params[i] - lr * wd * params[i] - lr * m_hat / (math.sqrt(v_hat) + eps)


def lr_at(step, max_lr, warmup, total):
    if step < warmup:
        return max_lr * (step + 1) / warmup
    progress = (step - warmup) / (total - warmup)
    return max_lr * 0.5 * (1 + math.cos(math.pi * progress))


def valley_grad(p):
    x, y = p
    return [2 * x, 200 * y]          # gradient of x² + 100·y²


def valley(p):
    return p[0] ** 2 + 100 * p[1] ** 2


sgd = [5.0, 1.0]
for _ in range(100):
    g = valley_grad(sgd)
    sgd = [sgd[0] - 0.009 * g[0], sgd[1] - 0.009 * g[1]]

adam, m, v = [5.0, 1.0], [0.0, 0.0], [0.0, 0.0]
for t in range(1, 101):
    adamw_step(adam, valley_grad(adam), m, v, t, 0.1, 0.0)

print(f"SGD   after 100 steps: loss {valley(sgd):.4f}")
print(f"AdamW after 100 steps: loss {valley(adam):.4f}")
print("schedule:", [round(lr_at(s, 3e-4, 10, 100) * 1e4, 2) for s in [0, 4, 9, 10, 55, 99]], "(× 1e-4)")
