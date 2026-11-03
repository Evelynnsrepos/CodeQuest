s, h, fc = ns.get("stdio_server"), ns.get("http_server"), ns.get("filesystem_config")
assert s and h and fc, "Keep stdio_server, http_server and filesystem_config."
assert s("uvx", ["mcp-server-git"]) == {"command": "uvx", "args": ["mcp-server-git"]}, f"stdio_server('uvx', ['mcp-server-git']) returned {s('uvx', ['mcp-server-git'])!r}. Leave out env when it isn't given."
assert s("node", ["x.js"], {"KEY": "1"}) == {"command": "node", "args": ["x.js"], "env": {"KEY": "1"}}, "With env given, add it under 'env'."
assert h("https://a.b/mcp") == {"url": "https://a.b/mcp"}, "http_server without a token is just {'url': ...}."
assert h("https://a.b/mcp", "t") == {"url": "https://a.b/mcp", "headers": {"Authorization": "Bearer t"}}, "With a token, add headers with 'Authorization': 'Bearer ' + token."
want = {"mcpServers": {"filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp/x"]}}}
assert fc("/tmp/x") == want, f"filesystem_config('/tmp/x') returned {fc('/tmp/x')!r}, expected {want!r}."
