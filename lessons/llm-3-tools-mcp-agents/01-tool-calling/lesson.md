---
title: How a model "uses" a tool
xp: 30
---
# Tool calling

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

## Your quest

Write the tool definition `ROLL_DICE` for a dice-rolling tool, in exactly the format above:

- name `"roll_dice"`, any useful description
- two parameters: `"sides"` (an `"integer"`) and `"count"` (an `"integer"`), each with a description
- only `"sides"` is required

## Review

<details><summary>What is Mixture of Experts?</summary>A model whose MLP blocks are split into many experts with a router choosing a few per token: big total size, small active size.</details>
<details><summary>Which LM Studio endpoint takes a chat, and what format is the reply?</summary>POST /v1/chat/completions; JSON with choices[0].message.content, finish_reason and usage.</details>
