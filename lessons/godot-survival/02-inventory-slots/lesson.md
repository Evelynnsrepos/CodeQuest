---
title: Inventory slots and stacks
xp: 30
hint: First loop: top up slots that already hold this item. Second loop: fill empty (null) slots.
hint: In both loops, put mini(remaining, space left) and subtract it from remaining. Return remaining at the end.
---
# 10 wood per slot

> **Warm-up:** You pick up 15 wood, but one slot holds only 10. Where does the rest go?

A simple inventory can be a Dictionary (`{"wood": 23}`), but survival games usually show **slots**: a fixed number of boxes, each holding one kind of item, up to a **stack limit**. 23 wood with a stack size of 10 fills three slots: 10, 10 and 3.

We'll store the slots in an Array. An empty slot is `null`, a full one is a small Dictionary:

```gdscript
var slots := [{"item": "wood", "count": 10}, {"item": "wood", "count": 3}, null, null]
```

Adding items happens in two passes:

1. **Top up** slots that already hold this item and aren't full yet.
2. **Fill empty slots** with new stacks.

At each step, put in as much as fits: `mini(remaining, space_left)`. If there's still something left when you run out of slots, the inventory is full, so return how many didn't fit (the game might drop them on the ground).

Let's trace adding 15 wood to the inventory above, with `stack_size = 10`:

```
pass 1: slot 0 is full (10), skip it.
        slot 1 has 3, space 7 → put in 7. Remaining: 8.
pass 2: slot 2 is empty → new stack of min(8, 10) = 8. Remaining: 0. Done!
```

## Your quest

Write `add_item(item: String, amount: int) -> int` that fills `slots` as described and returns how many items didn't fit (`0` when everything fit).

## Review

<details><summary>Why fill existing stacks before empty slots?</summary>So the same item stays together instead of spreading over many slots.</details>
<details><summary>What should add_item return when everything fit?</summary>0, the number of items left over.</details>
