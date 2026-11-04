r, n, t, x = ns.get("request"), ns.get("notification"), ns.get("tool_call_request"), ns.get("text_of")
assert r and n and t and x, "Keep request, notification, tool_call_request and text_of."
assert r(7, "tools/list") == {"jsonrpc": "2.0", "id": 7, "method": "tools/list"}, f"request(7, 'tools/list') returned {r(7, 'tools/list')!r}. Leave out params when it's None."
assert r(1, "ping", {"a": 1}) == {"jsonrpc": "2.0", "id": 1, "method": "ping", "params": {"a": 1}}, "request with params should include them under 'params'."
assert n("notifications/initialized") == {"jsonrpc": "2.0", "method": "notifications/initialized"}, "A notification has only jsonrpc and method, no id."
want = {"jsonrpc": "2.0", "id": 9, "method": "tools/call", "params": {"name": "add", "arguments": {"a": 1, "b": 2}}}
assert t(9, "add", {"a": 1, "b": 2}) == want, f"tool_call_request(9, 'add', {{'a': 1, 'b': 2}}) returned {t(9, 'add', {'a': 1, 'b': 2})!r}, expected {want!r}."
resp = {"jsonrpc": "2.0", "id": 9, "result": {"content": [{"type": "text", "text": "a"}, {"type": "image", "data": "..."}, {"type": "text", "text": "b"}]}}
assert x(resp) == "a\nb", f"text_of returned {x(resp)!r}, expected 'a\\nb': only items of type text, joined by newlines."
