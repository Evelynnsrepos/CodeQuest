def mcp_entry(name, url, token):
    return {"mcpServers": {name: {
        "command": "npx",
        "args": ["mcp-remote", url, "--header", "Authorization: Bearer ${AUTH_TOKEN}"],
        "env": {"AUTH_TOKEN": token},
    }}}


print(mcp_entry("shopping", "https://n8n.local/mcp/abc123", "secret-token"))
