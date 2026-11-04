def agent_parts(workflow, agent):
    return {"model": None, "tools": [], "memory": None}


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
