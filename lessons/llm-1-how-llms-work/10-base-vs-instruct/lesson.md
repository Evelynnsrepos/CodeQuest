---
title: Base models, instruct models and chat templates
minutes: 25
xp: 30
hint: Inside the loop: text = text + "<|im_start|>" + message["role"] + "\n" + message["content"] + "<|im_end|>\n"
hint: Last line: return text + "<|im_start|>assistant\n"
---
# From text predictor to assistant

⏱️ About 25 minutes

> **Warm-up:** a model only continues text. So how does it "know" that it should *answer* your question instead of, say, writing three more similar questions?

Models are made in stages:

1. **Pretraining** on trillions of tokens of web text, books and code. The result is a **base model**. It is a brilliant text continuer and nothing more. Give it `"What is the capital of France?"` and it may well continue with `"What is the capital of Germany?"`, because lists of quiz questions are common on the web.
2. **Supervised fine-tuning (SFT)** on many example conversations: user message → ideal assistant reply. The model learns the *format* of a conversation and the role of a helpful assistant.
3. **Preference tuning** (RLHF or DPO, Module 6): humans or other models compare two answers and the model is pushed towards the better one. This shapes tone, helpfulness and refusals.

The result is an **instruct** (or chat) model. On Hugging Face you see both: `Qwen3-8B-Base` vs `Qwen3-8B`, `Llama-3.1-8B` vs `Llama-3.1-8B-Instruct`. For chatting in LM Studio you almost always want the instruct one.

**But the model still only continues text.** The chat you see is flattened into one long string using a **chat template** with special tokens that mark who is speaking. Qwen models use the **ChatML** template:

```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
What is the capital of France?<|im_end|>
<|im_start|>assistant
```

The string ends with an open assistant turn, so the most likely continuation is the assistant's reply, followed by `<|im_end|>`, which works as the stop token. Llama 3 uses a different template (`<|start_header_id|>user<|end_header_id|>` … `<|eot_id|>`). Each model must get *its own* template, exactly as it was trained. GGUF files carry the template inside them, and LM Studio applies it for you (you can see and edit it under the model's prompt template settings). A wrong template is the classic cause of a model that rambles, never stops, or answers as the user.

Reasoning ("thinking") models such as Qwen3 add one more convention: they write their reasoning between `<think>` and `</think>` before the answer. It's still just tokens following a trained format.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `text = ""` | "text becomes empty" | an empty text to build on |
| `for message in messages:` | | once per message |
| `message["role"]` | "message at role" | `"system"`, `"user"` or `"assistant"` |
| `message["content"]` | | what was said |
| `"\n"` | "newline" | a line break inside a text |
| `text = text + "..."` | | adds more to the end of the text (a running total, but for text) |

### 👀 Worked example: a shopping list as text

```python
def as_list(items):
    text = ""
    for item in items:
        text = text + "- " + item["name"] + " x" + item["count"] + "\n"
    return text + "That's all.\n"

print(as_list([{"name": "milk", "count": "2"}, {"name": "tea", "count": "1"}]))
```

1. `text` = `""`.
2. milk: `text` = `"- milk x2\n"`.
3. tea: `text` = `"- milk x2\n- tea x1\n"`.
4. After the loop, one more line is added: `"That's all.\n"`.

It prints:

```
- milk x2
- tea x1
That's all.
```

Your quest has exactly this shape, with ChatML's markers instead of `- ` and ` x`.

## 🎯 Your quest

Write `to_chatml(messages)`. `messages` is a list of dictionaries like `{"role": "user", "content": "Hi"}`.

1. Replace the `pass` line (inside the loop) with:
   - `text = text + "<|im_start|>" + message["role"] + "\n" + message["content"] + "<|im_end|>\n"`
2. Change the last line to add the open assistant turn:
   - `return text + "<|im_start|>assistant\n"`

Run it: the output should look exactly like the ChatML example above.

## Review

<details><summary>What does top-p = 0.9 keep?</summary>The smallest set of most-likely tokens whose probabilities add up to at least 0.9, renormalized.</details>
<details><summary>Why cut off the long tail at all?</summary>Thousands of individually unlikely tokens add up to a real chance of a garbage pick over a long reply.</details>
<details><summary>Why does a ChatML prompt end with "<|im_start|>assistant" and a line break?</summary>So the most likely continuation is the assistant's reply. The model then ends it with <|im_end|>.</details>
