zs, pdf, st = ns.get("z_score"), ns.get("normal_pdf"), ns.get("standardize")
assert zs and pdf and st, "Keep z_score, normal_pdf and standardize."
assert zs(185, 170, 10) == 1.5 and zs(160, 170, 10) == -1, f"z_score(185, 170, 10) = 1.5, got {zs(185, 170, 10)!r}."
assert abs(pdf(0, 0, 1) - 0.3989422804) < 1e-9, f"normal_pdf(0, 0, 1) ≈ 0.399, got {pdf(0, 0, 1)!r}."
assert abs(pdf(1, 0, 1) - 0.2419707245) < 1e-9, "normal_pdf(1, 0, 1) ≈ 0.242."
assert abs(pdf(170, 170, 10) - 0.03989422804) < 1e-10, "Wider curve → lower peak: divide by σ."
w = 0.01
area = sum(pdf(-5 + (i + 0.5) * w, 0, 1) for i in range(1000)) * w
assert abs(area - 1) < 1e-6, "The total area under the curve must be 1."
r = st([2, 4, 4, 4, 5, 5, 7, 9])
assert all(abs(a - b) < 1e-12 for a, b in zip(r, [-1.5, -0.5, -0.5, -0.5, 0, 0, 1, 2])) and len(r) == 8, f"standardize gave {r!r}."
