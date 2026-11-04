im, nm, fm, dm = (ns.get(n) for n in ("is_missing", "normalize_missing", "fill_median", "drop_missing"))
assert im and nm and fm and dm, "Keep all four functions."
for v in (None, "", "  ", "N/A", "n/a", "NULL", " - ", "?", "Unknown"):
    assert im(v), f"is_missing({v!r}) should be True."
for v in ("0", "Ada", 0, "nan?"):
    assert not im(v), f"is_missing({v!r}) should be False (0 is a real value!)."
rows = [{"name": "Ada", "age": "N/A"}, {"name": "-", "age": "34"}]
out = nm(rows)
assert out == [{"name": "Ada", "age": None}, {"name": None, "age": "34"}], f"Got {out!r}."
assert rows[0]["age"] == "N/A", "normalize_missing must not change the original rows."
out = fm([{"x": 1}, {"x": None}, {"x": 100}, {"x": 3}], "x")
assert [r["x"] for r in out] == [1, 3, 100, 3], f"Median of 1, 100, 3 is 3. Got {out!r}."
assert dm([{"a": 1, "b": None}, {"a": 2, "b": 5}, {"a": None, "b": 1}], ["a"]) == [{"a": 1, "b": None}, {"a": 2, "b": 5}], "drop_missing: only the listed columns matter."
