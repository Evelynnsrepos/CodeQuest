A = ns.get("ANSWERS")
assert isinstance(A, dict), "Keep the ANSWERS dict."
key = {1: "a", 2: "b", 3: "b", 4: "c", 5: "b", 6: "a", 7: "b", 8: "a"}
hint = {1: "what does the + in x = x + f(x) do to the gradient?", 2: "what part of RoPE depends on position?",
        3: "think about cost at inference, not training", 4: "which stage shards the weights too?",
        5: "Goodhart's law", 6: "what is the baseline in A = (r - mean) / std?", 7: "compare with ln(vocab)",
        8: "self-consistency"}
for q in key:
    got = str(A.get(q, "")).strip().lower()
    assert got, f"Question {q} has no answer yet."
    assert got == key[q], f"Question {q} isn't right. Hint: {hint[q]}."
