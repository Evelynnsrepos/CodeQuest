import json


def request(id, method, params=None):
    return {}


def notification(method):
    return {}


def tool_call_request(id, name, arguments):
    return {}


def text_of(response):
    return ""


print(json.dumps(request(1, "initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                           "clientInfo": {"name": "codequest", "version": "1"}})))
print(json.dumps(notification("notifications/initialized")))
print(json.dumps(request(2, "tools/list")))
print(json.dumps(tool_call_request(3, "read_text_file", {"path": "/home/evilynn/notes/todo.md"})))
reply = {"jsonrpc": "2.0", "id": 3, "result": {"content": [{"type": "text", "text": "- learn MCP"},
                                                           {"type": "text", "text": "- write mcp.json"}], "isError": False}}
print(text_of(reply))
