def choose(prompt_works, needs_facts, needs_style):
    if prompt_works:
        return "prompt"
    if needs_facts:
        return "rag"
    if needs_style:
        return "fine-tune"
    return "prompt"


CASES = {
    "answer questions about the 200-page handbook that changes monthly": "rag",
    "always reply in our brand voice and exact JSON format; prompts keep drifting": "fine-tune",
    "summarize meeting notes; a good prompt already works": "prompt",
}
print(choose(False, True, False), CASES)
