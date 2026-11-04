def run_order(workflow, start):
    order, queue = [], [start]
    while queue:
        name = queue.pop(0)
        if name in order:
            continue
        order.append(name)
        for output in workflow["connections"].get(name, {}).get("main", []):
            for target in output:
                queue.append(target["node"])
    return order


wf = {
    "nodes": [{"name": n} for n in ["Every Morning", "Summarize", "Send", "Log"]],
    "connections": {
        "Every Morning": {"main": [[{"node": "Summarize", "type": "main", "index": 0}]]},
        "Summarize": {"main": [[{"node": "Send", "type": "main", "index": 0}, {"node": "Log", "type": "main", "index": 0}]]},
    },
}
print(run_order(wf, "Every Morning"))
