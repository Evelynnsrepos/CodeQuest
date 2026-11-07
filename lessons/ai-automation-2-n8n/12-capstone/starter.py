import json


def review(workflow):
    problems = []
    # setup:   nodes = workflow["nodes"]   and   connections = workflow.get("connections", {})
    # check 1: names = [], triggers = 0, loop over nodes: collect names, count triggers
    # check 2: has_model = [], the four loops from lesson 7: unknown nodes, and who gets an ai_languageModel
    # check 3: loop over nodes: agents not in has_model
    # check 4: settings = workflow.get("settings", {}), errorWorkflow empty?
    # check 5: loop over nodes: "sk-" or "Bearer " in json.dumps(node.get("parameters", {}))
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
