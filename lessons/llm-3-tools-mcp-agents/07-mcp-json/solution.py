import json


def stdio_server(command, args, env=None):
    entry = {"command": command, "args": args}
    if env is not None:
        entry["env"] = env
    return entry


def http_server(url, token=None):
    entry = {"url": url}
    if token is not None:
        entry["headers"] = {"Authorization": "Bearer " + token}
    return entry


def filesystem_config(folder):
    server = stdio_server("npx", ["-y", "@modelcontextprotocol/server-filesystem", folder])
    return {"mcpServers": {"filesystem": server}}


print(json.dumps(filesystem_config("/home/evilynn/notes"), indent=2))
print(json.dumps(http_server("https://example.com/mcp", "abc123")))
