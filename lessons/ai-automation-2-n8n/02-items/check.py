ti, rn = ns.get("to_items"), ns.get("run_node")
assert ti and rn, "Define to_items and run_node."
assert ti([{"a": 1}, {"a": 2}]) == [{"json": {"a": 1}}, {"json": {"a": 2}}], "Wrap each row as {'json': row}."
assert ti([]) == [], "No rows, no items."
calls = []
def fn(j):
    calls.append(j)
    return {"n": j["a"] * 10}
assert rn(ti([{"a": 1}, {"a": 2}, {"a": 3}]), fn) == [{"json": {"n": 10}}, {"json": {"n": 20}}, {"json": {"n": 30}}], "Return new items with fn's result under 'json'."
assert len(calls) == 3, "The node runs once per item."
