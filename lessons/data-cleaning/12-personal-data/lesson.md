---
title: Text hygiene and personal data
xp: 55
---
# Before you share it or train on it

> **Warm-up:** you want to train a model on your old support emails. What in them must not end up inside a model?

Text columns need two last cleanups.

**1. Hygiene.** Unicode can write "é" as one character or as "e + accent". They look the same but compare as different. `unicodedata.normalize("NFC", s)` picks one form. Also remove **control characters** (invisible codes like `\x00` or `\x1b` from broken exports), but keep normal line breaks and tabs.

**2. Personal data (PII).** Names, emails, phone numbers, addresses, IBANs. In the EU the **GDPR** (DSGVO) says you need a reason and permission to process them, and a model trained on them can repeat them to strangers. Before sharing a dataset or training on it, **redact**: replace each one with a placeholder like `[EMAIL]`.

Regex catches the regular-shaped ones (emails, phone numbers, IBANs). Names are much harder; real pipelines use a trained model for those (look up Microsoft Presidio). Regex redaction is a good first layer, not a guarantee.

## The patterns

| Thing | Pattern | Matches |
|---|---|---|
| email | `[\w.+-]+@[\w-]+(\.[\w-]+)+` | `ada.l+news@mail.example.de` |
| IBAN | `\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}(?: ?[A-Z0-9]{1,4})?\b` | `DE89 3704 0044 0532 0130 00` |
| phone | `\+?\d[\d /-]{7,}\d` | `+49 170 1234567`, `030/1234567` |

Order matters: redact **IBANs before phones**, or the phone pattern eats the IBAN's digits.

## Python you need

```python
import re, unicodedata
re.sub(r"\d+", "[N]", "a 12 b 345")      # 'a [N] b [N]'
unicodedata.category("\x00")             # 'Cc' = control character
```

## Your quest

1. `clean_text(s)`: NFC-normalize, then drop every character whose `unicodedata.category` is `"Cc"` **except** `\n` and `\t`.
2. `redact(s)`: replace emails with `[EMAIL]`, then IBANs with `[IBAN]`, then phones with `[PHONE]` (patterns in the starter).
3. `pii_counts(s)`: a dict `{"EMAIL": n, "IBAN": n, "PHONE": n}` with how many of each `redact` replaced.

**Remember:** redact before you share or train, and know that regex misses names.

## Review

<details><summary>Why read JSONL line by line?</summary>One broken line can be reported and skipped instead of crashing the whole file; and huge files stream.</details>
