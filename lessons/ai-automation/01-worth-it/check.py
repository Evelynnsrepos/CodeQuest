f = ns.get("payback_weeks")
assert f, "Define a function called payback_weeks."
for args, want in [((2, 5, 3), 18), ((5, 7, 1), 2), ((10, 6, 1), 1), ((1, 1, 2), 120)]:
    got = f(*args)
    assert got == want, f"payback_weeks{args} returned {got!r}, expected {want}."
assert f(0, 10, 1) is None, "When nothing is saved, return None (and don't divide by zero)."
assert f(3, 0, 1) is None, "Zero runs per week also saves nothing: return None."
