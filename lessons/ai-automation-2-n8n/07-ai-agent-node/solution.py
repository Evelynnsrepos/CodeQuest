def agent_parts(workflow, agent):
    parts = {"model": None, "tools": [], "memory": None}
    for source, outputs in workflow["connections"].items():
        for kind, lists in outputs.items():
            for targets in lists:
                for t in targets:
                    if t["node"] != agent:
                        continue
                    if kind == "ai_languageModel":
                        parts["model"] = source
                    elif kind == "ai_tool":
                        parts["tools"].append(source)
                    elif kind == "ai_memory":
                        parts["memory"] = source
    parts["tools"].sort()
    return parts


def link(kind, target):
    return {kind: [[{"node": target, "type": kind, "index": 0}]]}


wf = {"connections": {
    "Chat Trigger": {"main": [[{"node": "AI Agent", "type": "main", "index": 0}]]},
    "Ollama Chat Model": link("ai_languageModel", "AI Agent"),
    "Calculator": link("ai_tool", "AI Agent"),
    "Weather API": link("ai_tool", "AI Agent"),
    "Simple Memory": link("ai_memory", "AI Agent"),
}}
print(agent_parts(wf, "AI Agent"))
