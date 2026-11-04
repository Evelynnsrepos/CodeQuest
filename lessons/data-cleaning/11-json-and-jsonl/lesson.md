---
title: JSON, JSONL and nested data
xp: 50
---
# Data with layers

> **Warm-up:** an API returns `{"user": {"name": "Ada", "address": {"city": "Berlin"}}}`. How would you put that into a spreadsheet?

**JSON** stores nested data: objects inside objects, lists inside objects. Spreadsheets and many tools want **flat** rows. **Flattening** joins the path of keys with dots:

```
{"user": {"name": "Ada", "address": {"city": "Berlin"}}}
→ {"user.name": "Ada", "user.address.city": "Berlin"}
```

**JSONL** ("JSON lines") puts one JSON object per line. It's the standard format for AI training data (LLMs 5 and 7) and logs, because you can stream it line by line and append to it. One broken line shouldn't kill the whole file: read line by line, **collect** the line numbers that fail, and report them.

## Python you need

```python
import json
json.loads('{"a": 1}')              # {'a': 1}
try: json.loads("{broken")
except json.JSONDecodeError: ...
isinstance(v, dict)
text.splitlines()
```

## Your quest

1. `flatten(d, prefix="")`: a flat dict; nested dicts become dotted keys. Lists and other values stay as they are.
2. `read_jsonl(text)`: `(records, bad)`, where `records` are the parsed objects from non-blank lines and `bad` is a list of **1-based** line numbers that weren't valid JSON **objects** (a line like `[1, 2]` is valid JSON but not an object: bad).

**Remember:** one bad line → report it, don't crash.

## Review

<details><summary>What does a schema say about each column?</summary>Whether it's required, its type, and any extra rule it must follow.</details>
