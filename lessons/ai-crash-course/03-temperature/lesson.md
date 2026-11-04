---
title: Probabilities and temperature
xp: 25
---
# Why answers vary

> **Warm-up:** ask a chatbot the same question twice. Why can the answers differ?

The network outputs a **score** (a "logit") per token. **Softmax** turns scores into probabilities: raise e to each score, then divide by the total, so they're all positive and add up to 1.

```
scores  2.0   1.0   0.1
e^x     7.39  2.72  1.11   total 11.21
probs   0.66  0.24  0.10
```

Then the model **samples**: picks token 1 two thirds of the time, token 2 a quarter of the time, and so on. **Temperature** divides the scores before softmax:

- **T < 1** (e.g. 0.2): differences grow, the top token almost always wins: focused, repeatable. Good for code and facts.
- **T > 1**: differences shrink, unlikely tokens get picked more: varied, creative, more mistakes.
- **T = 0** in apps means "always take the top token".

**Go deeper:** LLMs 1, lessons 5, 8 and 9; Math 5 lesson 06.

<div class="quiz" data-answer="0" data-why="Dividing by 0.2 makes the gaps between scores 5 times bigger, so the top token pulls further ahead."><p><b>Predict first:</b> you lower the temperature from 1 to 0.2. What happens to the top token’s probability?</p><button>it goes up</button><button>it goes down</button><button>it stays the same</button></div>

<div class="explore" data-widget="temperature"></div>

## Your quest

`softmax_t(scores, t)`: divide each score by `t`, then softmax. Subtract the biggest score first (`math.exp` of big numbers overflows; subtracting doesn't change the result).

**Remember:** low temperature sharpens, high temperature flattens.
