h = ns.get("handle")
assert h, "Keep the function handle."
r = h({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2099-01-01", "capabilities": {}}})
assert r and r.get("id") == 1 and r.get("jsonrpc") == "2.0", f"initialize returned {r!r}. Use ok(id, result)."
res = r.get("result", {})
assert res.get("protocolVersion") == "2099-01-01", "Echo the client's protocolVersion from params."
assert res.get("capabilities") == {"tools": {}} and res.get("serverInfo") == {"name": "codequest-notes", "version": "1.0"}, f"initialize result was {res!r}."
assert h({"jsonrpc": "2.0", "method": "notifications/initialized"}) is None, "Notifications (no id) get no response: return None."
r = h({"jsonrpc": "2.0", "id": "x", "method": "tools/list"})
assert r == {"jsonrpc": "2.0", "id": "x", "result": {"tools": ns["TOOLS"]}}, f"tools/list returned {r!r}."
r = h({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_notes", "arguments": {}}})
assert r == {"jsonrpc": "2.0", "id": 3, "result": {"content": [{"type": "text", "text": "ideas.md\ntodo.md"}], "isError": False}}, f"tools/call list_notes returned {r!r}."
try:
    r = h({"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "read_note", "arguments": {"name": "nope.md"}}})
except KeyError:
    raise AssertionError("A failing tool crashed the server. Catch the exception and return a result with isError True.")
assert r.get("result", {}).get("isError") is True and "error" not in r, f"A failing tool should give a normal result with isError True, got {r!r}."
r = h({"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "rm_rf", "arguments": {}}})
assert r.get("result", {}).get("isError") is True, f"An unknown tool should give a result with isError True, got {r!r}."
r = h({"jsonrpc": "2.0", "id": 5, "method": "prompts/list"})
assert r == {"jsonrpc": "2.0", "id": 5, "error": {"code": -32601, "message": "Method not found"}}, f"An unknown method should give error -32601, got {r!r}."
