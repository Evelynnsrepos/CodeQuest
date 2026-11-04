import numpy as np
sm, at = ns.get("softmax"), ns.get("attention")
assert sm and at, "Keep softmax and attention."
p = sm(np.array([[1000.0, 1001.0], [0.0, 0.0]]))
assert np.allclose(p, [[0.26894, 0.73106], [0.5, 0.5]], atol=1e-5), "softmax: subtract the row max first (stable) and normalize per row."
rng = np.random.default_rng(1)
Q, K, V = (rng.normal(size=(5, 4)) for _ in range(3))
def ref(Q, K, V, causal):
    s = Q @ K.swapaxes(-1, -2) / np.sqrt(Q.shape[-1])
    if causal:
        n = s.shape[-1]; s = np.where(np.triu(np.ones((n, n), bool), 1), -np.inf, s)
    e = np.exp(s - s.max(-1, keepdims=True)); return (e / e.sum(-1, keepdims=True)) @ V
assert np.allclose(at(Q, K, V), ref(Q, K, V, False)), "attention: softmax(Q Kᵀ / √d) V."
out = at(Q, K, V, causal=True)
assert np.allclose(out, ref(Q, K, V, True)), "causal: mask scores above the diagonal with -inf."
assert np.allclose(out[0], V[0]), "With the causal mask, token 0 can only see itself: its output is V[0]."
Qb, Kb, Vb = (rng.normal(size=(3, 5, 4)) for _ in range(3))
assert np.allclose(at(Qb, Kb, Vb, causal=True), ref(Qb, Kb, Vb, True)), "Batches (b, n, d) must work too: use swapaxes(-1, -2)."
