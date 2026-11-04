f = ns.get("process_new")
assert f, "Define a function called process_new."
seen, done = [], {"a"}
n = f([("a", 1), ("b", 2), ("c", 3)], done, seen.append)
assert seen == [2, 3], f"Handle only items not in done, got {seen!r}."
assert n == 2, f"Return how many were handled this run (2), got {n!r}."
assert done == {"a", "b", "c"}, "Add each handled ID to done."
assert f([("a", 1), ("b", 2)], done, seen.append) == 0, "A second run handles nothing."
def boom(d):
    if d == "bad":
        raise ValueError("model down")
done2 = set()
try:
    f([("x", "ok"), ("y", "bad")], done2, boom)
except ValueError:
    pass
else:
    raise AssertionError("Let errors from handle go up.")
assert done2 == {"x"}, f"A failed item must not be marked done, got {done2!r}."
