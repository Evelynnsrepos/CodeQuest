def inbox_helper(emails, llm, done):
    result = {"run_now": [], "ask_first": [], "skipped": 0}
    # 1. skip done  2. label  3. plan  4. gate  5. mark done
    return result


emails = [
    {"id": "m1", "text": "WIN a FREE phone now!!!"},
    {"id": "m2", "text": "Can we move our call to Thursday?"},
    {"id": "m3", "text": "Your weekly newsletter"},
]


def fake_llm(prompt):
    if "FREE" in prompt:
        return "Spam."
    if "Thursday" in prompt:
        return "reply"
    return "other"


print(inbox_helper(emails, fake_llm, set()))
