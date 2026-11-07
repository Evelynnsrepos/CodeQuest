def error_alert(data):
    name = data["workflow"]["name"]
    if "execution" not in data:
        return "❌ " + name + " failed at its trigger: " + data["trigger"]["error"]["message"]
    ex = data["execution"]
    text = "❌ " + name + " failed at " + ex["lastNodeExecuted"] + ": " + ex["error"]["message"]
    if "url" in ex:
        text = text + "\n" + ex["url"]
    return text


data = {
    "execution": {"id": "231", "url": "https://n8n.example.com/execution/231",
                  "lastNodeExecuted": "Ollama Chat Model", "error": {"message": "connect ECONNREFUSED"}},
    "workflow": {"id": "1", "name": "Morning summary"},
}
print(error_alert(data))
