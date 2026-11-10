mg, bf = ns.get("model_gb"), ns.get("best_fit")
assert mg and bf, "Keep model_gb and best_fit."
assert mg(8, 16) == 16 and abs(mg(8, 4.5) - 4.5) < 1e-12, "model_gb: params × bits / 8."
assert bf(8, 12) == "Q8", "8B on 12 GB: FP16 needs 17.5, Q8 needs 10 → Q8."
assert bf(8, 24) == "FP16" and bf(14, 12) == "Q4_K_M" and bf(70, 12) is None, "Try FP16, then Q8, then Q4_K_M."
