import math
tr, mm, ts, r1, fr, lp, fp = (ns.get(n) for n in ("transpose", "matmul", "top_singular", "rank1", "frobenius", "lora_params", "full_params"))
assert all((tr, mm, ts, r1, fr, lp, fp)), "Keep all seven functions."
assert tr([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "transpose: rows become columns."
assert mm([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]], "matmul."
s, u, v = ts([[3, 0], [4, 5]])
assert abs(s - math.sqrt(45)) < 1e-6, f"σ₁ = √45 ≈ 6.708, got {s!r}."
assert abs(abs(u[0]) - 1 / math.sqrt(10)) < 1e-6 and abs(abs(v[0]) - 1 / math.sqrt(2)) < 1e-6, "u ≈ (0.316, 0.949), v ≈ (0.707, 0.707)."
R = r1([[3, 0], [4, 5]])
assert all(abs(R[i][j] - [[1.5, 1.5], [4.5, 4.5]][i][j]) < 1e-6 for i in range(2) for j in range(2)), f"rank1 = [[1.5, 1.5], [4.5, 4.5]], got {R!r}."
err = fr([[3 - R[0][0], 0 - R[0][1]], [4 - R[1][0], 5 - R[1][1]]])
assert abs(err - math.sqrt(5)) < 1e-6, "The rank-1 error equals σ₂ = √5."
s, u, v = ts([[2, 0, 0], [0, 1, 0]])
assert abs(s - 2) < 1e-6, "Works for non-square matrices too."
assert lp(4096, 4096, 16) == 131072 and fp(4096, 4096) == 16777216, "LoRA rank 16: 131,072 numbers instead of 16.8 million."
