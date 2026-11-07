import numpy as np


def softmax(x):
    shifted = x - x.max(axis=-1, keepdims=True)
    e = np.exp(shifted)
    return e / e.sum(axis=-1, keepdims=True)


def attention(Q, K, V, causal=False):
    d = Q.shape[-1]
    scores = Q @ K.swapaxes(-1, -2) / np.sqrt(d)
    if causal:
        n = scores.shape[-1]
        mask = np.triu(np.ones((n, n), dtype=bool), k=1)
        scores = np.where(mask, -np.inf, scores)
    return softmax(scores) @ V


rng = np.random.default_rng(0)
Q, K, V = (rng.normal(size=(4, 8)) for _ in range(3))
print(attention(Q, K, V, causal=True).shape)
