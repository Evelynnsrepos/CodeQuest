import json


def review(workflow):
    problems = []
    nodes = workflow["nodes"]
    connections = workflow.get("connections", {})

    names = []
    triggers = 0
    for node in nodes:
        names.append(node["name"])
        if node["type"].lower().endswith("trigger") or node["type"].endswith(".webhook"):
            triggers = triggers + 1
    if triggers != 1:
        problems.append("needs exactly one trigger")

    has_model = []
    for source in connections:
        outputs = connections[source]
        for kind in outputs:
            for targets in outputs[kind]:
                for target in targets:
                    if target["node"] not in names:
                        problems.append("unknown node: " + target["node"])
                    if kind == "ai_languageModel":
                        has_model.append(target["node"])

    for node in nodes:
        if node["type"].endswith(".agent") and node["name"] not in has_model:
            problems.append(node["name"] + " has no chat model")

    settings = workflow.get("settings", {})
    if settings.get("errorWorkflow", "") == "":
        problems.append("set an error workflow")

    for node in nodes:
        text = json.dumps(node.get("parameters", {}))
        if "sk-" in text or "Bearer " in text:
            problems.append(node["name"] + " has a secret in it, use credentials")
    return problems


wf = {
    "nodes": [
        {"name": "Every Morning", "type": "n8n-nodes-base.scheduleTrigger", "parameters": {}},
        {"name": "Sort Mail", "type": "@n8n/n8n-nodes-langchain.agent", "parameters": {}},
        {"name": "LM Studio", "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi", "parameters": {}},
        {"name": "Notify", "type": "n8n-nodes-base.httpRequest", "parameters": {"headers": "Bearer abc123"}},
    ],
    "connections": {
        "Every Morning": {"main": [[{"node": "Sort Mail", "type": "main", "index": 0}]]},
        "Sort Mail": {"main": [[{"node": "Notify", "type": "main", "index": 0}]]},
    },
    "settings": {},
}
print(review(wf))
