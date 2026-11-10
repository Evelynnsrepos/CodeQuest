---
title: The training options at a glance
minutes: 20
xp: 30
hint: Read the 'On your PC?' column of the table. 'yes' → True, 'no' or 'only toy models' → False
hint: Prompting and RAG change no weights: False. Everything that trains (pretraining, fine-tuning, LoRA, QLoRA, DPO) changes some: True
hint: LoRA changes weights too: the small added matrices are new weights of the model
---
# Same loop, different data and weights

⏱️ About 20 minutes

> **Warm-up:** you want a model that writes like you. List every way you can think of to get there, from cheapest to most expensive.

Every method below runs the forward/backward loop from LLMs 5. They differ in **what data** they use, **which weights** change, and **how much hardware** that takes:

| Method | What it does | Data | Hardware | On your PC? |
|---|---|---|---|---|
| **Prompting** | No training: instructions and examples in the prompt | a few examples | none | yes |
| **RAG** | No training: look up documents at question time | your documents | an embedding model | yes |
| **Pretraining** | Learn language from scratch | trillions of tokens | thousands of GPUs, months | only toy models |
| **Full fine-tuning** | Keep training *all* weights on your data | thousands+ examples | several 80 GB GPUs for 7B | no |
| **LoRA** | Freeze the model, train small add-on matrices | hundreds–thousands of examples | one GPU | small models |
| **QLoRA** | LoRA on a 4-bit quantized base model | same | one mid-range GPU | yes, up to ~8B with care |
| **RLHF / DPO** | Teach preferences: "answer A is better than B" | pairs of answers | like fine-tuning | DPO with (Q)LoRA, small scale |

Two more you'll hear about: **continued pretraining** (plain text from a new domain, before instruction tuning) and **distillation** (train a small model on a big model's outputs or distributions).

Always try them in this order: **prompting → RAG → (Q)LoRA fine-tuning**. Each step costs a lot more than the one before, and many projects are done after step one or two.

## 🧩 How to answer

Replace each `None` with `True` or `False`. Capital first letter, no quotes. Use the table above:

- `ON_MY_PC`: "yes" or "small models" or "yes, up to ~8B" → `True`. "no" or "only toy models" → `False`.
- `CHANGES_WEIGHTS`: does the method **train**? Training changes weights → `True`. Prompting and RAG only change what goes **into** the model → `False`.

Example of one filled line (a different method, not in the quest): `"using a calculator": False,`. Keep the comma at the end of each line.

## 🎯 Your quest

Fill in `ON_MY_PC`: for each method, `True` if it's realistic on a 12 GB GPU + 32 GB RAM for a useful model, `False` if not.

Then fill in `CHANGES_WEIGHTS`: `True` if the method changes any of the model's weights.

## Review

<details><summary>Roughly how much memory does full fine-tuning of an 8B model take?</summary>About 16 bytes per parameter, so ~128 GB plus activations.</details>
<details><summary>What does the Forward-Forward algorithm replace the backward pass with?</summary>A second forward pass on negative data; each layer learns locally to give high goodness to positive and low goodness to negative data.</details>
