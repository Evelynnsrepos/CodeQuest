run, make_csv = ns.get("run"), ns.get("make_csv")
assert run and make_csv, "Keep run and make_csv."
r = run(make_csv(300, seed=7))
assert r["rows"] == 300, f"rows should be 300, got {r['rows']}."
assert r["features"] == 9, f"Temperatur, Regen and 7 one-hot day columns = 9 features, got {r['features']}."
assert 0.9 < r["baseline_r2"] <= 1, f"The linear baseline should reach R² > 0.9, got {r['baseline_r2']:.3f}. Did decimal=',' read the numbers?"
assert 0.9 < r["torch_r2"] <= 1, f"The PyTorch model should reach R² > 0.9, got {r['torch_r2']:.3f}. Standardize X and y and undo the y scaling."
