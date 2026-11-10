---
title: The map of AI
minutes: 15
xp: 30
hint: Ask: where does the right answer come from? Labelled examples → supervised. No answers at all → unsupervised.
hint: The text itself gives the answer (the next word) → self-supervised. Rewards for actions → reinforcement.
---
# Where LLMs sit in the bigger picture

⏱️ About 15 minutes

> **Warm-up:** is a spam filter "AI"? Is a chess engine? Is ChatGPT? What do they have in common, and what's different?

**Artificial intelligence** is the broad goal: machines doing things that need intelligence. **Machine learning (ML)** is the approach that won: instead of writing rules, learn them from data. **Deep learning** is ML with many-layered neural networks. LLMs are one kind of deep learning model.

ML is usually split by **what signal the model learns from**:

| Kind | Learns from | Examples |
|---|---|---|
| **Supervised** | inputs with correct labels | spam or not, house price, image → "cat" |
| **Unsupervised** | inputs only, finds structure | customer groups (clustering), compression |
| **Self-supervised** | labels made from the data itself | LLM pretraining (next token is the label), masked image patches |
| **Reinforcement** | rewards from acting in an environment | game-playing agents, robot control, RLHF and GRPO |

Within supervised learning: **regression** predicts a number, **classification** predicts a category.

Before deep learning took over (around 2012, when the AlexNet CNN won the ImageNet competition), the field was dominated by **classic ML**: linear and logistic regression, decision trees, support vector machines, k-means. These are still the right tool for most **tabular data** (spreadsheets, databases): gradient-boosted trees (XGBoost, LightGBM) usually beat neural networks there.

This course walks the rest of the map: classic ML, then sequence models (RNNs), vision (CNNs, ViTs, CLIP), image generation (diffusion), speech, multimodal LLMs, and RL.

## 🎯 Your quest

Fill `KINDS` with `"supervised"`, `"unsupervised"`, `"self-supervised"` or `"reinforcement"` for each task.

There is no code to write. In the starter each task has empty quotes `""` after the colon. Type one of the four words **between** the quotes, like this:

```python
    "group songs into styles nobody has named yet": "unsupervised",
```

To decide, ask one question for each task: **where does the right answer come from?**

| The task has ... | Kind |
|---|---|
| past examples where a person wrote down the right answer | `supervised` |
| no answers at all; the program finds groups on its own | `unsupervised` |
| answers cut out of the data itself (hide the next word, then guess it) | `self-supervised` |
| a score (reward) after each try, no right answer to copy | `reinforcement` |

Keep the comma at the end of each line. When you run it, every line shows your word in front of the task.

## Review

<details><summary>What does GRPO use as the baseline for an answer's advantage?</summary>The mean reward of the group of answers to the same prompt.</details>
<details><summary>What is a harness?</summary>The program around a model that turns it into an agent: prompts, tools, the loop, permissions and context.</details>
