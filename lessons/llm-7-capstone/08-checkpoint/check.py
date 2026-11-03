A = ns.get("ANSWERS")
assert isinstance(A, dict), "Keep the ANSWERS dict."
key = {1: "b", 2: "a", 3: "b", 4: "a", 5: "b", 6: "a", 7: "a", 8: "a"}
why = {1: "compare file sizes with 12 GB", 2: "count bytes per parameter for full training", 3: "what has already influenced your choices?",
       4: "what should the model learn to write?", 5: "what happens after eval_loss starts rising?", 6: "who might be biased?",
       7: "which method adds facts cheaply?", 8: "what can training on one kind of output do to others?"}
for q in key:
    got = str(A.get(q, "")).strip().lower()
    assert got, f"Question {q} has no answer yet."
    assert got == key[q], f"Question {q} isn't right. Hint: {why[q]}."
