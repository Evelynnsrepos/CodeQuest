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

## Your quest

`softmax_t(scores, t)`: divide each score by `t`, then softmax. Subtract the biggest score first (`math.exp` of big numbers overflows; subtracting doesn't change the result).

**Remember:** low temperature sharpens, high temperature flattens.
