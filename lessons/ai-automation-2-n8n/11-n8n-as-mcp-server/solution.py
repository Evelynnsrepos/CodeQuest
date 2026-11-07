def mcp_entry(name, url, token):
    entry = {}
    entry["command"] = "npx"
    entry["args"] = ["mcp-remote", url, "--header", "Authorization: Bearer ${AUTH_TOKEN}"]
    entry["env"] = {"AUTH_TOKEN": token}
    return {"mcpServers": {name: entry}}


print(mcp_entry("shopping", "https://n8n.local/mcp/abc123", "secret-token"))
