tf, co, pl = ns.get("train_flops"), ns.get("chinchilla_optimal"), ns.get("predicted_loss")
assert tf and co and pl, "Keep train_flops, chinchilla_optimal and predicted_loss."
assert tf(1e9, 2e10) == 1.2e20, f"train_flops(1e9, 2e10) should be 1.2e20, got {tf(1e9, 2e10)!r}."
N, D = co(1.2e21)
assert abs(N - 1e19 ** 0.5) < 1, f"N should be sqrt(C/120), got {N!r}."
assert abs(D - 20 * N) < 1e-3 * D, "D should be 20 times N."
assert abs(tf(N, D) - 1.2e21) < 1e12, "The optimal N and D should use exactly the budget."
got = pl(7e10, 1.4e12)
assert abs(got - 1.93665) < 1e-4, f"Chinchilla itself (70B params, 1.4T tokens) should come out near 1.937, got {got!r}."
assert pl(1e9, 1e12) > pl(1e10, 1e12), "A bigger model with the same data should predict a lower loss."
