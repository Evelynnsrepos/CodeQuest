---
title: Capstone: review a workflow before it runs
minutes: 60
xp: 60
hint: Check 1: loop over nodes, append each node["name"] to names, and count triggers with if node["type"].lower().endswith("trigger") or node["type"].endswith(".webhook"):
hint: Check 2: the four loops from lesson 7. Inside: if target["node"] not in names: problems.append("unknown node: " + target["node"]), and if kind == "ai_languageModel": has_model.append(target["node"])
hint: Check 3: for node in nodes: if node["type"].endswith(".agent") and node["name"] not in has_model: problems.append(node["name"] + " has no chat model")
hint: Check 4: settings = workflow.get("settings", {}) and if settings.get("errorWorkflow", "") == "": problems.append("set an error workflow")
hint: Check 5: for node in nodes: text = json.dumps(node.get("parameters", {})) and if "sk-" in text or "Bearer " in text: problems.append(node["name"] + " has a secret in it, use credentials")
---
# Your own n8n workflow checker

⏱️ About 60 minutes · one function with five checks, one at a time

> **Warm-up:** before you switch a workflow to active, what five things would you check?

**In one sentence:** a good automation person reads a workflow like code before trusting it, so you'll write a checker for the mistakes from this course, then use it on your real exported workflows.

## 🐍 Python you need

You know almost everything already. The new pieces:

| You write | Say it | What it does |
|---|---|---|
| `workflow.get("connections", {})` | | the connections, or an empty dictionary if the workflow has none |
| `s.lower().endswith("trigger")` | | makes the text lowercase **first**, so `Trigger`, `TRIGGER` and `trigger` all match |
| `triggers != 1` | "triggers is not one" | true for 0, 2, 3, … |
| `x not in names` | "x is not in names" | true when the list doesn't hold `x` |
| `json.dumps(d)` | "JSON dump string" | turns a dictionary (with everything inside it) into **one** text, so you can search all of it with `in` at once |
| `settings.get("errorWorkflow", "")` | | the value, or `""` if the key is missing |

Problems are **added in check order**, because each check runs after the one before. That's why the checks are separate loops.

### 👀 Worked example: one check, the counting pattern

Check 1 is a counter, like this one that counts cats among pets:

```python
pets = [{"name": "Momo", "kind": "Cat"}, {"name": "Rex", "kind": "dog"}]
names = []
cats = 0
for pet in pets:
    names.append(pet["name"])
    if pet["kind"].lower() == "cat":
        cats = cats + 1
print(names, cats)
```

Momo: name added, `"Cat".lower()` is `"cat"` → `cats` = 1. Rex: name added, not a cat. Prints `['Momo', 'Rex'] 1`. One loop collects the names (needed for check 2) **and** counts.

## 🎯 Your quest

Write `review(workflow)` that returns a list of problem messages (empty = ready). The starter already has `problems = []` and `return problems`. Add the lines between them, check by check. Press **Submit** after each check: the checks are tested one at a time.

**Setup:**

1. `nodes = workflow["nodes"]`
2. `connections = workflow.get("connections", {})`

**Check 1, one trigger** (a node whose type ends in `trigger`, in any case, or the Webhook node, whose type ends in `.webhook`):

3. `names = []`
4. `triggers = 0`
5. `for node in nodes:`
6. `    names.append(node["name"])`
7. `    if node["type"].lower().endswith("trigger") or node["type"].endswith(".webhook"):`
8. `        triggers = triggers + 1`
9. `if triggers != 1:`
10. `    problems.append("needs exactly one trigger")`

**Check 2, connections point at real nodes** (the four loops from lesson 7; at the same time, remember which nodes get a model):

11. `has_model = []`
12. `for source in connections:`
13. `    outputs = connections[source]`
14. `    for kind in outputs:`
15. `        for targets in outputs[kind]:`
16. `            for target in targets:`
17. `                if target["node"] not in names:`
18. `                    problems.append("unknown node: " + target["node"])`
19. `                if kind == "ai_languageModel":`
20. `                    has_model.append(target["node"])`

**Check 3, every agent has a model:**

21. `for node in nodes:`
22. `    if node["type"].endswith(".agent") and node["name"] not in has_model:`
23. `        problems.append(node["name"] + " has no chat model")`

**Check 4, an error workflow is set** (lesson 9):

24. `settings = workflow.get("settings", {})`
25. `if settings.get("errorWorkflow", "") == "":`
26. `    problems.append("set an error workflow")`

**Check 5, no secrets in parameters:**

27. `for node in nodes:`
28. `    text = json.dumps(node.get("parameters", {}))`
29. `    if "sk-" in text or "Bearer " in text:`
30. `        problems.append(node["name"] + " has a secret in it, use credentials")`

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
