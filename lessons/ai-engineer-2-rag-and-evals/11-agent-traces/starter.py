import time


def run_agent(task, model, tools, max_steps=5):
    return None, []


def failure_summary(traces):
    return {"runs": 0, "no_answer": 0, "tool_errors": {}}


def scripted_model(task, trace):
    if not trace:
        return {"tool": "search", "args": {"q": task}}
    return {"answer": "Use nix-collect-garbage -d [nix-gc]"}


tools = {"search": lambda q: ["nix-gc"]}
answer, trace = run_agent("free disk space on nixos", scripted_model, tools)
print(answer)
for span in trace:
    print(span)
