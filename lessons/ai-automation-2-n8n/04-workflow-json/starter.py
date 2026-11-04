def run_order(workflow, start):
    return [start]


wf = {
    "nodes": [{"name": n} for n in ["Every Morning", "Summarize", "Send", "Log"]],
    "connections": {
        "Every Morning": {"main": [[{"node": "Summarize", "type": "main", "index": 0}]]},
        "Summarize": {"main": [[{"node": "Send", "type": "main", "index": 0}, {"node": "Log", "type": "main", "index": 0}]]},
    },
}
print(run_order(wf, "Every Morning"))
