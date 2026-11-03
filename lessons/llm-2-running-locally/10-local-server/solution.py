import json


def build_request(model, messages, temperature, max_tokens):
    return {"model": model, "messages": messages, "temperature": temperature, "max_tokens": max_tokens}


def parse_reply(text):
    data = json.loads(text)
    choice = data["choices"][0]
    return choice["message"]["content"], choice["finish_reason"], data["usage"]["total_tokens"]


request = build_request("qwen3-8b", [{"role": "user", "content": "Say hi in German."}], 0.7, 100)
print(json.dumps(request))

recorded = """{"id": "chatcmpl-123", "object": "chat.completion", "model": "qwen3-8b",
 "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hallo!"}, "finish_reason": "stop"}],
 "usage": {"prompt_tokens": 14, "completion_tokens": 3, "total_tokens": 17}}"""
print(parse_reply(recorded))
