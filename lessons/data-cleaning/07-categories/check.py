f, c, u = ns.get("fold"), ns.get("canonical"), ns.get("unknowns")
assert f and c and u, "Keep fold, canonical and unknowns."
assert f("  Café   KÖLN ") == "cafe koln", f"fold: tidy, casefold, strip accents. Got {f('  Café   KÖLN ')!r}."
assert f("Straße") == "strasse", "fold: casefold turns ß into ss."
CITY = {"koeln": "Köln", "cologne": "Köln", "munich": "München", "muenchen": "München"}
for s, want in [("Köln", "Köln"), (" KOELN", "Köln"), ("cologne", "Köln"), ("Koln", "Köln"),
                ("Munchen", "München"), ("MÜNCHEN ", "München"), ("Berlin", None)]:
    assert c(s, CITY) == want, f"canonical({s!r}) should be {want!r}, got {c(s, CITY)!r}."
assert u(["Köln", "Berlin", " berlin", "Hamburg", "", None], CITY) == ["berlin", "hamburg"], "unknowns: sorted, distinct, folded."
