---
title: How a model "uses" a tool
minutes: 25
xp: 30
hint: Fill "name" with "roll_dice" and "description" with a real sentence, like "Roll dice and return the results."
hint: "parameters" needs three keys: "type": "object", "properties": {...} and "required": ["sides"]
hint: Inside properties: "sides": {"type": "integer", "description": "..."} and the same for "count"
---
# Tool calling

⏱️ About 25 minutes

> **Warm-up:** a model is a function from tokens to next-token probabilities. So how can it possibly "check the weather" or "read a file"?

It can't, and it never does. What it can do is **write a request** in an agreed format. Your program (LM Studio, an agent) reads that request, runs the real function, and sends the result back as another message. The model only ever produces text.

The steps:

1. You describe the available tools in the request: a **name**, a **description** and the **parameters** as a JSON Schema.
2. The chat template renders those descriptions into the prompt (each model family has its own way).
3. A model trained for tool use answers with a **tool call** instead of plain text.
4. The app runs the tool and appends the result as a `tool` message.
5. The model is called again and now answers with the result in its context.

In the OpenAI-compatible API, step 1 looks like this:

```json
"tools": [{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "parameters": {
      "type": "object",
      "properties": {"city": {"type": "string", "description": "City name, e.g. Berlin"}},
      "required": ["city"]
    }
  }
}]
```

The description isn't decoration: it's the *only* thing the model knows about the tool. Vague descriptions give wrong or missing calls. Only models trained for tool calling (Qwen3, Llama 3.1+, Mistral, gpt-oss and others; LM Studio marks them with a tool icon) do it reliably, and low temperature helps.

## 🐍 Python you need

A tool definition is just **dictionaries inside dictionaries**. Python writes them almost exactly like JSON.

| You write | Say it | What it does |
|---|---|---|
| `{"name": "roll_dice"}` | | a dictionary with one key |
| `{"a": 1, "b": 2}` | | several pairs, separated by commas |
| `{"outer": {"inner": 1}}` | | a dictionary as a value inside another one |
| `["sides"]` | "a list with sides in it" | a list with one text |
| `"integer"` | | JSON Schema's word for a whole number |

The **indentation** (spaces in front) isn't required inside brackets, but it makes it much easier to see which bracket belongs where. Every `{` needs its `}`, every `[` its `]`, and pairs inside the same dictionary are separated by commas.

### 👀 Worked example: a tool for the weather

Here's the lesson's `get_weather` tool written in Python, with a second, optional parameter `"unit"`:

```python
GET_WEATHER = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name, e.g. Berlin"},
                "unit": {"type": "string", "description": "celsius or fahrenheit"},
            },
            "required": ["city"],
        },
    },
}
```

Read it from the outside in:

1. The whole thing: `type` is `"function"`, and `function` holds the details.
2. `function` has a `name`, a `description` and `parameters`.
3. `parameters` is a JSON Schema: it's an `"object"`, its `properties` list each parameter, and `required` says which ones must be given.
4. Each property has a `type` and a `description`. `"unit"` is not in `required`, so the model may leave it out.

## 🎯 Your quest

Write `ROLL_DICE` with the same shape as `GET_WEATHER`. Change the starter so that:

1. `"name"` is `"roll_dice"`.
2. `"description"` is a real sentence, for example `"Roll dice and return the results."`.
3. `"parameters"` (replace the empty `{}`) has:
   - `"type": "object",`
   - `"properties"` with two entries:
     - `"sides": {"type": "integer", "description": "Number of sides on each die, e.g. 6"},`
     - `"count": {"type": "integer", "description": "How many dice to roll"},`
   - `"required": ["sides"],`

Press **Run** to see it printed as JSON. If Python complains, count your brackets and commas.

## Review

<details><summary>What is Mixture of Experts?</summary>A model whose MLP blocks are split into many experts with a router choosing a few per token: big total size, small active size.</details>
<details><summary>Which LM Studio endpoint takes a chat, and what format is the reply?</summary>POST /v1/chat/completions; JSON with choices[0].message.content, finish_reason and usage.</details>
