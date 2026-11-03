import random
cl, sp = ns.get("clean"), ns.get("split")
assert cl and sp, "Keep clean and split."
raw = [{"prompt": " A ", "answer": " x "}, {"prompt": "a", "answer": "dup"}, {"prompt": "B", "answer": "  "},
       {"prompt": "  ", "answer": "y"}, {"prompt": "C", "answer": "z"}]
got = cl(raw)
assert got == [{"prompt": "A", "answer": "x"}, {"prompt": "C", "answer": "z"}], f"clean returned {got!r}, expected [{{'prompt': 'A', 'answer': 'x'}}, {{'prompt': 'C', 'answer': 'z'}}]."
assert raw[0]["prompt"] == " A ", "clean shouldn't change the records it was given; build new dictionaries."
items = list(range(25))
tr, va, te = sp(items, 7)
assert len(va) == 2 and len(te) == 2 and len(tr) == 21, f"25 items should split 21 / 2 / 2, got {len(tr)} / {len(va)} / {len(te)}."
assert sorted(tr + va + te) == items, "Every item must end up in exactly one split."
assert items == list(range(25)), "split shouldn't shuffle the original list; shuffle a copy."
expect = list(range(25)); random.Random(7).shuffle(expect)
assert tr + va + te == expect, "Shuffle a copy with random.Random(seed).shuffle, then take train, then val, then test in that order."
assert sp(items, 7) == (tr, va, te), "The same seed must give the same split."
