rp = ns.get("report")
assert rp, "Keep report."
r = rp(60, 100)
assert isinstance(r, dict) and set(r) >= {"rate", "low", "high", "p_value", "better"}, f"report must return a dict with rate, low, high, p_value, better; got {r!r}."
assert r["rate"] == 0.6 and abs(r["low"] - 0.50398) < 1e-4 and abs(r["high"] - 0.69602) < 1e-4, "60/100: rate 0.6, CI ≈ 0.504–0.696."
assert abs(r["p_value"] - 0.0284439668) < 1e-9 and r["better"] is True, "60/100: p ≈ 0.028 → better."
r = rp(6, 10)
assert abs(r["p_value"] - 0.376953125) < 1e-9 and r["better"] is False, "6/10 is no evidence."
r = rp(58, 100)
assert r["better"] is False, "58/100: CI dips below 0.5 → not (yet) better."
assert rp(600, 1000)["better"] is True, "600/1000 is clearly better."
