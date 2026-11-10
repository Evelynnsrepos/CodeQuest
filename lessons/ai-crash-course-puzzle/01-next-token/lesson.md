---
title: An LLM guesses the next word
minutes: 25
xp: 25
hint: next_word starts by checking the word is there: if word not in counts:  Then followers = counts[word].
hint: Inside the loop: if followers[w] > best_count: then best = w and best_count = followers[w]. After the loop: return best.
hint: generate: words = [start], then nxt = next_word(counts, last), then words.append(nxt).
distractor: if followers[w] < best_count:
distractor: best = followers
distractor: words.append(last)
---
# The one trick behind ChatGPT

⏱️ About 25 minutes · 🧩 9 gaps, 3 decoys

> **Warm-up:** finish this: "Once upon a ___". How did you know?

**In one sentence:** a large language model (**LLM**) looks at the text so far, guesses the next word, adds it, and repeats.

## 💡 The idea

An LLM gives every possible next word a **probability** (a chance, like "70% likely"), picks one, sticks it on the end, and starts again. Answers, code and poems all come out of that loop: **predict, append, repeat**.

The simplest way to guess is **counting**. In a pile of fairy tales, after the word "a" you saw "time" 9 times and "hill" once. So after "a", guess "time". A real LLM computes the chances with a neural network instead of counting, but the loop is the same.

## 🐍 The Python in this puzzle

**A dictionary** is a list of labels with a value each, like a phone book:

```python
likes = {"apple": 3, "pear": 7}
```

| Piece | Say it | What it does |
|---|---|---|
| `{ }` | "a dictionary" | holds the whole thing |
| `"pear": 7` | "pear maps to 7" | one entry: label (the **key**), colon, value |
| `likes["pear"]` | "likes at pear" | looks up the value: `7` |
| `"kiwi" not in likes` | "kiwi not in likes" | `True`, because there's no kiwi label |
| `None` | "none" | Python's word for "nothing" |
| `if ...:` | "if" | the indented lines below only run when it's true |
| `>` | "is bigger than" | `7 > 3` is `True`, `3 > 7` is `False` |
| `<` | "is smaller than" | the opposite. Watch out for this one in the tray! |

**A list** is items in order: `words = ["once", "upon"]`.

| Piece | Say it | What it does |
|---|---|---|
| `[start]` | "a list holding start" | a list with one item in it |
| `words[-1]` | "words at minus one" | the **last** item |
| `words.append(x)` | "words, append x" | adds `x` to the end |
| `for step in range(n):` | "n times" | repeats the indented lines n times |
| `break` | "break" | jumps out of the loop right now |
| `" ".join(words)` | "join with spaces" | glues the list into one text |

## 👀 Worked example: the most liked fruit

This finds the biggest one by keeping the **best so far**:

```python
def most_liked(likes):
    best = None
    best_count = 0
    for fruit in likes:
        if likes[fruit] > best_count:
            best = fruit
            best_count = likes[fruit]
    return best
```

Watch it run on `{"apple": 3, "pear": 7, "plum": 5}`:

| Turn | fruit | its count | bigger than best_count? | best | best_count |
|---|---|---|---|---|---|
| start | | | | None | 0 |
| 1 | apple | 3 | 3 > 0 yes | apple | 3 |
| 2 | pear | 7 | 7 > 3 yes | pear | 7 |
| 3 | plum | 5 | 5 > 7 no | pear | 7 |

Result: `"pear"`. Your `next_word` is **the same shape**, with `followers` instead of `likes` and `w` instead of `fruit`.

<div class="quiz" data-answer="0" data-why="It always picks the most frequent follower. A real LLM samples, so “hill” would still come out sometimes."><p><b>Predict first:</b> after “a” the counts are time: 9, hill: 1. Which word does the counting model pick?</p><button>time</button><button>hill</button><button>either, 50/50</button></div>

## 🧩 Your puzzle

**`next_word(counts, word)`**, top to bottom:

1. Check the word is known: the block starting with `if word not in counts:`
2. Get its inner dictionary, e.g. `{"time": 9, "hill": 1}`: `followers = counts[word]`
3. In the loop: "is this one **bigger** than the best so far?" (decoy: the one with `<`)
4. & 5. Then remember the name `w` and its count `followers[w]` (decoy: `best = followers`, that's the whole dictionary, not one word).
6. After the loop: give back the winner.

**`generate(counts, start, n)`**:

7. Start the list with just the first word.
8. Ask your own `next_word` what follows the **last** word.
9. Stick that **next** word on the end (decoy: appending `last` would repeat the same word forever).

Run it: you should see `time | once upon a time there`.

**Remember:** predict, append, repeat.
