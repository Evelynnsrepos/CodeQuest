f = ns.get("hsa_override")
assert f, "Keep the function hsa_override."
for gfx, want in [("gfx1031", "10.3.0"), ("gfx1035", "10.3.0"), ("gfx1102", "11.0.0"), ("gfx1100", "11.0.0"), ("gfx803", None), ("gfx90a", None)]:
    got = f(gfx)
    assert got == want, f"hsa_override({gfx!r}) returned {got!r}, expected {want!r}."
