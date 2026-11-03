d, t = ns.get("decide"), ns.get("trim_history")
assert d and t, "Keep decide and trim_history."
p = {"a": "allow", "b": "deny"}
assert d("a", p) == "allow" and d("b", p) == "deny", "decide should return the policy's entry."
assert d("zzz", p) == "ask", f"Unknown tools should give 'ask', got {d('zzz', p)!r}."
size = lambda m: m["n"]
roles = lambda ms: [m["role"] for m in ms]
msgs = [{"role": "system", "n": 5}, {"role": "user", "n": 10}, {"role": "assistant", "n": 2}, {"role": "tool", "n": 50},
        {"role": "user", "n": 3}]
orig = [dict(m) for m in msgs]
got = t(msgs, 70, size)
assert msgs == orig, "Don't change the input list."
assert len(got) == 5, "Total is exactly 70, which is within a budget of 70: nothing should be removed."
got = t(msgs, 69, size)
assert roles(got) == ["system", "assistant", "tool", "user"], f"Budget 69: dropping the oldest user message (10) is enough, got {roles(got)!r}."
got = t(msgs, 1, size)
assert roles(got) == ["system", "user"], f"Never delete the system prompt or the newest message, even if still over budget. Got {roles(got)!r}."
call = [{"role": "system", "n": 5}, {"role": "assistant", "n": 2}, {"role": "tool", "n": 50}, {"role": "user", "n": 10},
        {"role": "assistant", "n": 4}, {"role": "user", "n": 3}]
got = t(call, 73, size)
assert roles(got) == ["system", "user", "assistant", "user"], \
    f"Budget 73: dropping the tool call fits the budget, but its tool result must go with it. Got {roles(got)!r}."
