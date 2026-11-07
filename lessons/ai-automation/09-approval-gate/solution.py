def gate(actions, auto_ok):
    run_now = []
    ask_first = []
    for action in actions:
        if action["tool"] in auto_ok:
            run_now.append(action)
        else:
            ask_first.append(action)
    return run_now, ask_first


actions = [
    {"tool": "label", "args": {"id": 1, "label": "bills"}},
    {"tool": "send_email", "args": {"to": "boss@work.com"}},
    {"tool": "draft", "args": {"id": 2}},
]
run_now, ask_first = gate(actions, {"label", "draft"})
for action in run_now:
    print("run now:", action["tool"])
for action in ask_first:
    print("ask first:", action["tool"])
