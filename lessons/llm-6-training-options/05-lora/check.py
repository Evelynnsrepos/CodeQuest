lp, lf, mg, mv = ns.get("lora_params"), ns.get("lora_forward"), ns.get("merge"), ns["matvec"]
assert lp and lf and mg, "Keep lora_params, lora_forward and merge."
assert lp(4096, 4096, 16) == 131072 and lp(10, 30, 2) == 80, "lora_params(d_in, d_out, r) is r·d_in + d_out·r."
W = [[1.0, 2.0], [3.0, 4.0], [0.0, -1.0]]
A = [[1.0, 0.0], [0.0, 2.0]]
B = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]
x = [1.0, -1.0]
assert lf(W, A, B, x, 16, 2) == mv(W, x), "With B all zeros, the LoRA output must equal the base output (that's why B starts at 0)."
B = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
out = lf(W, A, B, x, 4, 2)
want = [a + 2 * b for a, b in zip(mv(W, x), [1.0, -2.0, -1.0])]
assert all(abs(o - w) < 1e-9 for o, w in zip(out, want)), f"lora_forward returned {out!r}, expected {want!r}: W·x + (α/r)·B·(A·x)."
M = mg(W, A, B, 4, 2)
assert len(M) == 3 and len(M[0]) == 2, "The merged matrix must have the same shape as W."
assert all(abs(o - w) < 1e-9 for o, w in zip(mv(M, x), out)), "The merged matrix must give exactly the same output as the adapter."
assert W == [[1.0, 2.0], [3.0, 4.0], [0.0, -1.0]], "Don't change W itself; return a new merged matrix."
