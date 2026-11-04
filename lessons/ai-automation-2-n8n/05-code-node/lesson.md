---
title: The Code node
xp: 25
---
# When no node does what you need

⏱️ About 10 minutes · one function

> **Warm-up:** you want only the orders over 100 € and a new field `big: true` on each. You could chain Filter and Edit Fields nodes. Is there a faster way?

**In one sentence:** the **Code** node runs your own JavaScript or Python on the items, and in "Run Once for All Items" mode it gets the whole list and returns a new list.

## 🪜 Plain words

The Code node has two modes:

- **Run Once for All Items**: your code sees every item at once (good for filtering, sorting, totals).
- **Run Once for Each Item**: your code runs per item.

In JavaScript (the default language), the all-items version of our task is:

```js
return $input.all()
  .filter(item => item.json.amount > 100)
  .map(item => ({ json: { ...item.json, big: true } }));
```

Python works too (choose it in the node). n8n's Python uses names with `_` instead of `$`, like `_input`, and isn't allowed inside `{{ }}` expressions. Here we write the same logic in plain Python, with the items as a normal list.

Rule of thumb: use a normal node when one exists (others can read it at a glance), the Code node when you'd need 3+ nodes or real logic.

## 🎯 Your quest

Write `code_node(items)`: keep only items whose `json["amount"]` is greater than 100, and return them as new items with all old fields plus `"big": True`. Don't change the input items.

<details><summary>💡 Hint</summary><code>return [{"json": {**i["json"], "big": True}} for i in items if i["json"]["amount"] > 100]</code>. <code>{**old, "big": True}</code> makes a copy with one more key.</details>

**Remember:** all items in, a new list out.

## Review

<details><summary>Lesson 4: where in a workflow JSON do you see which node comes next?</summary>In <code>connections[name]["main"]</code>.</details>
