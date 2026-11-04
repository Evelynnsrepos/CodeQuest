---
title: Joining tables
xp: 50
---
# Orders without customers

> **Warm-up:** you have a customers table and an orders table. How do you find out each order's city?

Data often comes in **several tables** linked by an **ID**: orders have a `customer_id` that points to a row in customers. A **join** combines them.

A **left join** keeps every row of the left table and adds the matching right row's columns. When nothing matches, the new columns are `None`, and that's a **data-quality signal**: an order for a customer who doesn't exist means something upstream is broken.

Two traps:

1. **Key types.** `"7"` (text from CSV) ≠ `7` (a number). Clean keys to one type first (`str(k).strip()`).
2. **Duplicate keys on the right.** If customer 7 appears twice, every order of customer 7 is doubled. Check that the right side's key is unique before joining.

## Python you need

Build a **lookup dict** from the right table once, then each match is instant:

```python
by_id = {str(c["id"]).strip(): c for c in customers}
by_id.get("7")   # the row, or None
```

## Your quest

1. `duplicate_keys(rows, key)`: the sorted list of key values (as stripped strings) that appear more than once.
2. `left_join(left, right, left_key, right_key)`: for each left row, a new dict with all its columns plus all right columns **except** `right_key`; missing matches get those columns as `None`. Assume `right` has unique keys. Compare keys as stripped strings.
3. `orphans(left, right, left_key, right_key)`: the left rows with **no** match.

**Remember:** check keys are unique and the same type before joining.

## Review

<details><summary>Why redact IBANs before phone numbers?</summary>The phone pattern would otherwise match the IBAN's digit groups first.</details>
