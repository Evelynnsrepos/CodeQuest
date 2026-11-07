def inbox_helper(emails, llm, done):
    result = {"run_now": [], "ask_first": [], "skipped": 0}
    for email in emails:
        if email["id"] in done:
            result["skipped"] = result["skipped"] + 1
            continue
        prompt = "Answer with one word from: spam, reply, other.\n\n" + email["text"]
        label = llm(prompt).strip().lower().strip(".")
        if label == "spam":
            result["run_now"].append({"tool": "archive", "id": email["id"]})
        elif label == "reply":
            result["ask_first"].append({"tool": "send_reply", "id": email["id"]})
        done.add(email["id"])
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
