---
title: Checkpoint: RAG or fine-tuning, and why
xp: 70
---
# Checkpoint

The Module 6 checkpoint, from your plan: *explain whether a given goal needs RAG or fine-tuning, and why.* For each goal, choose `"prompt"`, `"rag"`, `"finetune"` or `"both"`, and write **one or two sentences** of reasoning, as if explaining it to a friend.

| # | Goal |
|---|---|
| `notes` | "Make it know my notes" (300 Markdown files that I edit every week) |
| `pirate` | "Make a 1B model *always* talk like a pirate, in every reply, even with no system prompt, because it'll run inside a game where I can't control the prompt" |
| `football` | "Answer questions about this weekend's football results" |
| `json` | "Always answer in my app's exact JSON schema; with prompting it still breaks the format about 1 time in 10" |
| `helper` | "A helper that writes in my personal style *and* knows my project's documentation" |
| `german` | "Summarize articles in German instead of English" (a 14B model that speaks German well) |

The check looks at your choices and that each reason uses at least one fitting idea (for example knowledge that changes, citing sources, style, format, behaviour, a system prompt). Once you pass, compare your reasons with the model answers.

<details><summary>Open only after you pass: model answers</summary>

- **notes → rag.** It's knowledge, and it changes every week; RAG updates by editing files and can show which note it used. Fine-tuning would mostly copy the notes' style and hallucinate details.
- **pirate → finetune.** Normally a system prompt does this, but here you can't control the prompt and a small model forgets instructions. Baking a behaviour in is exactly what fine-tuning is for.
- **football → rag.** The facts didn't exist when the model was trained and change every week: retrieve them at question time (or call a tool).
- **json → finetune.** A format/behaviour the model must apply every time; a few hundred examples fix the 10% failures. (Also look at constrained/structured output, which forces valid JSON at sampling time.)
- **helper → both.** Style is behaviour (fine-tune), the docs are knowledge (RAG).
- **german → prompt.** The model can already do it; just ask in the system prompt. No training needed.
</details>

## What's next

LLMs 7, the capstone: your own fine-tuned model, end to end.
