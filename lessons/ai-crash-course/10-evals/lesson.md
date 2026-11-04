---
title: Evals: is it actually better?
xp: 25
---
# Measure, don't vibe

> **Warm-up:** you changed your prompt and the first two answers looked better. Is the new prompt better?

Maybe. Two examples is luck. An **eval** is a fixed set of test questions with known good answers (a **golden set**), scored the same way every time you change something. Common scores:

- **accuracy**: share of answers that match (for questions with one right answer);
- **win rate**: in blind A/B comparisons, how often the new version is preferred (by people, or by a judge model);
- the **error bar**: with few questions, results jump around. With 100 questions and 60% wins, the true rate is roughly 50–70%; with 10 questions, 30–90%.

The interval is about **p ± 2·√(p(1−p)/n)**, where p is the measured rate and n the number of questions. If it includes 50%, you can't call a winner yet.

**Go deeper:** LLMs 7 lesson 05 (blind eval), Math 4 lessons 11–12, AI engineer 2 (evals in practice).

<div class="quiz" data-answer="1" data-why="0.55 ± 2·√(0.55·0.45/100) ≈ 0.45 to 0.65. That range includes 50%, so you can’t call a winner yet."><p><b>Predict first:</b> the new prompt won 55 of 100 blind comparisons. Is it clearly better?</p><button>yes, 55% is more than half</button><button>not yet</button></div>

## Your quest

1. `accuracy(preds, gold)`: share of positions where the prediction equals the gold answer (compare stripped, lowercased strings).
2. `win_interval(wins, n)`: `(low, high)` with `p ± 2·√(p(1−p)/n)`.
3. `is_better(wins, n)`: `True` only if `low > 0.5`.

**Remember:** a fixed test set, the same scoring, and an error bar.
