def inbox_helper(emails, llm, done):
    result = {"run_now": [], "ask_first": [], "skipped": 0}
    labels = ["spam", "reply", "other"]
    for email in emails:
        if email["id"] in done:
            result["skipped"] += 1
            continue
        prompt = f"Answer with one word from: {', '.join(labels)}.\n\n{email['text']}"
        label = llm(prompt).strip().lower().strip(".")
        if label not in labels:
            label = "other"
        tool = {"spam": "archive", "reply": "send_reply"}.get(label)
        if tool:
            result["run_now" if tool == "archive" else "ask_first"].append({"tool": tool, "id": email["id"]})
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
