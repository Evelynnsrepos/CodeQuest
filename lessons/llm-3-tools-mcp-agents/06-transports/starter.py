import json


def read_stdio(raw):
    responses = {}
    notifications = []
    bad_lines = 0
    # for line in raw.splitlines():
    #     if line.strip() == "":
    #         continue
    #     try:
    #         message = json.loads(line)
    #     except ValueError:
    #         bad_lines = bad_lines + 1
    #         continue
    #     if "id" in message:
    #         responses[message["id"]] = message
    #     else:
    #         notifications.append(message["method"])
    return responses, notifications, bad_lines


stdout = """{"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2025-06-18", "capabilities": {"tools": {}}}}
Server started, watching /home/evilynn/notes
{"jsonrpc": "2.0", "method": "notifications/tools/list_changed"}

{"jsonrpc": "2.0", "id": 2, "result": {"tools": [{"name": "read_text_file"}]}}
"""
responses, notifications, bad = read_stdio(stdout)
print("responses for ids:", sorted(responses))
print("notifications:", notifications)
print("bad lines:", bad)
