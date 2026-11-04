pc, T = ns.get("percentile"), ns.get("Tracker")
assert pc and T, "Keep percentile and Tracker."
xs = list(range(1, 101))
assert pc(xs, 50) == 50 and pc(xs, 95) == 95 and pc(xs, 99) == 99 and pc([7], 95) == 7, "Nearest rank: position ceil(p/100 · n)."
assert pc([5, 1, 3], 50) == 3, "Sort first."
t = T()
for ms in [300, 320, 350, 400, 420, 450, 500, 600, 900, 4000]:
    t.record("small", 2000, 300, ms)
t.record("big", 10000, 1000, 2500)
assert abs(t.cost() - (10 * (2000 * 0.25 + 300 * 1.25) + 10000 * 3 + 1000 * 15) / 1e6) < 1e-12, f"Total cost wrong: {t.cost()!r}."
bm = t.cost_by_model()
assert abs(bm["small"] - 0.00875) < 1e-12 and abs(bm["big"] - 0.045) < 1e-12, f"cost_by_model: {bm!r}."
assert t.latency() == {"p50": 450, "p95": 4000, "p99": 4000}, f"latency over all 11 calls: {t.latency()!r}."
assert t.over_budget(0.05) and not t.over_budget(0.06), "over_budget: total > limit."
