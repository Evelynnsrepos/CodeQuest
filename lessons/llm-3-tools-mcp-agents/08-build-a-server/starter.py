import json

NOTES = {"todo.md": "- learn MCP\n- write mcp.json", "ideas.md": "fine-tune a pirate model"}

TOOLS = [
    {"name": "list_notes", "description": "List all note files.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "read_note", "description": "Read one note by file name.",
     "inputSchema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
]


def list_notes():
    return "\n".join(sorted(NOTES))


def read_note(name):
    return NOTES[name]  # raises KeyError for unknown names


IMPLEMENTATIONS = {"list_notes": list_notes, "read_note": read_note}


def ok(id, result):
    return {"jsonrpc": "2.0", "id": id, "result": result}


def fail(id, code, message):
    return {"jsonrpc": "2.0", "id": id, "error": {"code": code, "message": message}}


def text_result(text, is_error=False):
    return {"content": [{"type": "text", "text": text}], "isError": is_error}


def handle(message):
    return None


for msg in [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "read_note", "arguments": {"name": "todo.md"}}},
    {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "read_note", "arguments": {"name": "secret.md"}}},
    {"jsonrpc": "2.0", "id": 5, "method": "resources/list"},
]:
    print(json.dumps(handle(msg)))
