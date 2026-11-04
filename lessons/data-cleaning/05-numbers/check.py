p = ns.get("parse_number")
assert p, "Keep parse_number."
cases = [(("1.234,56 €", ","), 1234.56), (("$1,234.56", "."), 1234.56), (("12%", "."), 0.12),
         (("12,5%", ","), 0.125), (("1\xa0234", "."), 1234.0), (("-3,5", ","), -3.5), (("7", ","), 7.0)]
for (s, dec), want in cases:
    got = p(s, decimal=dec)
    assert got is not None and abs(got - want) < 1e-9, f"parse_number({s!r}, decimal={dec!r}) should be {want}, got {got!r}."
for s in (None, "", "  ", "abc", "12 apples"):
    assert p(s) is None, f"parse_number({s!r}) should be None."
