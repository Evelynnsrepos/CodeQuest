import json


def build_request(model, messages, temperature, max_tokens):
    request = {}
    request["model"] = model
    request["messages"] = messages
    request["temperature"] = temperature
    request["max_tokens"] = max_tokens
    return request


def parse_reply(text):
    data = json.loads(text)
    choice = data["choices"][0]
    content = choice["message"]["content"]
    reason = choice["finish_reason"]
    tokens = data["usage"]["total_tokens"]
    return content, reason, tokens


request = build_request("qwen3-8b", [{"role": "user", "content": "Say hi in German."}], 0.7, 100)
print(json.dumps(request))

recorded = """{"id": "chatcmpl-123", "object": "chat.completion", "model": "qwen3-8b",
 "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hallo!"}, "finish_reason": "stop"}],
 "usage": {"prompt_tokens": 14, "completion_tokens": 3, "total_tokens": 17}}"""
print(parse_reply(recorded))
