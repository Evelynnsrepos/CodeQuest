def changed_files(before, now):
    return list(now)


before = {"receipt1.jpg": 100, "receipt2.jpg": 200}
now = {"receipt1.jpg": 100, "receipt2.jpg": 250, "receipt3.jpg": 300}
print(changed_files(before, now))
