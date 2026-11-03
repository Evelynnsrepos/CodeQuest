choices = {
    "notes": "rag",
    "pirate": "finetune",
    "football": "rag",
    "json": "finetune",
    "helper": "both",
    "german": "prompt",
}

reasons = {
    "notes": "It's knowledge that changes every week, so retrieve it at question time; RAG can also cite the note it used.",
    "pirate": "It's a behaviour that must hold with no system prompt in a small model, so bake the style in with fine-tuning.",
    "football": "These are new facts that change every weekend; the model can't know them, so look them up with RAG.",
    "json": "A strict output format is behaviour; a few hundred examples teach the model to follow the schema every time.",
    "helper": "My writing style is behaviour (fine-tune) and the project docs are knowledge (RAG), so it needs both.",
    "german": "The model already speaks German well, so a system prompt asking for German summaries is enough.",
}
