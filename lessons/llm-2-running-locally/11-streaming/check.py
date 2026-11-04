f = ns.get("collect_stream")
assert f, "Keep the function collect_stream."
raw = ': keep-alive comment\n\ndata: {"choices": [{"delta": {"role": "assistant"}}]}\n\ndata: {"choices": [{"delta": {"content": "A"}}]}\n\ndata: {"choices": [{"delta": {"content": "B"}}]}\n\ndata: [DONE]\n\ndata: {"choices": [{"delta": {"content": "X"}}]}\n'
try:
    got = f(raw)
except KeyError:
    raise AssertionError("A delta without 'content' crashed your code. Use delta.get('content', '').")
except ValueError:
    raise AssertionError("Your code tried to parse something that isn't JSON. Skip lines without 'data: ' and stop at [DONE].")
assert got == "AB", f"collect_stream returned {got!r}, expected 'AB'. Ignore other lines and stop at [DONE]."
