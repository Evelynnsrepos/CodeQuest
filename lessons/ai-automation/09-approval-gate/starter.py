def gate(actions, auto_ok):
    return actions, []


actions = [
    {"tool": "label", "args": {"id": 1, "label": "bills"}},
    {"tool": "send_email", "args": {"to": "boss@work.com"}},
    {"tool": "draft", "args": {"id": 2}},
]
run_now, ask_first = gate(actions, {"label", "draft"})
print("run now:", [a["tool"] for a in run_now])
print("ask first:", [a["tool"] for a in ask_first])
