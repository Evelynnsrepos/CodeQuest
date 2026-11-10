---
title: Workflows are JSON
minutes: 35
xp: 30
hint: Start with two lists: order = [] and queue = [start], then the loop: while len(queue) > 0:
hint: Inside the while: name = queue.pop(0), then if name in order: continue, then order.append(name)
hint: Still inside: outputs = workflow["connections"].get(name, {}).get("main", [])
hint: Then two loops inside each other: for output in outputs: and for target in output: and inside both: queue.append(target["node"]). At the end: return order
---
# Read a workflow like n8n does

⏱️ About 35 minutes · one function

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `queue = [start]` | "queue becomes a list with start in it" | a **to-do list** of nodes still to visit |
| `while len(queue) > 0:` | "while the queue isn't empty" | a **while loop**: repeats the lines under it as long as the condition is true. Here: as long as there's something on the to-do list. |
| `queue.pop(0)` | "queue pop zero" | takes the **first** thing off the list and gives it to you. The list gets one shorter. |
| `d.get(name, {})` | "d get name, else empty dictionary" | the value for `name`, or an empty dictionary if there is none |
| `.get(name, {}).get("main", [])` | | two lookups in a row: first the node, then its `"main"` part. If either is missing you get an empty list, so the loop below just does nothing. |
| `for output in outputs:` then `for target in output:` | "for each output, for each target in it" | a loop **inside** a loop: `outputs` is a list of lists |

### 👀 Worked example: who hears the news?

Ana tells Ben and Cleo. Ben tells Dan. In what order do people hear it, if each person passes it on in turn?

```python
def news_order(tells, first):
    order = []
    queue = [first]
    while len(queue) > 0:
        person = queue.pop(0)
        if person in order:
            continue
        order.append(person)
        for friend in tells.get(person, []):
            queue.append(friend)
    return order

print(news_order({"Ana": ["Ben", "Cleo"], "Ben": ["Dan"]}, "Ana"))
```

Watch the to-do list (`queue`) and the result (`order`):

| round | pop | queue after | order after |
|---|---|---|---|
| start | | `[Ana]` | `[]` |
| 1 | Ana | `[Ben, Cleo]` | `[Ana]` |
| 2 | Ben | `[Cleo, Dan]` | `[Ana, Ben]` |
| 3 | Cleo | `[Dan]` | `[Ana, Ben, Cleo]` |
| 4 | Dan | `[]` | `[Ana, Ben, Cleo, Dan]` |

The queue is empty, so the `while` stops. Everyone close to Ana comes before people further away: that's called **breadth-first**. If someone is told twice, the `if person in order: continue` skips the second time.

Your quest is this, with one difference: n8n's connections have **two** levels of lists (outputs, then targets), so you need two `for` loops.

## 🎯 Your quest

Write `run_order(workflow, start)`. Replace the starter's line with:

1. `order = []`
2. `queue = [start]`
3. `while len(queue) > 0:`
4. `    name = queue.pop(0)`
5. `    if name in order:`
6. `        continue`
7. `    order.append(name)`
8. `    outputs = workflow["connections"].get(name, {}).get("main", [])`
9. `    for output in outputs:`
10. `        for target in output:`
11. `            queue.append(target["node"])`
12. `return order`

## 🖥️ In n8n

Before importing a stranger's workflow, read its `nodes` list: look for HTTP Request nodes with unknown URLs and Code nodes. Keep your own workflows in a git repo (Git course!) as exported `.json` files.

**Remember:** nodes + connections, all plain JSON.

## Review

<details><summary>Lesson 3: what does $('Read Email').item.json.subject read?</summary>The subject from the earlier node called "Read Email", for the matching item.</details>
