ANSWERS = {
    1: "a",
    2: "b",
    3: "b",
    4: "c",
    5: "b",
    6: "a",
    7: "b",
    8: "a",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
