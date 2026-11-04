---
title: Capstone: review a workflow before it runs
xp: 60
---
# Your own n8n workflow checker

⏱️ About 20 minutes · one function with five checks

> **Warm-up:** before you switch a workflow to active, what five things would you check?

**In one sentence:** a good automation person reads a workflow like code before trusting it, so you'll write a checker for the mistakes from this course, then use it on your real exported workflows.

## 🎯 Your quest

Write `review(workflow)` that returns a list of problem messages (empty = ready). Do the checks in this order. The checks test them one at a time.

1. **One trigger.** Count nodes whose `type` ends with `Trigger` (any case: `.lower().endswith("trigger")`), plus the Webhook node, the one trigger without it in its name (`type` ends with `.webhook`). Not exactly 1 → `"needs exactly one trigger"`.
2. **Connections point at real nodes.** For every target in `connections` (any connection type) whose node name isn't in `nodes` → `"unknown node: NAME"`.
3. **Every agent has a model.** For every node whose type ends with `.agent`, if no `ai_languageModel` connection goes to it → `"NAME has no chat model"` (reuse lesson 7's idea).
4. **An error workflow is set.** `workflow.get("settings", {}).get("errorWorkflow")` is empty → `"set an error workflow"` (lesson 9).
5. **No secrets in parameters.** If `json.dumps` of a node's `parameters` contains `"sk-"` or `"Bearer "` → `"NAME has a secret in it, use credentials"`.

Report problems node by node in the order of the `nodes` list (for checks 3 and 5) and connections in the order they appear (check 2).

<details><summary>💡 Hint 1: names and types</summary><code>names = {n["name"] for n in workflow["nodes"]}</code></details>
<details><summary>💡 Hint 2: walking connections</summary>Same four loops as lesson 7: <code>for source, outputs in ...items(): for kind, lists in outputs.items(): for targets in lists: for t in targets:</code></details>
<details><summary>💡 Hint 3: secrets</summary><code>text = json.dumps(node.get("parameters", {}))</code>, then <code>if "sk-" in text or "Bearer " in text:</code></details>

## 🖥️ Make it real

Build this in n8n on your computer, then export it and run `review()` on it (paste the JSON into `json.loads`):

1. **Schedule Trigger** (every morning) → **Read/Write Files from Disk** or an email node to get new items.
2. **Loop Over Items** (batch size 2, lesson 10).
3. **AI Agent** with your **LM Studio** or **Ollama** model (lesson 6), one or two tools, **Require Specific Output Format** + Structured Output Parser (lesson 8).
4. An **IF** node on the label → a "safe" path that runs alone and a "risky" path that only drafts (AI automation 1, lesson 9).
5. Settings → your **Error Handler** workflow (lesson 9).
6. Optional: offer it as a tool with an **MCP Server Trigger** in a second workflow (lesson 11).

Save the exported JSON in a git repo. That's a portfolio piece: a local-AI automation that runs every day without sending your data anywhere.

**Remember:** one trigger, real connections, a model per agent, an error workflow, no secrets.

## Review

<details><summary>Lesson 1: in the AI starter kit, what's the Ollama base URL?</summary><code>http://ollama:11434</code> (the compose service name).</details>
<details><summary>Lesson 3: what does $json mean?</summary>The current item's json.</details>
<details><summary>Lesson 11: which node lets an n8n agent use another MCP server?</summary>The MCP Client Tool node.</details>
