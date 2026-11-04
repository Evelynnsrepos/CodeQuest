---
title: Prompt, RAG or fine-tune?
xp: 25
---
# Three ways to make a model do your thing

> **Warm-up:** you want a chatbot that answers questions about your company's handbook. What would you try first?

| | What it changes | Good for | Cost |
|---|---|---|---|
| **Prompting** | only the instructions and examples you send | most tasks; always try first | minutes |
| **RAG** (retrieval-augmented generation) | adds relevant documents to the prompt at question time | facts the model doesn't know, facts that change, answers with sources | a few hours to build |
| **Fine-tuning** | the model's weights, with your examples | a consistent style or format, a narrow skill, a smaller cheaper model | data + GPU time; retrain to update |

The rule of thumb: **prompt first; add RAG for knowledge; fine-tune for behaviour.** A common mistake is fine-tuning to teach facts: the model learns the style of your documents but still makes up details, and you must retrain whenever they change.

**Go deeper:** LLMs 3 (RAG and tools), LLMs 6 (fine-tuning and its alternatives), AI engineer 2 (real RAG).

## Your quest

`choose(prompt_works, needs_facts, needs_style)`: return `"prompt"` if `prompt_works`; otherwise `"rag"` if it needs facts the model doesn't have; otherwise `"fine-tune"` if it needs a style or behaviour; otherwise `"prompt"` (keep improving the prompt).

Then fill `CASES` with the right choice for each scenario, using your function's logic.

**Remember:** prompt first, RAG for knowledge, fine-tune for behaviour.
