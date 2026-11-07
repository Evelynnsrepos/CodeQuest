import json
import re


def parse_verdict(text):
    # m = re.search(r"\{.*?\}", text, re.S)
    # if m is None:
    #     return None
    # try:
    #     data = json.loads(m.group(0))
    #     w = data.get("winner")
    # except (json.JSONDecodeError, AttributeError):
    #     return None
    # if w in ["A", "B", "tie"]:
    #     return w
    # return None
    return None


def pairwise(judge, question, x, y):
    # first = parse_verdict(judge(question, x, y))
    # second = parse_verdict(judge(question, y, x))
    # if first == "A" and second == "B":
    #     return "x"
    # if first == "B" and second == "A":
    #     return "y"
    # return "tie"
    return "tie"


def kappa(a, b):
    # n = len(a)
    # same = 0
    # for i in range(n):
    #     if a[i] == b[i]:
    #         same = same + 1
    # p_o = same / n
    # p_e = 0
    # for label in set(a) | set(b):
    #     p_e = p_e + (a.count(label) / n) * (b.count(label) / n)
    # if p_e == 1:
    #     return 1.0
    # return (p_o - p_e) / (1 - p_e)
    return 0.0


print(parse_verdict('Sure! {"winner": "B", "reason": "more precise"}'))
human = ["good", "bad", "good", "good", "bad", "good"]
judge = ["good", "bad", "good", "bad", "bad", "good"]
print(kappa(human, judge))
