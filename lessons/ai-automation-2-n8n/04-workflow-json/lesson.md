---
title: Workflows are JSON
xp: 30
---
# Read a workflow like n8n does

⏱️ About 12 minutes · one function

> **Warm-up:** you find a cool workflow online as a `.json` file. Before you import it, how can you see what it does and where it sends data?

**In one sentence:** every n8n workflow is a JSON file with a list of `nodes` and a `connections` map, so you can read, check, version in git and share it.

## 🪜 Plain words

Select nodes and press Ctrl+C in n8n, and you get JSON like this (shortened):

```json
{
  "nodes": [
    {"name": "Every Morning", "type": "n8n-nodes-base.scheduleTrigger", "parameters": {}},
    {"name": "Summarize", "type": "@n8n/n8n-nodes-langchain.agent", "parameters": {}},
    {"name": "Send", "type": "n8n-nodes-base.telegram", "parameters": {}}
  ],
  "connections": {
    "Every Morning": {"main": [[{"node": "Summarize", "type": "main", "index": 0}]]},
    "Summarize": {"main": [[{"node": "Send", "type": "main", "index": 0}]]}
  }
}
```

`connections[source]["main"]` is a list of **outputs** (an IF node has two: true and false), and each output is a list of targets. Paste JSON into the canvas with Ctrl+V to import it.

## 🎯 Your quest

Write `run_order(workflow, start)`: starting at the node named `start`, follow `main` connections and return the node names in the order they're first reached (breadth-first: all direct next nodes before their next nodes). Each name appears once.

<details><summary>💡 Hint</summary>
<pre>order, queue = [], [start]
while queue:
    name = queue.pop(0)
    if name in order:
        continue
    order.append(name)
    for output in workflow["connections"].get(name, {}).get("main", []):
        for target in output:
            queue.append(target["node"])
return order</pre>
</details>

## 🖥️ In n8n

Before importing a stranger's workflow, read its `nodes` list: look for HTTP Request nodes with unknown URLs and Code nodes. Keep your own workflows in a git repo (Git course!) as exported `.json` files.

**Remember:** nodes + connections, all plain JSON.

## Review

<details><summary>Lesson 3: what does $('Read Email').item.json.subject read?</summary>The subject from the earlier node called "Read Email", for the matching item.</details>
