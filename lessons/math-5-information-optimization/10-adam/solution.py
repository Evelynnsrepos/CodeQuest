import math


def adam_step(theta, g, m, v, t, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = [b1 * mi + (1 - b1) * gi for mi, gi in zip(m, g)]
    v = [b2 * vi + (1 - b2) * gi * gi for vi, gi in zip(v, g)]
    out = []
    for th, mi, vi in zip(theta, m, v):
        m_hat = mi / (1 - b1 ** t)
        v_hat = vi / (1 - b2 ** t)
        out.append(th - lr * m_hat / (math.sqrt(v_hat) + eps))
    return out, m, v


print(adam_step([1.0, 1.0], [0.5, 500.0], [0.0, 0.0], [0.0, 0.0], 1))
