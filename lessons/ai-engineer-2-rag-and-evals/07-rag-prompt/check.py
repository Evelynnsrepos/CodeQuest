bp, ci, ca, HEADER = ns.get("build_prompt"), ns.get("citations"), ns.get("check_answer"), ns.get("HEADER")
assert bp and ci and ca and HEADER, "Keep build_prompt, citations, check_answer and HEADER."
chunks = [{"id": "a", "text": "x" * 36}, {"id": "b", "text": "y" * 36}, {"id": "c", "text": "z"}]
prompt, used = bp("why?", chunks, budget=20)
assert used == ["a"], f"Each source line '[n] (id) ' + 36 characters is 44 characters = 11 tokens; only one fits in 20, and you stop at the first that doesn't fit. Got {used!r}."
assert prompt == HEADER + "\n\n[1] (a) " + "x" * 36 + "\n\nQuestion: why?", f"Prompt layout: header, blank line, sources, blank line, question. Got {prompt!r}."
prompt, used = bp("q", chunks, budget=100)
assert used == ["a", "b", "c"] and "[3] (c) z" in prompt, "With room, all sources in order, numbered from 1."
assert ci("See [2] and [1], also [2].") == [1, 2], "citations: sorted, distinct."
assert ca("Use it [1].", 2) == "ok" and ca("Use it [3].", 2) == "bad citation" and ca("Use [0].", 2) == "bad citation", "check_answer: numbers must be 1..n_sources."
assert ca("Just do it.", 2) == "no citations" and ca("I don't know.", 2) == "ok", "No citations is only fine for I don't know."
