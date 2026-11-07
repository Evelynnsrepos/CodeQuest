def run_order(workflow, start):
    # order = []
    # queue = [start]
    # while len(queue) > 0:
    #     name = queue.pop(0)
    #     if name in order:
    #         continue
    #     order.append(name)
    #     outputs = workflow["connections"].get(name, {}).get("main", [])
    #     for output in outputs:
    #         for target in output:
    #             queue.append(target["node"])
    # return order
    return [start]


wf = {
    "nodes": [{"name": "Every Morning"}, {"name": "Summarize"}, {"name": "Send"}, {"name": "Log"}],
    "connections": {
        "Every Morning": {"main": [[{"node": "Summarize", "type": "main", "index": 0}]]},
        "Summarize": {"main": [[{"node": "Send", "type": "main", "index": 0}, {"node": "Log", "type": "main", "index": 0}]]},
    },
}
print(run_order(wf, "Every Morning"))
