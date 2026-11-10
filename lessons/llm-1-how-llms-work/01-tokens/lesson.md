---
title: What the model actually reads
minutes: 20
xp: 15
hint: encode: inside the for loop, replace pass with ids.append(vocab[token])
hint: decode: for i in ids: and inside it pieces.append(id_to_token[i])
hint: decode, last line: return "".join(pieces)
---
# Tokens

⏱️ About 20 minutes

> **Warm-up (answer in your head first):** when you type `Hello, how are you?` into LM Studio, what does the model receive: words, letters, or something else?

The model never sees letters or words. A program called the **tokenizer** chops your text into pieces called **tokens**, using a fixed list called the **vocabulary**. Every model ships its own vocabulary, usually 32,000 to 260,000 entries. Each token has a position in that list, its **ID**, and the model only ever sees those ID numbers.

```
"Hello, how are you?"
→ ["Hello", ",", " how", " are", " you", "?"]   (6 tokens)
→ [  412,   7,   88,    91,    60,   3 ]        (IDs in a made-up vocabulary)
```

Two things to notice:

- The **space belongs to the next word** (`" how"`, not `"how"`). `"how"` and `" how"` are different tokens with different IDs.
- Going from text to IDs is **encoding**. Going back from IDs to text is **decoding**. The model reads IDs and writes IDs; the tokenizer turns its output IDs back into the text you see.

Tokens are the unit of everything: the context window is measured in tokens, speed is measured in **tokens per second** (LM Studio shows it under every reply), and paid APIs charge per million tokens. A rough rule for English is 1 token ≈ ¾ of a word, but it depends on the language and the tokenizer.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `{"Hello": 0, ",": 1}` | "a dictionary: Hello is 0, comma is 1" | a **dictionary**: pairs of key → value. Here: token → ID. |
| `vocab["Hello"]` | "vocab at Hello" | looks up the value for that key: `0` |
| `id_to_token[0]` | "id-to-token at 0" | the other direction: ID → token, `"Hello"` |
| `ids = []` | "ids becomes an empty list" | a new, empty list |
| `for token in tokens:` | "for each token in tokens" | runs the lines under it (4 more spaces) once per item in the list |
| `ids.append(x)` | "ids append x" | adds `x` to the end of the list |
| `"".join(pieces)` | "empty-string join pieces" | glues a list of texts together with nothing between them: `["Hi", "!"]` → `"Hi!"` |

The line `id_to_token = {...}` at the top of the starter builds the reverse dictionary for you. You don't need to change or understand it yet.

### 👀 Worked example: same shape, a colour code

```python
code = {"red": 1, "blue": 2}
name = {1: "red", 2: "blue"}

def to_numbers(colours):
    numbers = []
    for c in colours:
        numbers.append(code[c])
    return numbers

def to_text(numbers):
    pieces = []
    for n in numbers:
        pieces.append(name[n])
    return "-".join(pieces)

print(to_numbers(["blue", "red"]))   # [2, 1]
print(to_text([2, 1]))               # blue-red
```

`to_numbers(["blue", "red"])`, round by round:

1. `numbers` = `[]`.
2. `c` = `"blue"`: `code["blue"]` is 2 → `numbers` = `[2]`.
3. `c` = `"red"`: `code["red"]` is 1 → `numbers` = `[2, 1]`.

`to_text` does the reverse and glues with `"-"`. Your `decode` glues with `""` (nothing), because the spaces are already inside the tokens.

## 🎯 Your quest

The starter has a tiny vocabulary `vocab` (token → ID) and its reverse `id_to_token` (ID → token).

**Part 1:** `encode(tokens)`. In the loop, replace the `pass` line with:

- `ids.append(vocab[token])` (8 spaces in front: it's inside the loop)

**Part 2:** `decode(ids)`. Replace the comment and `return ""` with:

1. `for i in ids:`
2. `    pieces.append(id_to_token[i])`
3. `return "".join(pieces)`

Running it should print:

```
[0, 1, 2, 3, 4, 5]
Hello, how are you?
```

## Try it on your machine

Load any model in LM Studio, send a message and look under the reply for the **tokens/s** and token count. Then try the same sentence in German. Does it use more or fewer tokens?
## Review

<details><summary>What does "".join(["a", "b", "c"]) give?</summary>"abc": the pieces glued together with nothing between them.</details>
