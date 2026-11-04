import numpy as np


def softmax(x):
    return x


def attention(Q, K, V, causal=False):
    return V


rng = np.random.default_rng(0)
Q, K, V = (rng.normal(size=(4, 8)) for _ in range(3))
print(attention(Q, K, V, causal=True).shape)
