f = ns.get("mcp_entry")
assert f, "Define a function called mcp_entry."
got = f("shop", "https://n8n.local/mcp/x1", "tok")
assert "mcpServers" in got and "shop" in got["mcpServers"], "Top level: {'mcpServers': {name: {...}}}."
e = got["mcpServers"]["shop"]
assert e.get("command") == "npx", "command is 'npx'."
assert e.get("args") == ["mcp-remote", "https://n8n.local/mcp/x1", "--header", "Authorization: Bearer ${AUTH_TOKEN}"], f"args are wrong: {e.get('args')!r}."
assert e.get("env") == {"AUTH_TOKEN": "tok"}, "The token goes in env as AUTH_TOKEN."
assert "tok" not in " ".join(e["args"]), "The real token must not appear in args."
