---
title: Publish it with a model card
xp: 40
---
# Write it up so someone else can trust it

> **Warm-up:** you find a fine-tune on Hugging Face with no description. What do you not know about it?

Everything that matters: what it was trained on, for what, how well it works, and where it fails. A **model card** answers those (you read them in LLMs 2, lesson 12; now you write one). Put it as `README.md` in your GitHub repo and, if you upload the GGUF, in the Hugging Face repo too.

Sections a good card has:

| Section | What goes in it |
|---|---|
| `## Base model` | exact model name and its license (your fine-tune inherits it) |
| `## Training data` | where the data came from, how many examples, how you cleaned it |
| `## Training` | method (QLoRA), rank, alpha, learning rate, epochs, max length, hardware, time |
| `## Evaluation` | blind win rate with its interval, tool-call accuracy base vs tuned |
| `## Limitations` | what it does badly, what it must not be used for |
| `## How to run` | GGUF file + quant, LM Studio / llama.cpp settings, chat template |

Also commit your scripts, your config and a small sample of the data (not private data!) so the run is reproducible.

## Your quest

1. `make_card(info)`: `info` is a dict with keys `name`, `base_model`, `license`, `data`, `training`, `evaluation`, `limitations`, `how_to_run`. Return Markdown that starts with `# <name>` and then has the six sections above, **in that order**, each followed by its text. Put `License: <license>` on its own line inside the base model section.
2. `missing_sections(markdown)`: return the list of the six section headings (like `"## Training data"`) that are not in the text, in table order.

## Review

<details><summary>Your tuned model's tool-call accuracy fell from 0.95 to 0.70. What's the fix?</summary>Mix tool-calling examples (in the right chat template) back into the training data and retrain.</details>
<details><summary>Why must the card name the base model's license?</summary>The fine-tune is a derivative, so the base license's terms still apply to it.</details>
