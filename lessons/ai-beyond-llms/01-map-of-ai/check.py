K = ns.get("KINDS")
assert isinstance(K, dict) and len(K) == 5, "Keep the KINDS dict with its five tasks."
want = ["supervised", "unsupervised", "self-supervised", "reinforcement", "supervised"]
hint = ["it has past examples with the right answer", "nobody gave it labels", "where does the 'label' come from?",
        "it learns from rewards for its actions", "doctors provided the labels"]
for (task, got), w, h in zip(K.items(), want, hint):
    assert str(got).strip().lower() == w, f"'{task}': not {got!r}. Hint: {h}."
