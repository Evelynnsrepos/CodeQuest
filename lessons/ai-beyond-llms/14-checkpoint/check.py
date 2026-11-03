A = ns.get("ANSWERS")
assert isinstance(A, dict), "Keep the ANSWERS dict."
key = {1: "b", 2: "b", 3: "a", 4: "b", 5: "a", 6: "b", 7: "b", 8: "a"}
hint = {1: "what wins on tabular data?", 2: "parallelism and long-range links", 3: "weight sharing",
        4: "the training loss is MSE on what?", 5: "zero-shot with captions", 6: "recall = TP / (TP + FN)",
        7: "encoder + projector", 8: "look at the target in the update"}
for q in key:
    got = str(A.get(q, "")).strip().lower()
    assert got, f"Question {q} has no answer yet."
    assert got == key[q], f"Question {q} isn't right. Hint: {hint[q]}."
