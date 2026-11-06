---
title: An LLM guesses the next word
xp: 25
hint: next_word, first line: if word not in counts: and under it (8 spaces) return None
hint: Then copy the "most liked fruit" example: followers = counts[word], best = None, best_count = 0, and a for loop.
hint: generate: words = [start], then for step in range(n): and inside it last = words[-1] and nxt = next_word(counts, last).
---
# The one trick behind ChatGPT

⏱️ About 25 minutes · two functions, shown step by step first

> **Warm-up:** finish this: "Once upon a ___". How did you know?

**In one sentence:** a large language model (**LLM**) looks at the text so far, guesses the next word, adds it, and repeats.

## 💡 The idea

An LLM gives every possible next piece of text a **probability** (a chance, like "70% likely"), picks one, adds it to the end, and starts again with the longer text. Answers, code and poems all come out of that loop: **predict, append, repeat**.

It learned those chances by reading huge amounts of text and noticing what usually comes next. The simplest version is **counting**: in a pile of fairy tales, after the word "a" you saw "time" 9 times and "hill" once. So after "a", guess "time".

A real LLM doesn't count; it computes the chances with a neural network, so it also handles sentences it has never seen. But the loop is the same, and that loop is what you'll build.

<div class="quiz" data-answer="0" data-why="It always picks the most frequent follower. A real LLM samples, so “hill” would still come out about 10% of the time."><p><b>Predict first:</b> after “a” the counts are time: 9, hill: 1. Which word does the counting model pick?</p><button>time</button><button>hill</button><button>either, 50/50</button></div>

**Go deeper:** LLMs 1 (How an LLM works), lessons 1–7.

## 🐍 Python you need (part 1): dictionaries and if

A **dictionary** (`dict`) is a list of labels, each with a value. Like a phone book: name → number.

```python
likes = {"apple": 3, "pear": 7, "plum": 5}
```

| You write | Say it | What it does |
|---|---|---|
| `{ ... }` | "a dictionary" | curly brackets hold the whole dictionary |
| `"apple": 3` | "apple maps to 3" | one entry: the **key** `"apple"`, a colon, the **value** `3`. Entries are separated by commas. |
| `likes["pear"]` | "likes at pear" | looks up the value for the key `"pear"`: gives `7` |
| `"kiwi" in likes` | "kiwi in likes" | `True` if `"kiwi"` is a key, otherwise `False`. Here: `False`. |
| `"kiwi" not in likes` | "kiwi not in likes" | the opposite: here `True` |
| `None` | "none" | Python's word for "nothing / no answer" |

A value can itself be a dictionary. That's how the word counts are stored: for each word, a dictionary of the words that came after it and how often.

```python
counts = {"a": {"time": 9, "hill": 1}}
counts["a"]            # gives {"time": 9, "hill": 1}
counts["a"]["time"]    # gives 9
```

**if** runs the indented lines below it only when something is true:

```python
def describe(likes, fruit):
    if fruit not in likes:
        return None
    return likes[fruit]
```

- `if fruit not in likes:` "if the fruit is not a key in likes". The colon starts the "then" part.
- `return None`: indented **8 spaces** (4 for the function, 4 more for the if). Only runs when the fruit is missing. `return` stops the function right there.
- `return likes[fruit]`: back at 4 spaces, so it runs when the if was false.

`describe(likes, "pear")` gives `7`. `describe(likes, "kiwi")` gives `None`.

## 🐍 Python you need (part 2): the "best so far" loop

A **for loop** repeats some lines once for every key in a dictionary:

```python
for fruit in likes:
    print(fruit)
```

This prints `apple`, then `pear`, then `plum`. Each time round, the box `fruit` holds the next key. The indented lines are what gets repeated.

To find the biggest, walk through and keep the **best one so far**:

### 👀 Worked example: the most liked fruit

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

1. `best = None`: no winner yet.
2. `best_count = 0`: the winner's score so far is 0.
3. `for fruit in likes:` look at each fruit in turn.
4. `if likes[fruit] > best_count:` "if this fruit's count is bigger than the best so far" (`>` means "is bigger than").
5. `best = fruit` and `best_count = likes[fruit]`: then it's the new winner; remember its name and its count.
6. `return best`: after the loop (back at 4 spaces), give back the winner.

Watch it run on `{"apple": 3, "pear": 7, "plum": 5}`:

| Turn | fruit | its count | bigger than best_count? | best after | best_count after |
|---|---|---|---|---|---|
| start | | | | None | 0 |
| 1 | apple | 3 | 3 > 0 yes | apple | 3 |
| 2 | pear | 7 | 7 > 3 yes | pear | 7 |
| 3 | plum | 5 | 5 > 7 no | pear | 7 |

Result: `"pear"`.

## 🐍 Python you need (part 3): lists, building text

A **list** is items in order, in square brackets: `words = ["once", "upon"]`.

| You write | Say it | What it does |
|---|---|---|
| `[ "once" ]` | "a list holding once" | a list with one item |
| `words.append("a")` | "words, append a" | adds `"a"` to the end: now `["once", "upon", "a"]` |
| `words[-1]` | "words at minus one" | the **last** item: `"a"` |
| `range(3)` | "range 3" | used as `for step in range(3):` to repeat something **3 times** |
| `break` | "break" | leaves the loop immediately |
| `x is None` | "x is none" | `True` when `x` holds nothing |
| `" ".join(words)` | "join words with spaces" | glues the list into one text: `"once upon a"` |

### 👀 Worked example: a counting list

```python
def count_up(start, n):
    numbers = [start]
    for step in range(n):
        last = numbers[-1]
        numbers.append(last + 1)
    return numbers
```

`count_up(5, 3)`: the list starts as `[5]`. Turn 1: the last is 5, append 6. Turn 2: last 6, append 7. Turn 3: last 7, append 8. Gives `[5, 6, 7, 8]`. Your `generate` works exactly like this, except "the next item" comes from `next_word`, and you stop early if it's `None`.

## 🎯 Your quest

The editor has comments marking every line to write.

**1. `next_word(counts, word)`**: the most frequent word after `word`, or `None` if `word` isn't in `counts`.

- First: `if word not in counts:` and under it `return None` (like `describe`).
- Then: `followers = counts[word]` (the inner dictionary, e.g. `{"time": 9, "hill": 1}`).
- Then the "best so far" loop from `most_liked`, using `followers` instead of `likes`, and `return best`.

**2. `generate(counts, start, n)`**: like `count_up`:

- `words = [start]`
- `for step in range(n):` and inside it:
  - `last = words[-1]`
  - `nxt = next_word(counts, last)` (your own function from step 1!)
  - `if nxt is None:` then `break`
  - `words.append(nxt)`
- after the loop: `return " ".join(words)`

`generate(counts, "once", 5)` should give `"once upon a time there"`: it stops after "there" because nothing ever followed "there".

**Remember:** predict, append, repeat.
