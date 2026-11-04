f = ns.get("agent_parts")
assert f, "Define a function called agent_parts."
L = lambda kind, target: {kind: [[{"node": target, "type": kind, "index": 0}]]}
wf = {"connections": {
    "Trigger": {"main": [[{"node": "Agent A", "type": "main", "index": 0}]]},
    "LM Studio": L("ai_languageModel", "Agent A"),
    "Search": L("ai_tool", "Agent A"),
    "Calculator": L("ai_tool", "Agent A"),
    "Memory": L("ai_memory", "Agent A"),
    "Ollama": L("ai_languageModel", "Agent B"),
    "Files": L("ai_tool", "Agent B"),
}}
assert f(wf, "Agent A") == {"model": "LM Studio", "tools": ["Calculator", "Search"], "memory": "Memory"}, f"Agent A: got {f(wf, 'Agent A')!r}."
assert f(wf, "Agent B") == {"model": "Ollama", "tools": ["Files"], "memory": None}, "Only count sub-nodes plugged into this agent."
assert f(wf, "Nobody") == {"model": None, "tools": [], "memory": None}, "An agent with nothing plugged in."
assert f(wf, "Agent A")["model"] != "Trigger", "A main connection is not a model."
