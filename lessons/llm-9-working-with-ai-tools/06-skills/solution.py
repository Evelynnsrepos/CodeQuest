import re


def parse_skill(text):
    if not text.startswith("---"):
        return {"body": text}
    lines = text.split("\n")
    end = lines.index("---", 1)
    out = {}
    for line in lines[1:end]:
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    out["body"] = "\n".join(lines[end + 1:])
    return out


def words(s):
    return set(re.findall(r"[a-z]+", s.lower()))


def pick_skill(skills, task):
    best, best_n = None, 0
    for name, desc in skills.items():
        n = len(words(desc) & words(task))
        if n > best_n:
            best, best_n = name, n
    return best


doc = "---\nname: new-lesson\ndescription: Add a CodeQuest lesson\n---\n1. Copy a folder"
print(parse_skill(doc), pick_skill({"deploy": "Deploy the server", "new-lesson": "Add a CodeQuest lesson"}, "add a lesson about entropy"))
