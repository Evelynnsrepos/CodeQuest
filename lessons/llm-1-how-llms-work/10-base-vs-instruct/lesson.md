---
title: Base models, instruct models and chat templates
xp: 30
---
# From text predictor to assistant

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

## Your quest

Write `to_chatml(messages)`. `messages` is a list of dictionaries like `{"role": "user", "content": "Hi"}`. For each message, add

```
<|im_start|>ROLE\nCONTENT<|im_end|>\n
```

to the result, and at the very end add the open assistant turn `<|im_start|>assistant\n`. (`\n` is a newline inside a Python string.)

## Review

<details><summary>What does top-p = 0.9 keep?</summary>The smallest set of most-likely tokens whose probabilities add up to at least 0.9, renormalized.</details>
<details><summary>Why cut off the long tail at all?</summary>Thousands of individually unlikely tokens add up to a real chance of a garbage pick over a long reply.</details>
