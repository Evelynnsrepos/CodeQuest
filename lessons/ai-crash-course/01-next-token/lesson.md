---
title: An LLM guesses the next word
xp: 20
---
# The one trick behind ChatGPT

> **Warm-up:** finish this: "Once upon a ___". How did you know?

A large language model (**LLM**) does one thing: given the text so far, it gives a **probability for every possible next piece of text**, picks one, adds it, and repeats. Answers, code and poems all come out of that loop.

It learned those probabilities by reading huge amounts of text and noticing what usually comes next. The simplest version of that idea is counting: after "once upon a", the word "time" came next most often.

```python
counts = {"a": {"time": 9, "hill": 1}}
max(counts["a"], key=counts["a"].get)   # 'time'
```

A real LLM doesn't count whole phrases; it computes the probabilities with a neural network, so it can handle sentences it has never seen. But the loop is the same.

**Go deeper:** LLMs 1 (How an LLM works), lessons 1–7.

## Your quest

1. `next_word(counts, word)`: the most frequent word after `word`, or `None` if `word` isn't in `counts`.
2. `generate(counts, start, n)`: start with `[start]`, append `next_word` of the last word `n` times (stop early if it's `None`), return the words joined by spaces.

**Remember:** predict, append, repeat.
