import json
b, p = ns.get("build_request"), ns.get("parse_reply")
assert b and p, "Keep build_request and parse_reply."
msgs = [{"role": "system", "content": "Be brief."}, {"role": "user", "content": "Hi"}]
got = b("llama-3.1-8b-instruct", msgs, 0.2, 50)
want = {"model": "llama-3.1-8b-instruct", "messages": msgs, "temperature": 0.2, "max_tokens": 50}
assert got == want, f"build_request returned {got!r}, expected {want!r}."
reply = {"choices": [{"index": 0, "message": {"role": "assistant", "content": "Servus"}, "finish_reason": "length"}],
         "usage": {"prompt_tokens": 5, "completion_tokens": 50, "total_tokens": 55}}
got = p(json.dumps(reply))
assert tuple(got) == ("Servus", "length", 55), f"parse_reply returned {got!r}, expected ('Servus', 'length', 55)."
