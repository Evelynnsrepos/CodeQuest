ANSWERS = {
    1: "b",
    2: "a",
    3: "b",
    4: "a",
    5: "b",
    6: "a",
    7: "a",
    8: "a",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
