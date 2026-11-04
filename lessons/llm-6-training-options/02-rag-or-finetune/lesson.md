---
title: RAG or fine-tuning?
xp: 35
---
# Knowledge vs behaviour

> **Warm-up:** "I want the model to know my notes." Fine-tune it on the notes, or put the relevant notes in the prompt? Why?

The rule of thumb that holds up remarkably well:

> **RAG for knowledge. Fine-tuning for behaviour.**

**Knowledge** (facts, documents, your notes, a product manual, anything that changes): use **RAG**. Fine-tuning on facts works poorly: the model picks up the *style* of the documents much faster than it reliably memorizes their *content*, it can't cite sources, it hallucinates confidently when it half-remembers, and every update means retraining. RAG can be updated by editing a file, can quote its source, and lets you check what the model saw.

**Behaviour** (format, style, tone, a persona, always answering in strict JSON, a narrow skill, shorter answers, a language it handles poorly): **fine-tuning** shines. These are patterns the model applies *everywhere*, hard to describe in a prompt but easy to show with a few hundred examples. Fine-tuning can also make a small model as good as a bigger one on *one narrow task*, which saves VRAM and speed.

Before either: **try prompting**. A good system prompt with 3–5 examples ("few-shot") often solves behaviour problems with zero training.

Combinations are normal: a fine-tuned model that's good at *using* retrieved documents, or at calling your tools reliably, with RAG feeding it the facts.

Most people who think they need training actually need RAG or a better prompt.

## Your quest

`decide(goal)` gets a dictionary describing a goal: `"needs_facts"` (it must know specific, changing or private information), `"needs_behaviour"` (a style, format or skill applied everywhere) and `"prompt_works"` (a system prompt with examples already does it). Return:

- `"prompt"` if `prompt_works` is true,
- otherwise `"both"` if it needs facts and behaviour,
- otherwise `"rag"` for facts, `"finetune"` for behaviour, and `"prompt"` if it needs neither.

## Review

<details><summary>In which order should you try prompting, RAG and fine-tuning?</summary>Prompting first, then RAG, then (Q)LoRA fine-tuning.</details>
<details><summary>Which methods change the model's weights?</summary>Pretraining, full fine-tuning, LoRA, QLoRA and DPO. Prompting and RAG don't.</details>
