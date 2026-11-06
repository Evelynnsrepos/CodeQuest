def choose(prompt_works, needs_facts, needs_style):
    # if prompt_works:   inside: return "prompt"
    # if needs_facts:    inside: return "rag"
    # if needs_style:    inside: return "fine-tune"
    # last line: return "prompt"
    return ""


# Write "prompt", "rag" or "fine-tune" between each pair of empty quotes:
CASES = {
    "answer questions about the 200-page handbook that changes monthly": "",
    "always reply in our brand voice and exact JSON format; prompts keep drifting": "",
    "summarize meeting notes; a good prompt already works": "",
}
print(choose(False, True, False), CASES)
