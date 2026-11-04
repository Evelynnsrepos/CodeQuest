import time


def run_agent(task, model, tools, max_steps=5):
    trace = []
    for step in range(1, max_steps + 1):
        action = model(task, trace)
        if "answer" in action:
            trace.append({"step": step, "type": "answer", "name": None, "args": None,
                          "result": action["answer"], "error": None, "ms": 0.0})
            return action["answer"], trace
        name, args = action["tool"], action.get("args", {})
        start = time.perf_counter()
        result, error = None, None
        try:
            if name not in tools:
                raise KeyError(name)
            result = tools[name](**args)
        except Exception as e:
            error = f"{type(e).__name__}: {e.args[0] if isinstance(e, KeyError) else e}"
        trace.append({"step": step, "type": "tool", "name": name, "args": args, "result": result,
                      "error": error, "ms": (time.perf_counter() - start) * 1000})
    return None, trace


def failure_summary(traces):
    errors = {}
    for _, trace in traces:
        for span in trace:
            if span["type"] == "tool" and span["error"]:
                errors[span["name"]] = errors.get(span["name"], 0) + 1
    return {"runs": len(traces), "no_answer": sum(a is None for a, _ in traces), "tool_errors": errors}


def scripted_model(task, trace):
    if not trace:
        return {"tool": "search", "args": {"q": task}}
    return {"answer": "Use nix-collect-garbage -d [nix-gc]"}


tools = {"search": lambda q: ["nix-gc"]}
answer, trace = run_agent("free disk space on nixos", scripted_model, tools)
print(answer)
for span in trace:
    print(span)
