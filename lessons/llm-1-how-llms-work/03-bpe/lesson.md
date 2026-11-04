---
title: How a vocabulary is built (BPE)
xp: 25
---
# Byte Pair Encoding

> **Warm-up:** if you had to pick 50,000 text pieces to cover all of the internet, how would you decide which ones?

You let the data decide. **Byte Pair Encoding (BPE)** is the algorithm behind the tokenizers of GPT, Llama, Qwen, Mistral and most others:

1. Start with the text split into single characters (real tokenizers start from the 256 possible **bytes**, so any text, emoji or language works).
2. Count every **pair of neighbouring tokens**.
3. **Merge** the most frequent pair into one new token and add it to the vocabulary.
4. Repeat until the vocabulary has the size you want (for example 128,000 merges for Llama 3).

```
l o w   l o w e r   l o w e s t
pairs: (l,o)=3  (o,w)=3  (w,e)=2 ...
merge (l,o) → lo w   lo w e r   lo w e s t
merge (lo,w) → low   low e r   low e s t
```

Frequent words end up as single tokens after a few merges; rare words stay in pieces. The list of merges *is* the tokenizer: to tokenize new text you replay the same merges in the same order. That's why a model only works with the exact tokenizer it was trained with: different merges give different IDs, and the model's numbers would mean nothing.

<svg viewBox="0 0 520 220" width="100%" style="max-width:520px" role="img" aria-label="Byte Pair Encoding merges the most frequent pair step by step: l o w e r becomes lo w e r, then low e r, then low er"><defs><marker id="ah1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs><text x="10" y="22" font-size="12" fill="currentColor" text-anchor="start" font-weight="normal">start: single letters</text><rect x="20" y="30" width="34" height="30" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="37.0" y="49.666666666666664" font-size="14" fill="currentColor" text-anchor="middle">l</text><rect x="60" y="30" width="34" height="30" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="77.0" y="49.666666666666664" font-size="14" fill="currentColor" text-anchor="middle">o</text><rect x="100" y="30" width="34" height="30" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="117.0" y="49.666666666666664" font-size="14" fill="currentColor" text-anchor="middle">w</text><rect x="140" y="30" width="34" height="30" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="157.0" y="49.666666666666664" font-size="14" fill="currentColor" text-anchor="middle">e</text><rect x="180" y="30" width="34" height="30" rx="8" fill="#6c4cf5" fill-opacity=".14" stroke="#6c4cf5" stroke-width="2"/><text x="197.0" y="49.666666666666664" font-size="14" fill="currentColor" text-anchor="middle">r</text><text x="10" y="92" font-size="12" fill="currentColor" text-anchor="start" font-weight="normal">merge the most frequent pair  l + o → lo</text><rect x="20" y="100" width="38" height="30" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="39.0" y="119.66666666666667" font-size="14" fill="currentColor" text-anchor="middle">lo</text><rect x="64" y="100" width="34" height="30" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="81.0" y="119.66666666666667" font-size="14" fill="currentColor" text-anchor="middle">w</text><rect x="104" y="100" width="34" height="30" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="121.0" y="119.66666666666667" font-size="14" fill="currentColor" text-anchor="middle">e</text><rect x="144" y="100" width="34" height="30" rx="8" fill="#30a46c" fill-opacity=".14" stroke="#30a46c" stroke-width="2"/><text x="161.0" y="119.66666666666667" font-size="14" fill="currentColor" text-anchor="middle">r</text><text x="10" y="162" font-size="12" fill="currentColor" text-anchor="start" font-weight="normal">then  lo + w → low,  e + r → er</text><rect x="20" y="170" width="49" height="30" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="44.5" y="189.66666666666666" font-size="14" fill="currentColor" text-anchor="middle">low</text><rect x="75" y="170" width="38" height="30" rx="8" fill="#d97706" fill-opacity=".14" stroke="#d97706" stroke-width="2"/><text x="94.0" y="189.66666666666666" font-size="14" fill="currentColor" text-anchor="middle">er</text><text x="420" y="50" font-size="13" fill="currentColor" text-anchor="middle" font-weight="normal">5 tokens</text><text x="420" y="120" font-size="13" fill="currentColor" text-anchor="middle" font-weight="normal">4 tokens</text><text x="420" y="190" font-size="13" fill="currentColor" text-anchor="middle" font-weight="normal">2 tokens</text></svg>

## Python you need

Tuples are fixed pairs of values: `pair = ("l", "o")`. They can be dictionary keys.

`counts.get(key, 0)` returns the stored value, or `0` if the key isn't there yet. So counting looks like this:

```python
counts = {}
for fruit in ["apple", "pear", "apple"]:
    counts[fruit] = counts.get(fruit, 0) + 1
# {"apple": 2, "pear": 1}
```

`range(len(items) - 1)` gives every position that has a right-hand neighbour.

## Your quest

Write `count_pairs(tokens)`: return a dictionary that maps every neighbouring pair `(tokens[i], tokens[i + 1])` to how often it occurs.

`merge` and the training loop are written for you. With a working `count_pairs`, the program learns 5 merges from a tiny text and prints the vocabulary it grew. Watch `" low"` appear as one token.

One detail real tokenizers add: before BPE runs, a **pre-tokenizer** splits the text at spaces and punctuation, so merges never glue two words together. Without it, a frequent phrase like `" low low"` would become a single token.

## Review

<details><summary>Why are models bad at counting the letters in a word?</summary>They see subword tokens, not letters. "strawberry" might be three tokens, and the letters inside each token are never shown to the model directly.</details>
<details><summary>Why does German usually cost more tokens than English?</summary>The tokenizer's training data had more English, so English words got merged into whole tokens more often and German words stay split into more pieces.</details>
