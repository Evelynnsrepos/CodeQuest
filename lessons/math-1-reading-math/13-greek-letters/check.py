M = ns.get("MEANING")
assert isinstance(M, dict), "Keep the MEANING dict."
want = {"θ": "parameters", "η": "learning rate", "σ": "standard deviation", "μ": "mean", "ε": "tiny number", "Δ": "change"}
for k, v in want.items():
    got = str(M.get(k, "")).strip().lower()
    assert got == v, f"{k} usually means {v!r} in AI papers (got {got!r}). Check the table."
