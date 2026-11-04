sp, be, os_ = ns.get("split"), ns.get("best_epoch"), ns.get("overfitting_starts")
assert sp and be and os_, "Keep split, best_epoch and overfitting_starts."
tr, va = sp(list(range(10)), 0.3)
assert tr == list(range(7)) and va == [7, 8, 9], f"split(range(10), 0.3) returned {tr!r}, {va!r}; expected the last 3 as validation."
tr, va = sp(list(range(5)), 0.1)
assert tr == list(range(5)) and va == [], "With int(5 × 0.1) = 0 validation items, everything is training."
assert be([3.0, 2.0, 2.5, 1.5, 1.7]) == 3, "best_epoch([3, 2, 2.5, 1.5, 1.7]) should be 3."
assert os_([5, 4, 3, 2], [5, 4, 4.5, 5]) == 2, "Training falls at epoch 2 while validation rises: overfitting starts at 2."
assert os_([5, 4, 3], [5, 4, 3]) is None, "When validation keeps falling, return None."
assert os_([5, 5.2, 4], [5, 5.5, 4]) is None, "Epoch 1: both rise (not overfitting). Epoch 2: both fall. Return None."
