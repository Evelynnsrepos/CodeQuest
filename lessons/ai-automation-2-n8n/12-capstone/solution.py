import json


def review(workflow):
    problems = []
    nodes = workflow["nodes"]
    names = {n["name"] for n in nodes}
    connections = workflow.get("connections", {})

    triggers = [n for n in nodes if n["type"].lower().endswith("trigger") or n["type"].endswith(".webhook")]
    if len(triggers) != 1:
        problems.append("needs exactly one trigger")

    has_model = set()
    for source, outputs in connections.items():
        for kind, lists in outputs.items():
            for targets in lists:
                for t in targets:
                    if t["node"] not in names:
                        problems.append(f"unknown node: {t['node']}")
                    if kind == "ai_languageModel":
                        has_model.add(t["node"])

    for n in nodes:
        if n["type"].endswith(".agent") and n["name"] not in has_model:
            problems.append(f"{n['name']} has no chat model")

    if not workflow.get("settings", {}).get("errorWorkflow"):
        problems.append("set an error workflow")

    for n in nodes:
        text = json.dumps(n.get("parameters", {}))
        if "sk-" in text or "Bearer " in text:
            problems.append(f"{n['name']} has a secret in it, use credentials")
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
