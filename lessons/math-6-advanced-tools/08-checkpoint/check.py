an = ns.get("analyse")
assert an, "Keep analyse."
features = {"length_chars": [120, 340, 90, 560, 210, 430], "length_tokens": [31, 86, 24, 139, 54, 107], "rating": [4, 3, 5, 2, 4, 3]}
A = [0.71, 0.74, 0.69, 0.73, 0.72, 0.70]
B = [0.68, 0.70, 0.69, 0.67, 0.71, 0.66]
r = an(features, A, B)
assert set(r) >= {"redundant", "explained", "t", "df", "better"}, f"Missing keys in {r!r}."
assert [tuple(p) for p in r["redundant"]] == [("length_chars", "length_tokens"), ("length_chars", "rating"), ("length_tokens", "rating")], f"redundant: all pairs with |r| > 0.95 (longer answers got lower ratings here too), sorted. Got {r['redundant']!r}."
assert 0.9 < r["explained"] <= 1.0, f"With three nearly redundant columns, PC1 keeps over 90%: got {r['explained']:.3f}."
assert abs(r["t"] - 2.7775) < 1e-3 and abs(r["df"] - 10) < 1e-6, "t ≈ 2.78, df = 10."
assert r["better"] is True, "Significant and A's mean is higher → better."
assert an(features, B, A)["better"] is False, "Significant but A is lower → not better."
assert an(features, [0.7, 0.71, 0.69], [0.7, 0.69, 0.71])["better"] is False, "Not significant → not better."
