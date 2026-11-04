---
title: The AI Agent node
xp: 30
---
# A model, tools and memory plugged into one node

⏱️ About 12 minutes · one function

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

## 🎯 Your quest

Write `agent_parts(workflow, agent)`: look through `workflow["connections"]` for sub-nodes connected to the node named `agent` and return `{"model": name or None, "tools": [sorted names], "memory": name or None}`.

<details><summary>💡 Hint</summary>
<pre>parts = {"model": None, "tools": [], "memory": None}
for source, outputs in workflow["connections"].items():
    for kind, lists in outputs.items():
        for targets in lists:
            for t in targets:
                if t["node"] == agent:
                    ...  # ai_languageModel / ai_tool / ai_memory
parts["tools"].sort()</pre>
</details>

**Remember:** one model, a few well-described tools, optional memory.

## Review

<details><summary>Lesson 6: the LM Studio base URL in n8n ends with…?</summary><code>/v1</code></details>
