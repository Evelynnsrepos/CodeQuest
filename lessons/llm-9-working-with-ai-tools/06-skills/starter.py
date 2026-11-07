def parse_skill(text):
    # if not text.startswith("---"):
    #     return {"body": text}
    # lines = text.split("\n")
    # end = lines.index("---", 1)
    # out = {}
    # for line in lines[1:end]:
    #     if ":" in line:
    #         pieces = line.split(":", 1)
    #         out[pieces[0].strip()] = pieces[1].strip()
    # out["body"] = "\n".join(lines[end + 1:])
    # return out
    return {}


def words(s):
    out = set()
    word = ""
    for ch in s.lower() + " ":
        if "a" <= ch <= "z":
            word = word + ch
        elif word != "":
            out.add(word)
            word = ""
    return out


def pick_skill(skills, task):
    # best = None
    # best_n = 0
    # task_words = words(task)
    # for name in skills:
    #     n = 0
    #     for w in words(skills[name]):
    #         if w in task_words:
    #             n = n + 1
    #     if n > best_n:
    #         best = name
    #         best_n = n
    # return best
    return None


doc = "---\nname: new-lesson\ndescription: Add a CodeQuest lesson\n---\n1. Copy a folder"
print(parse_skill(doc), pick_skill({"deploy": "Deploy the server", "new-lesson": "Add a CodeQuest lesson"}, "add a lesson about entropy"))
