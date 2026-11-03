f = ns.get("run_tool_calls")
assert f, "Keep the function run_tool_calls."
def call(i, name, args): return {"id": i, "type": "function", "function": {"name": name, "arguments": args}}
tools = {"echo": lambda word: word * 2}
got = f({"tool_calls": [call("a", "echo", '{"word": "ab"}')]}, tools)
assert got == [{"role": "tool", "tool_call_id": "a", "content": "abab"}], f"One echo call returned {got!r}, expected [{{'role': 'tool', 'tool_call_id': 'a', 'content': 'abab'}}]."
got = f({"tool_calls": [call("x", "nope", "{}")]}, tools)
assert got and got[0]["content"] == "error: unknown tool nope", f"An unknown tool gave {got!r}. Its content should be 'error: unknown tool nope'."
try:
    got = f({"tool_calls": [call("y", "echo", '{"word": ')]}, tools)
except ValueError:
    raise AssertionError("Broken JSON in the arguments crashed your function. Catch the ValueError.")
assert got[0]["content"] == "error: invalid arguments", f"Broken JSON gave {got!r}, expected content 'error: invalid arguments'."
got = f({"tool_calls": [call("1", "echo", '{"word": "x"}'), call("2", "echo", '{"word": "y"}')]}, tools)
assert [g["tool_call_id"] for g in got] == ["1", "2"] and [g["content"] for g in got] == ["xx", "yy"], "Keep one result per call, in the same order, each with its call's id."
assert tools["echo"](word=3) == 6
r = f({"tool_calls": [call("n", "echo", '{"word": 4}')]}, tools)
assert r[0]["content"] == "8", "content must be a string: use str(result)."
