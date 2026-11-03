ANSWERS = {
    1: "b",
    2: "b",
    3: "a",
    4: "b",
    5: "a",
    6: "b",
    7: "b",
    8: "a",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
