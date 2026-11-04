import time
import numpy as np
st, cm, ms = ns.get("standardize"), ns.get("cosine_matrix"), ns.get("most_similar")
assert st and cm and ms, "Keep standardize, cosine_matrix and most_similar."
X = np.array([[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]])
Z = np.asarray(st(X))
assert Z.shape == (3, 2) and np.allclose(Z.mean(axis=0), 0) and np.allclose(Z.std(axis=0), 1), "standardize: every column should end with mean 0 and std 1."
A = np.array([[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]])
C = np.asarray(cm(A))
assert C.shape == (3, 3) and np.allclose(np.diag(C), 1), "cosine_matrix: shape (rows, rows), 1 on the diagonal."
assert abs(C[0, 1] - 0.99388) < 1e-4 and abs(C[0, 2]) < 1e-12, f"cosine of rows 0 and 1 ≈ 0.994, rows 0 and 2 = 0. Got {C[0, 1]:.4f}, {C[0, 2]:.4f}."
assert ms(A, 0) == 1 and ms(A, 2) == 1, "most_similar: skip the row itself."
big = np.random.default_rng(0).normal(size=(2000, 256))
t = time.perf_counter(); st(big); cm(big); t = time.perf_counter() - t
assert t < 2.0, f"That took {t:.1f} s: use whole-array operations, not loops."
