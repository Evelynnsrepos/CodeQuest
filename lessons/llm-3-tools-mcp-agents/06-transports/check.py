f = ns.get("read_stdio")
assert f, "Keep the function read_stdio."
raw = '{"jsonrpc": "2.0", "id": 5, "result": {}}\n\nDEBUG hello\n{"jsonrpc": "2.0", "method": "notifications/progress"}\n{"jsonrpc": "2.0", "id": "abc", "error": {"code": -32601, "message": "Method not found"}}\nnot json either\n'
try:
    resp, notes, bad = f(raw)
except ValueError:
    raise AssertionError("A line that isn't JSON crashed read_stdio. Catch the ValueError and count it.")
assert set(resp) == {5, "abc"}, f"responses has ids {sorted(map(str, resp))}, expected 5 and 'abc'. Error responses have ids too."
assert resp[5] == {"jsonrpc": "2.0", "id": 5, "result": {}}, "Store the whole message under its id."
assert notes == ["notifications/progress"], f"notifications is {notes!r}, expected ['notifications/progress']."
assert bad == 2, f"bad_lines is {bad!r}, expected 2. Don't count empty lines."
