def error_alert(data):
    name = data["workflow"]["name"]
    ex = data.get("execution")
    if not ex:
        return f"❌ {name} failed at its trigger: {data['trigger']['error']['message']}"
    text = f"❌ {name} failed at {ex['lastNodeExecuted']}: {ex['error']['message']}"
    url = ex.get("url")
    if url:
        text += "\n" + url
    return text


data = {
    "execution": {"id": "231", "url": "https://n8n.example.com/execution/231",
                  "lastNodeExecuted": "Ollama Chat Model", "error": {"message": "connect ECONNREFUSED"}},
    "workflow": {"id": "1", "name": "Morning summary"},
}
print(error_alert(data))
