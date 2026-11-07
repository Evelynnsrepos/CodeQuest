import re


def readme_report(text):
    # lines = text.splitlines()
    # first = ""
    # for l in lines:
    #     if l.strip() != "":
    #         first = l
    #         break
    # heads = []
    # for l in lines:
    #     if l.startswith("#"):
    #         heads.append(l.lower())
    # low = text.lower()
    # report = {
    #     "title": first.startswith("# "),
    #     "run": False,
    #     "docker": "docker run" in low or "docker compose" in low,
    #     "eval": False,
    #     "numbers": re.search(r"\d+%|\d\.\d+", text) is not None,
    #     "license": False,
    # }
    # for h in heads:
    #     if "run" in h or "install" in h or "usage" in h:
    #         report["run"] = True
    #     if "eval" in h or "results" in h:
    #         report["eval"] = True
    #     if "license" in h:
    #         report["license"] = True
    # return report
    return {}


def score(text):
    # report = readme_report(text)
    # total = 0
    # for key in report:
    #     if report[key]:
    #         total = total + 1
    # return total
    return 0


MY_README = """my project
"""
print(readme_report(MY_README), score(MY_README))
