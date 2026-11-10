def changed_files(before, now):
    # found = []
    # for name in now:
    #     if before.get(name) != now[name]:
    #         found.append(name)
    # return sorted(found)
    return list(now)


before = {"receipt1.jpg": 100, "receipt2.jpg": 200}
now = {"receipt1.jpg": 100, "receipt2.jpg": 250, "receipt3.jpg": 300}
print(changed_files(before, now))
