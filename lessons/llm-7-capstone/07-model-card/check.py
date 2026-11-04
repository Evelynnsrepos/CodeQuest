mc, ms, S = ns.get("make_card"), ns.get("missing_sections"), ns.get("SECTIONS")
assert mc and ms and S, "Keep SECTIONS, make_card and missing_sections."
info = {"name": "m", "base_model": "BASE", "license": "mit", "data": "DATA", "training": "TRAIN",
        "evaluation": "EVAL", "limitations": "LIMIT", "how_to_run": "RUN"}
card = mc(info)
assert card.startswith("# m"), "The card should start with '# <name>'."
pos = [card.find(s + "\n") for s in S]
assert all(p >= 0 for p in pos), "Every section heading should be on its own line."
assert pos == sorted(pos), "The sections should be in table order."
assert "License: mit" in card.splitlines(), "Put 'License: <license>' on its own line."
for word, sec in [("BASE", 0), ("DATA", 1), ("TRAIN", 2), ("EVAL", 3), ("LIMIT", 4), ("RUN", 5)]:
    i = card.find(word)
    nxt = pos[sec + 1] if sec + 1 < len(pos) else len(card)
    assert pos[sec] < i < nxt, f"{word!r} should be inside the {S[sec]!r} section."
assert ms(card) == [], f"A full card should have no missing sections, got {ms(card)!r}."
assert ms("# x\n## Training data\nstuff\n## Evaluation\n") == ["## Base model", "## Training", "## Limitations", "## How to run"], \
    "missing_sections should match whole heading lines ('## Training data' is not '## Training')."
