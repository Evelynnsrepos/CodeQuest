---
title: One thing, many spellings
xp: 45
---
# Köln, Koeln, Cologne, koln

> **Warm-up:** a form lets people type their city. How many ways can someone write "München"?

A **category** column (city, product type, label) should have a small, fixed set of values. People type variants: accents or no accents, `oe` for `ö`, English names, typos. Clean it in two steps:

1. **Fold** the text to a rough form: `key()` from lesson 03, and strip accents, so `Köln`, `KÖLN` and `Koln` all become `koln`.
2. **Map** folded forms to the one official spelling with a dictionary you write by hand: `{"koln": "Köln", "koeln": "Köln", "cologne": "Köln"}`.

Values that don't fold to anything in your map are **unknown**: collect them, look at them, and extend the map. Don't silently guess.

**For AI labels:** if half your "positive" examples say `pos` and the other half `Positive`, the model sees two classes. This step matters a lot for training data.

## Python you need

Accents can be split off a letter: `unicodedata.normalize("NFKD", "ö")` gives `"o"` followed by a separate "combining" dot mark. Drop the marks:

```python
import unicodedata
def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
strip_accents("Café Köln")   # 'Cafe Koln'
```

(`ß` has no accent to strip; `casefold()` already turns it into `ss`.)

## Your quest

1. `fold(s)`: tidy (strip and collapse spaces), casefold, strip accents.
2. `canonical(s, mapping)`: if `fold(s)` is a key of `mapping`, return the mapped value; if `fold(s)` equals the `fold` of one of the mapping's **values**, return that value; otherwise `None`.
3. `unknowns(values, mapping)`: the sorted list of distinct `fold`ed values that `canonical` can't place (ignore `None` and blanks).

**Remember:** a small hand-written map beats clever guessing.

## Review

<details><summary>Why store dates as YYYY-MM-DD?</summary>Unambiguous, sorts correctly as text, read by every tool.</details>
