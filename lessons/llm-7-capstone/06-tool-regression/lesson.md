---
title: Give it a tool and check nothing broke
xp: 50
---
# Fine-tuning can quietly break tool calling

> **Warm-up:** you fine-tuned on plain question/answer pairs with no tool calls. What might happen to the model's ability to call tools?

It can get worse. This is **catastrophic forgetting** (LLMs 6): training only on one kind of output pulls the model away from others. LoRA forgets less than full fine-tuning, but "less" isn't "none". So the last step before you ship is a **regression test**: the same tool tasks, base vs tuned.

**On your machine:** load your GGUF in LM Studio, attach the MCP server you built in LLMs 3 (lesson 9) through `mcp.json`, and run 10–20 prompts that should trigger a tool and a few that shouldn't. Record each reply's tool call (or none). Do the same with the base model.

A reply counts as **correct** when:

- the prompt expects a tool, and the reply calls exactly that tool name with exactly the expected arguments, or
- the prompt expects no tool (`None`), and the reply has no tool call.

If the tuned model's accuracy drops by more than a small tolerance, fix the data: mix some tool-calling examples (in your model's chat template) back into the training set and train again.

## Your quest

Each case is `{"expect": {"name": ..., "args": {...}}}` or `{"expect": None}`. Each reply is `{"tool": {"name": ..., "args": {...}}}` or `{"tool": None}`.

1. `accuracy(cases, replies)`: fraction correct (a float).
2. `regressed(base_acc, tuned_acc, tolerance=0.05)`: `True` when tuned is worse than base by **more** than the tolerance.

## Review

<details><summary>Blind evaluation gives a win rate of 0.58 with a 95% interval of 0.44 to 0.72. Did fine-tuning help?</summary>Not shown yet: the interval includes 0.5. Collect more test prompts.</details>
<details><summary>What is MCP's job, in one sentence?</summary>A standard way to plug tools and data sources into any AI app, so one server works with many clients.</details>
