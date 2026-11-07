---
title: The Code node
minutes: 25
xp: 25
hint: Start with new_items = [] and the loop for item in items:
hint: Inside the loop: if item["json"]["amount"] > 100: and under it fields = dict(item["json"])
hint: Under the if, two more lines: fields["big"] = True and new_items.append({"json": fields})
hint: After the loop: return new_items
---
# When no node does what you need

⏱️ About 25 minutes · one function, seven lines

> **Warm-up:** you want only the orders over 100 € and a new field `big: true` on each. You could chain Filter and Edit Fields nodes. Is there a faster way?

**In one sentence:** the **Code** node runs your own JavaScript or Python on the items, and in "Run Once for All Items" mode it gets the whole list and returns a new list.

## 🪜 Plain words

The Code node has two modes:

- **Run Once for All Items**: your code sees every item at once (good for filtering, sorting, totals).
- **Run Once for Each Item**: your code runs per item.

In JavaScript (the default language), the all-items version of our task looks like this. You don't need to read JavaScript: it's only here so you recognize it in n8n.

```js
return $input.all()
  .filter(item => item.json.amount > 100)
  .map(item => ({ json: { ...item.json, big: true } }));
```

Python works too (choose it in the node). n8n's Python uses names with `_` instead of `$`, like `_input`, and isn't allowed inside `{{ }}` expressions. Here we write the same logic in plain Python, with the items as a normal list.

Rule of thumb: use a normal node when one exists (others can read it at a glance), the Code node when you'd need 3+ nodes or real logic.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `item["json"]["amount"]` | "item's json's amount" | two lookups in a row: the `json` dictionary, then the `amount` in it |
| `>` | "is more than" | `250 > 100` is true. `100 > 100` is **false**: 100 isn't *more* than 100. |
| `dict(d)` | "dict of d" | makes a **copy** of the dictionary `d`. Changing the copy doesn't change the original. |
| `fields["big"] = True` | "fields at big becomes true" | adds a new key (or changes an old one) |

Why copy? Without `dict(...)`, `fields` would be the **same** dictionary as the input item's, just with a second name. Adding `"big"` would then change the input too, and the node before this one would suddenly "see" a field it never made.

### 👀 Worked example: only the long names, with a mark

```python
def long_names(people):
    result = []
    for person in people:
        if len(person["name"]) > 3:
            copy = dict(person)
            copy["long"] = True
            result.append(copy)
    return result

print(long_names([{"name": "Ana"}, {"name": "Bianca"}]))
```

1. `{"name": "Ana"}`: `len("Ana")` is 3. `3 > 3` is false, skip.
2. `{"name": "Bianca"}`: 6 > 3 is true. Copy it, add `"long": True`, append.
3. Returns `[{"name": "Bianca", "long": True}]`, and the input list is unchanged.

## 🎯 Your quest

Write `code_node(items)`: keep only items whose amount is more than 100, as new items with all the old fields plus `"big": True`. Replace `return items` with:

1. `new_items = []`
2. `for item in items:`
3. `    if item["json"]["amount"] > 100:`
4. `        fields = dict(item["json"])`
5. `        fields["big"] = True`
6. `        new_items.append({"json": fields})`
7. `return new_items`

**Remember:** all items in, a new list out.

## Review

<details><summary>Lesson 4: where in a workflow JSON do you see which node comes next?</summary>In <code>connections[name]["main"]</code>.</details>
<details><summary>Why copy the json with dict() before adding a field?</summary>So the input items stay unchanged. Without the copy you'd change the original dictionary too.</details>
