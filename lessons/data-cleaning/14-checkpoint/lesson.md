---
title: Checkpoint: clean a real export
xp: 120
---
# A messy German shop export

> **Warm-up:** before reading on, list the problems you'd expect in a CSV exported from a small online shop's admin page.

Here's the file (it's in the starter as `RAW`):

```
Bestellnr;Kunde;E-Mail;Datum;Betrag;Stadt
1001;Ada Lovelace;ada@example.de;04.11.2026;12,50 €;Köln
1002; ada lovelace ;ADA@example.de;04.11.2026;12,50 €;koeln
1003;Linus;linus@example.de;2026-11-05;1.234,00 €;Muenchen
1004;Grace;N/A;05.11.2026;-;Berlin
1005;Test;test@example.de;31.02.2026;99999,00 €;?
```

Problems: semicolons and a German decimal comma; spaces and case; the same order twice under a different number (1002 duplicates 1001: same email, date and amount); a city written three ways; `N/A` and `-` meaning missing; an impossible date; a test order.

## Your quest

Write `clean_orders(text)` that returns `(clean, report)` using what you built in this course (the helpers you need are short; write them again here):

1. Read the CSV (guess the delimiter, strip a BOM).
2. Turn missing markers (`""`, `N/A`, `-`, `?`, …) into `None`.
3. Tidy every text value; `Kunde` keeps its spelling, `E-Mail` is casefolded.
4. `Betrag` → float with decimal `","`; `Datum` → ISO with the `FORMATS` from lesson 06; `Stadt` → canonical with the `CITY` map in the starter (unknown → `None`).
5. Each clean row is a dict with keys `id` (int), `customer`, `email`, `date`, `amount`, `city`.
6. **Reject** (don't keep) rows with a missing email or a date that couldn't be parsed. Then drop **duplicates**: same email, date and amount, keep the first.
7. `report` is a dict: `{"read": rows read, "rejected": [ids rejected in step 6], "duplicates": [ids dropped as duplicates], "kept": rows kept}`.

Expected: 1001 and 1003 are kept, 1004 and 1005 rejected, 1002 is a duplicate.

## Review

<details><summary>What's a left join's "orphan" telling you?</summary>A row points to something that doesn't exist: an upstream data-quality problem.</details>
<details><summary>Name the steps of a cleaning pipeline.</summary>Read, normalize missing, tidy text, convert types (numbers, dates, categories), validate and reject with reasons, deduplicate, report.</details>

## What's next

The same ideas, with a library that does them fast on millions of rows, are in **pandas** (`read_csv(sep=";", decimal=",")`, `isna()`, `drop_duplicates()`, `merge()`). The *AI engineer* courses use it on your own computer. For AI training data, LLMs 7 lesson 02 applies this course to prompt/answer pairs.
