def error_alert(data):
    return "❌ something failed"


data = {
    "execution": {"id": "231", "url": "https://n8n.example.com/execution/231",
                  "lastNodeExecuted": "Ollama Chat Model", "error": {"message": "connect ECONNREFUSED"}},
    "workflow": {"id": "1", "name": "Morning summary"},
}
print(error_alert(data))
