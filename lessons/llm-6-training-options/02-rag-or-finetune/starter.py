def decide(goal):
    return ""


goals = {
    "answer questions about my notes": {"needs_facts": True, "needs_behaviour": False, "prompt_works": False},
    "talk like a pirate": {"needs_facts": False, "needs_behaviour": True, "prompt_works": True},
    "always reply in my company's strict JSON schema": {"needs_facts": False, "needs_behaviour": True, "prompt_works": False},
    "support bot for our docs, in our brand voice": {"needs_facts": True, "needs_behaviour": True, "prompt_works": False},
}
for goal, info in goals.items():
    print(f"{goal}: {decide(info)}")
