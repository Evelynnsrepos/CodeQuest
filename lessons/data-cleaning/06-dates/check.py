ti, bd = ns.get("to_iso"), ns.get("bad_dates")
assert ti and bd, "Keep to_iso and bad_dates."
for s, want in [("04.11.2026", "2026-11-04"), (" 2026-11-04 ", "2026-11-04"), ("11/04/2026", "2026-11-04"),
                ("4 Nov 2026", "2026-11-04"), ("04.11.26", "2026-11-04")]:
    assert ti(s) == want, f"to_iso({s!r}) should be {want!r}, got {ti(s)!r}."
assert ti("31.02.2026") is None, "31 February doesn't exist: None."
assert ti(None) is None and ti("soon") is None, "Unparseable → None."
assert ti("03/04/2026", ["%d/%m/%Y"]) == "2026-04-03", "Use the formats you're given, in order."
assert bd(["04.11.2026", "", "soon", None, "31.02.2026"]) == [2, 4], f"bad_dates: skip blanks, report the rest. Got {bd(['04.11.2026', '', 'soon', None, '31.02.2026'])!r}."
