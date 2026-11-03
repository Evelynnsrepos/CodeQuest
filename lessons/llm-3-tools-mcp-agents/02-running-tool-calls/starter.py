import json


def add(a, b):
    return a + b


def shout(text):
    return text.upper() + "!"


TOOLS = {"add": add, "shout": shout}


def run_tool_calls(message, tools):
    results = []
    for call in message["tool_calls"]:
        pass
    return results


message = {"role": "assistant", "content": None, "tool_calls": [
    {"id": "call_1", "type": "function", "function": {"name": "add", "arguments": '{"a": 2, "b": 40}'}},
    {"id": "call_2", "type": "function", "function": {"name": "shout", "arguments": '{"text": "hallo"}'}},
    {"id": "call_3", "type": "function", "function": {"name": "multiply", "arguments": '{"a": 2}'}},
]}
for result in run_tool_calls(message, TOOLS):
    print(result)
