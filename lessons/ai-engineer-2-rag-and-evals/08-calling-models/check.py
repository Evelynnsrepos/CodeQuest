import json
import httpx
chat = ns.get("chat")
assert chat, "Keep chat."
OK = {"choices": [{"message": {"content": "Hallo!"}}], "usage": {"prompt_tokens": 9, "completion_tokens": 2}}
def scripted(responses):
    calls = []
    def handler(request):
        calls.append(json.loads(request.content))
        r = responses[min(len(calls) - 1, len(responses) - 1)]
        if r == "timeout":
            raise httpx.ReadTimeout("slow", request=request)
        return r
    return httpx.Client(transport=httpx.MockTransport(handler)), calls
msgs = [{"role": "user", "content": "Hi"}]
c, calls = scripted([httpx.Response(200, json=OK)])
assert chat(msgs, "m", "http://x/v1", c) == ("Hallo!", OK["usage"]), "Return (content, usage)."
assert calls[0] == {"model": "m", "messages": msgs, "temperature": 0}, f"Send model, messages and temperature 0. Got {calls[0]!r}."
slept = []
c, calls = scripted([httpx.Response(503), "timeout", httpx.Response(200, json=OK)])
assert chat(msgs, "m", "http://x/v1", c, sleep=slept.append)[0] == "Hallo!" and slept == [1, 2], f"Retry 503 and timeouts, waiting 1 then 2. Slept {slept}."
slept = []
c, calls = scripted([httpx.Response(429, headers={"Retry-After": "7"}), httpx.Response(200, json=OK)])
chat(msgs, "m", "http://x/v1", c, sleep=slept.append)
assert slept == [7.0], f"Use the Retry-After header when present. Slept {slept}."
slept = []
c, calls = scripted([httpx.Response(500)])
try:
    chat(msgs, "m", "http://x/v1", c, retries=3, sleep=slept.append)
    raise AssertionError("After all retries fail, raise RuntimeError.")
except RuntimeError:
    pass
assert len(calls) == 4 and slept == [1, 2, 4], f"retries=3 means 4 attempts and waits 1, 2, 4. Got {len(calls)} calls, slept {slept}."
c, calls = scripted([httpx.Response(401)])
try:
    chat(msgs, "m", "http://x/v1", c, sleep=slept.append)
    raise AssertionError("401 should raise immediately.")
except httpx.HTTPStatusError:
    pass
assert len(calls) == 1, "Don't retry a 401: the request itself is wrong."
