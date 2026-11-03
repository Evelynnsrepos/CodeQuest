import json
a2c, tj, vl = ns.get("alpaca_to_chat"), ns.get("to_jsonl"), ns.get("validate_line")
assert a2c and tj and vl, "Keep alpaca_to_chat, to_jsonl and validate_line."
got = a2c({"instruction": "Translate.", "input": "Hund", "output": "dog"})
want = {"messages": [{"role": "user", "content": "Translate.\n\nHund"}, {"role": "assistant", "content": "dog"}]}
assert got == want, f"alpaca_to_chat without a system prompt returned {got!r}, expected {want!r}."
got = a2c({"instruction": "Hi.", "input": "", "output": "Hello"}, "Be nice.")
want = {"messages": [{"role": "system", "content": "Be nice."}, {"role": "user", "content": "Hi."}, {"role": "assistant", "content": "Hello"}]}
assert got == want, f"With an empty input and a system prompt, got {got!r}, expected {want!r}."
out = tj([{"a": 1}, {"b": [2, 3]}])
assert out.splitlines() == ['{"a": 1}', '{"b": [2, 3]}'], f"to_jsonl should give one JSON object per line, got {out!r}."
good = json.dumps({"messages": [{"role": "user", "content": "x"}, {"role": "assistant", "content": "y"}]})
assert vl(good) is None, f"validate_line rejected a valid example: {vl(good)!r}."
bad = ["{oops", json.dumps({"messages": [{"role": "user", "content": "x"}]}),
       json.dumps({"messages": [{"role": "user", "content": "x"}, {"role": "bot", "content": "y"}]}),
       json.dumps({"messages": [{"role": "user", "content": ""}, {"role": "assistant", "content": "y"}]}),
       json.dumps({"messages": [{"role": "assistant", "content": "x"}, {"role": "user", "content": "y"}]}),
       json.dumps({"text": "plain"})]
for line in bad:
    try:
        r = vl(line)
    except Exception as e:
        raise AssertionError(f"validate_line crashed on {line!r}: {e!r}. Return an error text instead.")
    assert isinstance(r, str) and r, f"validate_line({line!r}) should return an error text, got {r!r}."
