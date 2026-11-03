---
title: What the model actually reads
xp: 15
---
# Tokens

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

## Python you need

A dictionary maps keys to values. You look a value up with square brackets:

```python
ages = {"Ada": 36, "Linus": 28}
print(ages["Ada"])      # 36
```

`"".join(pieces)` glues a list of strings together: `"".join(["a", "b"])` is `"ab"`.

## Your quest

The starter code has a tiny vocabulary `vocab` (token → ID) and its reverse `id_to_token` (ID → token).

1. Finish `encode(tokens)`: return a list with the ID of each token, in order.
2. Finish `decode(ids)`: turn each ID back into its token, then join them into one string.

Running it should print:

```
[0, 1, 2, 3, 4, 5]
Hello, how are you?
```

## Try it on your machine

Load any model in LM Studio, send a message and look under the reply for the **tokens/s** and token count. Then try the same sentence in German. Does it use more or fewer tokens?
