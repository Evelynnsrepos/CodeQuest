ch, rs = ns.get("choices", {}), ns.get("reasons", {})
want = {"notes": "rag", "pirate": "finetune", "football": "rag", "json": "finetune", "helper": "both", "german": "prompt"}
hints = {"notes": "notes: is this knowledge or behaviour? And it changes every week.",
         "pirate": "pirate: you can't use a system prompt here, and the behaviour must hold in every reply.",
         "football": "football: the model was trained before this weekend. Can training keep up with results?",
         "json": "json: prompting already failed 1 in 10. Is a format knowledge or behaviour?",
         "helper": "helper: style is one kind of problem, documentation another.",
         "german": "german: can the model already do this if you just ask?"}
for k, v in want.items():
    assert ch.get(k) in ("prompt", "rag", "finetune", "both"), f"Set choices[{k!r}] to \"prompt\", \"rag\", \"finetune\" or \"both\"."
    assert ch[k] == v, hints[k]
ideas = {"rag": ("knowledge", "fact", "change", "update", "cite", "source", "retriev", "look up", "lookup", "document", "new"),
         "finetune": ("behavio", "style", "format", "schema", "always", "every", "consisten", "bake", "example", "persona", "tone"),
         "both": ("style", "behavio", "knowledge", "fact", "doc"),
         "prompt": ("prompt", "already", "ask", "instruction", "system", "no training")}
for k, v in want.items():
    text = (rs.get(k) or "").strip()
    assert len(text) >= 40, f"Write a real reason for {k!r} (at least a full sentence)."
    assert any(w in text.lower() for w in ideas[v]), f"Your reason for {k!r} doesn't mention why {v} fits. Use the key idea (e.g. {', '.join(ideas[v][:4])})."
