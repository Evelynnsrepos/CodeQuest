---
title: Routers: send each item to the right place
minutes: 20
xp: 25
hint: First two lines: labels = list(handlers) and prompt = "Answer with one word from: " + ", ".join(labels) + ".\n\n" + text
hint: Then clean the reply like lesson 3: reply = llm(prompt).strip().lower().strip(".")
hint: Pick the handler: handler = handlers.get(reply, handlers["other"])
hint: Last line: return handler(text)
---
# One question, many paths

⏱️ About 20 minutes · one function, five lines

> **Warm-up:** your inbox gets bills, newsletters and messages from friends. Should one prompt handle all three?

**In one sentence:** a **router** asks the model one short question (which kind is this?) and then your code sends the item to the function for that kind.

## 🪜 Plain words

Think of a post office worker who only reads the address and puts each letter in the right box. The worker doesn't open the letters. The model is that worker: it only decides **where** something goes. What happens next is done by plain, testable functions, called **handlers**.

The handlers live in a **dictionary**: label → function.

```python
handlers = {"bill": save_to_bills, "newsletter": archive, "other": ask_me}
```

`"bill"` is the key, `save_to_bills` is the function for it (no brackets: we store the function, we don't run it yet).

This lesson is lesson 3's `label_for` plus that dictionary.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `list(handlers)` | "list of handlers" | the dictionary's **keys** as a list: `["bill", "newsletter", "other"]` |
| `", ".join(labels)` | "comma-space join labels" | `"bill, newsletter, other"` |
| `.strip().lower().strip(".")` | | cleans the reply (lesson 3): ends trimmed, lowercase, no dots |
| `handlers["other"]` | "handlers at other" | the value stored under the key `"other"`: here, a function |
| `handlers.get(reply, backup)` | "handlers get reply, else backup" | the value under the key `reply`. If there's no such key, it gives `backup` instead of crashing. |
| `handler(text)` | "handler of text" | **runs** the function in the box `handler` with `text` |

### 👀 Worked example: a tiny food router

```python
def make_tea(order):
    return "tea for " + order

def make_coffee(order):
    return "coffee for " + order

def say_sorry(order):
    return "sorry, " + order

drinks = {"tea": make_tea, "coffee": make_coffee, "other": say_sorry}

choice = "juice"
maker = drinks.get(choice, drinks["other"])
print(maker("Ana"))
```

Line by line:

1. `drinks` maps three words to three functions.
2. `choice` is `"juice"`. There is no key `"juice"`, so `drinks.get("juice", drinks["other"])` gives the backup: the function `say_sorry`. Now `maker` **is** `say_sorry`.
3. `maker("Ana")` runs `say_sorry("Ana")` and prints `sorry, Ana`.

With `choice = "tea"`, `maker` would be `make_tea`, and it prints `tea for Ana`.

## 🎯 Your quest

Write `route(text, llm, handlers)`. Replace the starter's last line with:

1. `labels = list(handlers)`
2. `prompt = "Answer with one word from: " + ", ".join(labels) + ".\n\n" + text`
3. `reply = llm(prompt).strip().lower().strip(".")`
4. `handler = handlers.get(reply, handlers["other"])`
5. `return handler(text)`

## 🖥️ On your computer

Routers save money: a small fast local model does the routing, and only the hard path calls a big model.

**Remember:** the model picks the path, code walks it.

## Review

<details><summary>Lesson 5: how do you get a function's name in Python?</summary><code>step.__name__</code></details>
<details><summary>What does handlers.get("xyz", handlers["other"]) give when there's no "xyz" key?</summary>The backup: the function stored under "other".</details>
