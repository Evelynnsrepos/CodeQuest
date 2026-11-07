---
title: The AI Agent node
minutes: 40
xp: 30
hint: Start with parts = {"model": None, "tools": [], "memory": None}, then for source in connections: and inside it outputs = connections[source]
hint: Two more loops: for kind in outputs: and for targets in outputs[kind]: and for target in targets: and then if target["node"] == agent:
hint: Inside that if: if kind == "ai_languageModel": parts["model"] = source, elif kind == "ai_tool": parts["tools"].append(source), elif kind == "ai_memory": parts["memory"] = source
hint: After all the loops (4 spaces): parts["tools"].sort() and return parts
---
# A model, tools and memory plugged into one node

⏱️ About 40 minutes · one function with loops inside loops

> **Warm-up:** in AI automation 1 you wrote the agent loop yourself. In n8n you drag in an AI Agent node. Where did the loop go?

**In one sentence:** the **AI Agent** node runs the agent loop for you; you plug **sub-nodes** into it: exactly one chat **model**, any number of **tools**, and optionally a **memory**.

## 🪜 Plain words

Under the Agent node on the canvas are little sockets:

| Socket | Plug in | Connection type in the JSON |
|---|---|---|
| Chat Model | Ollama Chat Model, OpenAI Chat Model (LM Studio) | `ai_languageModel` |
| Tool | Calculator, HTTP Request Tool, Call n8n Workflow Tool, MCP Client Tool… | `ai_tool` |
| Memory | Simple Memory (remembers the chat) | `ai_memory` |

In the workflow JSON, the **sub-node** is the source: `"Ollama Chat Model": {"ai_languageModel": [[{"node": "AI Agent", "type": "ai_languageModel", "index": 0}]]}`.

**For local models:** pick a model trained for tool calling (for example Qwen or Llama instruct models; the model card says "tools"). Small models get confused by many tools, so give the agent **2 to 4** tools with clear descriptions. Each tool's description is what the model reads to decide when to use it.

## 🐍 Python you need

The tricky part is how deep the connections are packed. Here's one sub-node, unpacked layer by layer:

```python
connections = {
    "Calculator": {                      # source: the sub-node's name
        "ai_tool": [                     # kind: what sort of plug
            [                            # one output (a list of targets)
                {"node": "AI Agent", "type": "ai_tool", "index": 0}   # one target
            ]
        ]
    }
}
```

So it's: dictionary → dictionary → list → list → dictionary. Each layer needs its own loop.

| You write | Say it | What it does |
|---|---|---|
| `for source in connections:` | "for each source" | the dictionary's keys: node names like `"Calculator"` |
| `outputs = connections[source]` | | that node's dictionary, like `{"ai_tool": [[...]]}` |
| `for kind in outputs:` | "for each kind" | its keys: `"main"`, `"ai_tool"`, … |
| `for targets in outputs[kind]:` | "for each list of targets" | the outer list |
| `for target in targets:` | "for each target" | the inner list: one `{"node": ..., ...}` at a time |
| `target["node"] == agent` | | is this plug going into **our** agent? |
| `parts["tools"].sort()` | "sort the tools" | puts that list in alphabetical order (it changes the list itself) |

### 👀 Worked example: who brings what to the party

Same layers, smaller: dictionary → list → dictionary.

```python
bring = {
    "Ana": [{"to": "Party", "what": "cake"}],
    "Ben": [{"to": "Picnic", "what": "juice"}, {"to": "Party", "what": "music"}],
}

def for_party(bring, party):
    found = {"cake": None, "music": None}
    for person in bring:
        for promise in bring[person]:
            if promise["to"] == party:
                if promise["what"] == "cake":
                    found["cake"] = person
                elif promise["what"] == "music":
                    found["music"] = person
    return found

print(for_party(bring, "Party"))
```

1. `person` = `"Ana"`: one promise, to `"Party"`, `"cake"` → `found["cake"]` = `"Ana"`.
2. `person` = `"Ben"`: first promise is to `"Picnic"`, not our party, skip. Second is to `"Party"`, `"music"` → `found["music"]` = `"Ben"`.
3. Returns `{"cake": "Ana", "music": "Ben"}`.

Your quest has two more layers, but each loop does the same thing: go one layer deeper.

## 🎯 Your quest

Write `agent_parts(workflow, agent)`. It returns `{"model": name or None, "tools": [sorted names], "memory": name or None}`. Replace the starter's line with (count the spaces: each loop adds 4):

1. `parts = {"model": None, "tools": [], "memory": None}`
2. `connections = workflow["connections"]`
3. `for source in connections:`
4. `    outputs = connections[source]`
5. `    for kind in outputs:`
6. `        for targets in outputs[kind]:`
7. `            for target in targets:`
8. `                if target["node"] == agent:`
9. `                    if kind == "ai_languageModel":`
10. `                        parts["model"] = source`
11. `                    elif kind == "ai_tool":`
12. `                        parts["tools"].append(source)`
13. `                    elif kind == "ai_memory":`
14. `                        parts["memory"] = source`
15. `parts["tools"].sort()`
16. `return parts`

A `"main"` connection (like the trigger's) matches none of the three kinds, so it's ignored.

**Remember:** one model, a few well-described tools, optional memory.

## Review

<details><summary>Lesson 6: the LM Studio base URL in n8n ends with…?</summary><code>/v1</code></details>
