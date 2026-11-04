f = ns.get("inbox_helper")
assert f, "Keep the function inbox_helper."
def model(p):
    if "FREE" in p: return " Spam.\n"
    if "Thursday" in p: return "REPLY"
    if "weird" in p: return "I'd say spam, probably"
    return "other"
mails = [{"id": "a", "text": "FREE stuff"}, {"id": "b", "text": "Thursday?"}, {"id": "c", "text": "news"}, {"id": "d", "text": "weird one"}]
calls = []
def spy(p):
    calls.append(p)
    return model(p)
# Step 1: skip done
r = f(mails, spy, {"a", "b", "c", "d"})
assert r.get("skipped") == 4 and calls == [], "Step 1: skip emails already in done (and don't ask the model about them)."
# Step 2: label
done = set()
r = f(mails, spy, done)
assert len(calls) == 4, "Step 2: ask the model once per new email."
assert "spam, reply, other" in calls[0] and "FREE stuff" in calls[0], "Step 2: the prompt needs the text and 'spam, reply, other'."
# Steps 3 and 4: plan and gate
assert r.get("run_now") == [{"tool": "archive", "id": "a"}], f"Steps 3-4: spam is archived right away, got run_now={r.get('run_now')!r}."
assert r.get("ask_first") == [{"tool": "send_reply", "id": "b"}], f"Steps 3-4: replies wait for approval; 'other' and unclear labels get no action. Got ask_first={r.get('ask_first')!r}."
# Step 5: mark done
assert done == {"a", "b", "c", "d"}, "Step 5: mark every handled email done, even ones with no action."
r2 = f(mails + [{"id": "e", "text": "FREE again"}], model, done)
assert r2 == {"run_now": [{"tool": "archive", "id": "e"}], "ask_first": [], "skipped": 4}, f"Running again only handles the new email, got {r2!r}."
