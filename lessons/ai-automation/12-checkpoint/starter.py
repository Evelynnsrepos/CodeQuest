def inbox_helper(emails, llm, done):
    result = {"run_now": [], "ask_first": [], "skipped": 0}
    # for email in emails:
    #     1. skip:   if email["id"] in done: count it in result["skipped"], then continue
    #     2. label:  prompt = "Answer with one word from: spam, reply, other.\n\n" + email["text"]
    #                label = llm(prompt).strip().lower().strip(".")
    #     3+4. plan and gate:  if label == "spam": ... run_now   elif label == "reply": ... ask_first
    #     5. mark:   done.add(email["id"])
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
