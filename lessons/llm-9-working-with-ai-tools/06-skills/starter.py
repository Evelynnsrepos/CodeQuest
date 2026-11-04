import re


def parse_skill(text):
    return {}


def pick_skill(skills, task):
    return None


doc = "---\nname: new-lesson\ndescription: Add a CodeQuest lesson\n---\n1. Copy a folder"
print(parse_skill(doc), pick_skill({"deploy": "Deploy the server", "new-lesson": "Add a CodeQuest lesson"}, "add a lesson about entropy"))
