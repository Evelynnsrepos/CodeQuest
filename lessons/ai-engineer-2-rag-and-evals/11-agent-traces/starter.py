import time


def run_agent(task, model, tools, max_steps=5):
    # trace = []
    # for step in range(1, max_steps + 1):
    #     action = model(task, trace)
    #     if "answer" in action:
    #         span = {"step": step, "type": "answer", "name": None, "args": None, "result": action["answer"], "error": None, "ms": 0.0}
    #         trace.append(span)
    #         return action["answer"], trace
    #     name = action["tool"]
    #     args = action.get("args", {})
    #     start = time.perf_counter()
    #     result = None
    #     error = None
    #     try:
    #         if name not in tools:
    #             raise KeyError(name)
    #         result = tools[name](**args)
    #     except KeyError as e:
    #         error = type(e).__name__ + ": " + str(e.args[0])
    #     except Exception as e:
    #         error = type(e).__name__ + ": " + str(e)
    #     ms = (time.perf_counter() - start) * 1000
    #     span = {"step": step, "type": "tool", "name": name, "args": args, "result": result, "error": error, "ms": ms}
    #     trace.append(span)
    # return None, trace
    return None, []


def failure_summary(traces):
    # errors = {}
    # no_answer = 0
    # for answer, trace in traces:
    #     if answer is None:
    #         no_answer = no_answer + 1
    #     for span in trace:
    #         if span["type"] == "tool" and span["error"]:
    #             errors[span["name"]] = errors.get(span["name"], 0) + 1
    # return {"runs": len(traces), "no_answer": no_answer, "tool_errors": errors}
    return {"runs": 0, "no_answer": 0, "tool_errors": {}}


def scripted_model(task, trace):
    if not trace:
        return {"tool": "search", "args": {"q": task}}
    return {"answer": "Use nix-collect-garbage -d [nix-gc]"}


def search(q):
    return ["nix-gc"]


tools = {"search": search}
answer, trace = run_agent("free disk space on nixos", scripted_model, tools)
print(answer)
for span in trace:
    print(span)
