import json


def stdio_server(command, args, env=None):
    return {}


def http_server(url, token=None):
    return {}


def filesystem_config(folder):
    return {}


print(json.dumps(filesystem_config("/home/evilynn/notes"), indent=2))
print(json.dumps(http_server("https://example.com/mcp", "abc123")))
