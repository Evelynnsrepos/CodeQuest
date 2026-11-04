import json


def review(workflow):
    problems = []
    # 1. one trigger  2. real nodes  3. agents have a model  4. error workflow  5. no secrets
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
