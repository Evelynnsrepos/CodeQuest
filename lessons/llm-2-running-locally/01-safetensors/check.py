import json
r, c = ns.get("read_header"), ns.get("count_params")
assert r and c, "Keep the functions read_header and count_params."
h = {"a": {"dtype": "F32", "shape": [3, 5], "data_offsets": [0, 60]}, "__metadata__": {"x": "y"}}
t = json.dumps(h).encode("utf-8")
got = r(len(t).to_bytes(8, "little") + t + bytes(60))
assert got == h, f"read_header returned {got!r} for a file whose header is {h!r}. Read n from the first 8 bytes, then the next n bytes."
got = c(h)
assert got == 15, f"count_params returned {got!r} for one tensor of shape [3, 5], expected 15. Did you skip __metadata__?"
got = c({"w": {"shape": [2, 3, 4]}, "b": {"shape": [7]}})
assert got == 31, f"count_params returned {got!r} for shapes [2, 3, 4] and [7], expected 24 + 7 = 31."
