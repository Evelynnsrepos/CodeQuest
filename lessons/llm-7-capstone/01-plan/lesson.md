---
title: Pick a goal and a base model
xp: 40
---
# The capstone

> **Warm-up:** what's one thing you'd *actually* use a small custom model for? Pick something where you'd immediately notice a bad answer.

The capstone uses every module once, on one project you care about:

1. Choose a **narrow goal** and a small **instruct** base model (1–4B).
2. Build a dataset of 200–1,000 examples in JSONL and clean it by hand.
3. Fine-tune with QLoRA (Unsloth or TRL), locally or on a rented GPU.
4. Evaluate base vs fine-tuned on 20+ held-out prompts, blind.
5. Merge, convert to GGUF, quantize, load in LM Studio.
6. Give it an MCP tool and use it as a small agent.
7. Write it up on GitHub: what worked, what didn't, what you'd change.

Each lesson here builds a small tool for one step, which you then run on your real data.

**Good goals are narrow and checkable:** "answers in my writing style", "turns my messy notes into a fixed Markdown template", "explains NixOS options like I would", "a German–English tutor persona for a game". "A smarter general assistant" is not a capstone goal: you can't beat the base model at everything with 500 examples.

First check the goal against LLMs 6, lesson 2: if it's really *knowledge*, add RAG instead of (or as well as) fine-tuning.

**Choosing the base model** (LLMs 2, lesson 12): instruct version, a license that allows what you want to do with the result, good at your language, a size that trains in your memory budget and runs fast after quantization, and a chat template with tool calling if you'll use MCP. Families with 1–4B instruct models at the time of writing include Qwen3, Llama 3.2, Gemma 3, SmolLM3 and Phi; new ones appear constantly, so check the Hub.

## Your quest

1. Fill in `PROJECT` for **your** capstone: a `goal` (one sentence), a `base_model` (Hugging Face name), a `why_finetune` reason, and at least **three** `success_criteria` you can check on held-out prompts.
2. Write `pick_base(candidates, max_params_b)`: from a list of model dictionaries, keep those that are `instruct`, have a license in `OK_LICENSES` and at most `max_params_b` billion parameters; return the **name** of the largest one, or `None`.

## Review

<details><summary>RAG or fine-tuning for "make it know my notes"?</summary>RAG: it's changing knowledge, and RAG can cite its sources.</details>
<details><summary>What does a training loss near 0 on a small dataset usually mean?</summary>The model is memorizing the training examples (overfitting).</details>
