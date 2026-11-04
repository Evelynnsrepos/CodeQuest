import copy
f = ns.get("review")
assert f, "Keep the function review."
M = lambda n: {"node": n, "type": "main", "index": 0}
good = {
    "nodes": [
        {"name": "Every Morning", "type": "n8n-nodes-base.scheduleTrigger", "parameters": {}},
        {"name": "Agent", "type": "@n8n/n8n-nodes-langchain.agent", "parameters": {"text": "={{ $json.text }}"}},
        {"name": "Ollama", "type": "@n8n/n8n-nodes-langchain.lmChatOllama", "parameters": {}},
        {"name": "Send", "type": "n8n-nodes-base.telegram", "parameters": {}},
    ],
    "connections": {
        "Every Morning": {"main": [[M("Agent")]]},
        "Ollama": {"ai_languageModel": [[{"node": "Agent", "type": "ai_languageModel", "index": 0}]]},
        "Agent": {"main": [[M("Send")]]},
    },
    "settings": {"errorWorkflow": "42"},
}
assert f(good) == [], f"A good workflow has no problems, got {f(good)!r}."
w = copy.deepcopy(good); w["nodes"].append({"name": "Hook", "type": "n8n-nodes-base.webhook", "parameters": {}})
assert f(w) == ["needs exactly one trigger"], "Check 1: two triggers (the Webhook node, type ending in .webhook, is a trigger too)."
w = copy.deepcopy(good); w["nodes"][0]["type"] = "n8n-nodes-base.manualTRIGGER"
assert f(w) == [], "Check 1: 'Trigger' in any case counts."
w = copy.deepcopy(good); w["nodes"] = w["nodes"][1:]; w["connections"].pop("Every Morning")
assert f(w) == ["needs exactly one trigger"], "Check 1: no trigger."
w = copy.deepcopy(good); w["connections"]["Agent"]["main"][0].append(M("Ghost"))
assert f(w) == ["unknown node: Ghost"], "Check 2: a connection to a node that doesn't exist."
w = copy.deepcopy(good); w["connections"].pop("Ollama")
assert f(w) == ["Agent has no chat model"], "Check 3: an agent without ai_languageModel."
w = copy.deepcopy(good); w["settings"] = {}
assert f(w) == ["set an error workflow"], "Check 4."
w = copy.deepcopy(good); w.pop("settings")
assert f(w) == ["set an error workflow"], "Check 4: no settings at all."
w = copy.deepcopy(good); w["nodes"][3]["parameters"] = {"headers": {"Authorization": "Bearer abc"}}
assert f(w) == ["Send has a secret in it, use credentials"], "Check 5: Bearer token in parameters."
w = copy.deepcopy(good); w["nodes"][1]["parameters"]["key"] = "sk-123"
assert f(w) == ["Agent has a secret in it, use credentials"], "Check 5: an sk- key."
w = copy.deepcopy(good); w["settings"] = {}; w["connections"].pop("Ollama"); w["nodes"][3]["parameters"] = {"k": "sk-1"}
assert f(w) == ["Agent has no chat model", "set an error workflow", "Send has a secret in it, use credentials"], "All problems, in check order."
