f = ns.get("run_batch")
assert f, "Define a function called run_batch."
def handle(text):
    if "bad" in text:
        raise ValueError("model timed out")
    return len(text)
out = f({"a": "hello", "b": "bad one", "c": "", "d": "  \n ", "e": "hi"}, handle)
assert isinstance(out, tuple) and len(out) == 2, "Return a pair: (results, errors)."
results, errors = out
assert results == {"a": 5, "e": 2}, f"results should be {{'a': 5, 'e': 2}}, got {results!r}."
assert errors == {"b": "model timed out"}, f"errors should hold the message as text, got {errors!r}."
calls = []
f({"x": " ", "y": ""}, lambda t: calls.append(t))
assert calls == [], "Don't call handle for empty files."
