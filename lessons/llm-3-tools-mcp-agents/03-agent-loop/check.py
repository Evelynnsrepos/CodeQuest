f = ns.get("run_agent")
assert f, "Keep the function run_agent."
tc, sm, T = ns["tool_call"], ns["scripted_model"], ns["TOOLS"]
import io, contextlib
msgs = [{"role": "user", "content": "hi"}]
with contextlib.redirect_stdout(io.StringIO()):
    got = f(msgs, sm([tc("a", "list_files", {}), {"role": "assistant", "content": "done"}]), T, 5)
assert got == "done", f"run_agent returned {got!r}, expected the final answer 'done'."
assert len(msgs) == 4, f"After one tool round the history should have 4 messages (user, call, tool result, answer), it has {len(msgs)}."
assert msgs[2]["role"] == "tool" and msgs[2]["tool_call_id"] == "a", "The tool result should come right after the tool call in messages."
loop = [tc(str(i), "list_files", {}) for i in range(10)]
with contextlib.redirect_stdout(io.StringIO()):
    try:
        got = f([{"role": "user", "content": "x"}], sm(loop), T, 3)
    except StopIteration:
        raise AssertionError("run_agent kept calling the model. Stop after max_steps rounds.")
assert got == "stopped: too many steps", f"A model that never stops calling tools should give 'stopped: too many steps' after max_steps, got {got!r}."
