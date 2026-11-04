f = ns.get("code_node")
assert f, "Define a function called code_node."
items = [{"json": {"id": 1, "amount": 40}}, {"json": {"id": 2, "amount": 250}}, {"json": {"id": 3, "amount": 100}}, {"json": {"id": 4, "amount": 101}}]
got = f(items)
assert got == [{"json": {"id": 2, "amount": 250, "big": True}}, {"json": {"id": 4, "amount": 101, "big": True}}], f"Keep amounts over 100 (100 itself isn't over), add big: True. Got {got!r}."
assert "big" not in items[1]["json"], "Don't change the input items; build new ones."
assert f([]) == [], "No items in, no items out."
