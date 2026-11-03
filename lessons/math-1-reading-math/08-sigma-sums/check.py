sg, mn, ms = ns.get("sigma"), ns.get("mean"), ns.get("mse")
assert sg and mn and ms, "Keep sigma, mean and mse."
assert sg(lambda i: i ** 2, 1, 3) == 14, f"Σ i² from 1 to 3 should be 14 (end included!), got {sg(lambda i: i ** 2, 1, 3)!r}."
assert sg(lambda i: i, 1, 100) == 5050, "Σ i from 1 to 100 is 5050."
assert sg(lambda i: 2, 0, 4) == 10, "Five terms of 2 (from 0 to 4) is 10."
assert mn([2, 4, 9]) == 5, f"mean([2, 4, 9]) should be 5, got {mn([2, 4, 9])!r}."
assert abs(ms([1, 2, 3], [1, 0, 6]) - 13 / 3) < 1e-12, f"mse should be (0 + 4 + 9) / 3 ≈ 4.333, got {ms([1, 2, 3], [1, 0, 6])!r}."
