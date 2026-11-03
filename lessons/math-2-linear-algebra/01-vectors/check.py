d, e, fv = ns.get("dim"), ns.get("entry"), ns.get("flat_vector")
assert d and e and fv, "Keep dim, entry and flat_vector."
assert d([4, -1, 7]) == 3 and d([0.0] * 4096) == 4096, "dim is the number of entries."
assert e([4, -1, 7], 1) == 4 and e([4, -1, 7], 3) == 7, f"entry(v, 1) is the FIRST entry (4), got {e([4, -1, 7], 1)!r}. Math counts from 1."
assert fv({"rooms": 3, "floor": 2, "size": 65}) == [65, 3, 2], "Order matters: (size, rooms, floor)."
