import io, json, urllib.request
ask = ns.get("ask")
assert ask, "Keep the function ask."
assert ns.get("RUN_FOR_REAL") is False, "Leave RUN_FOR_REAL = False inside CodeQuest."
seen = {}
class FakeResponse(io.BytesIO):
    def __enter__(self): return self
    def __exit__(self, *a): return False
def fake_urlopen(req, *args, **kwargs):
    seen["url"] = req.full_url if hasattr(req, "full_url") else req
    seen["method"] = req.get_method() if hasattr(req, "get_method") else None
    seen["headers"] = {k.lower(): v for k, v in req.header_items()} if hasattr(req, "header_items") else {}
    seen["body"] = req.data
    reply = {"choices": [{"index": 0, "message": {"role": "assistant", "content": "A cache of keys and values."}, "finish_reason": "stop"}],
             "usage": {"prompt_tokens": 20, "completion_tokens": 7, "total_tokens": 27}}
    return FakeResponse(json.dumps(reply).encode("utf-8"))
original = urllib.request.urlopen
urllib.request.urlopen = fake_urlopen
try:
    answer = ask("What is a KV cache?", model="qwen3-8b", base_url="http://127.0.0.1:5555/v1")
finally:
    urllib.request.urlopen = original
assert seen, "ask never called urllib.request.urlopen. Call it as urllib.request.urlopen(req)."
assert seen["url"] == "http://127.0.0.1:5555/v1/chat/completions", f"You sent the request to {seen['url']!r}; it should go to base_url + '/chat/completions'."
assert seen["method"] == "POST", "The request should be a POST: pass the body as data= to urllib.request.Request."
assert seen["headers"].get("content-type") == "application/json", "Set the header Content-Type: application/json."
assert isinstance(seen["body"], bytes), "The body must be bytes: json.dumps(...).encode('utf-8')."
body = json.loads(seen["body"])
assert body.get("model") == "qwen3-8b", f"The body's model is {body.get('model')!r}; use the model argument."
msgs = body.get("messages")
assert msgs == [{"role": "system", "content": "Answer briefly."}, {"role": "user", "content": "What is a KV cache?"}], f"messages should be the system message and the user's question, got {msgs!r}."
assert body.get("temperature") == 0.2 and body.get("max_tokens") == 300, "Send temperature 0.2 and max_tokens 300."
assert answer == "A cache of keys and values.", f"ask returned {answer!r}; return choices[0]['message']['content'] from the response."
