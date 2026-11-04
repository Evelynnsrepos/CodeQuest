fl, rj = ns.get("flatten"), ns.get("read_jsonl")
assert fl and rj, "Keep flatten and read_jsonl."
got = fl({"user": {"name": "Ada", "address": {"city": "Berlin"}}, "tags": ["a", "b"], "n": 1})
assert got == {"user.name": "Ada", "user.address.city": "Berlin", "tags": ["a", "b"], "n": 1}, f"Got {got!r}."
assert fl({}) == {} and fl({"a": {}}) == {}, "Empty dicts flatten to nothing."
text = '{"prompt": "hi", "answer": "hello"}\n\n{broken\n[1, 2]\n{"prompt": "x", "answer": "y"}\n'
recs, bad = rj(text)
assert recs == [{"prompt": "hi", "answer": "hello"}, {"prompt": "x", "answer": "y"}], f"Got {recs!r}."
assert bad == [3, 4], f"Line 3 is broken, line 4 is a list, not an object (1-based, blank line 2 skipped). Got {bad!r}."
