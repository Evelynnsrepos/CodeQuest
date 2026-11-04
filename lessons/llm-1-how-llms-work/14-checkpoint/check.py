assert ns.get("sees_first_message") is False, "Question 1: 11,000 tokens don't fit in 8,192. With a rolling window, which messages are thrown away first?"
w = ns.get("why_it_forgets")
assert w == "b", {"a": "Question 2: the weights never change while you chat. Only training changes them.",
                  "c": "Question 2: attention doesn't tire. It is the same calculation for every token.",
                  "d": "Question 2: the model has no memory between messages. Look at lesson 13 again."}.get(w, "Question 2: set why_it_forgets to one of \"a\", \"b\", \"c\", \"d\".")
m = ns.get("middle_fact")
assert m == "b", {"a": "Question 3: the document fits in the window, so nothing was dropped.",
                  "c": "Question 3: low temperature makes answers more predictable, not more forgetful."}.get(m, "Question 3: set middle_fact to \"a\", \"b\" or \"c\".")
k = ns.get("keep_instruction")
assert k == "a", {"b": "Question 4: with a rolling window, your first message is the first thing to be dropped.",
                  "c": "Question 4: temperature only changes how tokens are picked; it can't bring back dropped text."}.get(k, "Question 4: set keep_instruction to \"a\", \"b\" or \"c\".")
d = ns.get("dropped")
assert d == 2, f"Question 5: you answered {d!r}. The budget is 4,096 - 512 = 3,584 tokens. Add up the system prompt and messages, then drop the oldest messages one at a time until it fits."
e = (ns.get("explanation") or "").strip()
low = e.lower()
assert len(e) >= 150 and low.count(".") + low.count("!") + low.count("?") >= 3, "Question 6: write at least three full sentences."
assert "token" in low and "context" in low, "Question 6: use the words token and context in your explanation."
assert any(w in low for w in ("drop", "remov", "cut", "truncat", "throw", "no longer", "doesn't see", "does not see", "can't see", "cannot see", "left out")), "Question 6: say what happens to the oldest messages when the chat no longer fits."
