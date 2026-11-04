ch, CASES = ns.get("choose"), ns.get("CASES")
assert ch and isinstance(CASES, dict), "Keep choose and CASES."
assert ch(True, True, True) == "prompt", "If a prompt already works, stop there."
assert ch(False, True, True) == "rag", "Missing knowledge comes first: RAG."
assert ch(False, False, True) == "fine-tune" and ch(False, False, False) == "prompt", "Style → fine-tune; nothing specific → keep prompting."
want = ["rag", "fine-tune", "prompt"]
for (k, v), w in zip(CASES.items(), want):
    assert v.strip().lower() == w, f"'{k[:40]}...' → think about what is missing: knowledge, behaviour, or nothing."
