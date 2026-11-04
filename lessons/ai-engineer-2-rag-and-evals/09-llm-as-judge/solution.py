import json
import re


def parse_verdict(text):
    m = re.search(r"\{.*?\}", text, re.S)
    if not m:
        return None
    try:
        w = json.loads(m.group(0)).get("winner")
    except (json.JSONDecodeError, AttributeError):
        return None
    return w if w in ("A", "B", "tie") else None


def pairwise(judge, question, x, y):
    first = parse_verdict(judge(question, x, y))
    second = parse_verdict(judge(question, y, x))
    if first == "A" and second == "B":
        return "x"
    if first == "B" and second == "A":
        return "y"
    return "tie"


def kappa(a, b):
    n = len(a)
    p_o = sum(x == y for x, y in zip(a, b)) / n
    labels = set(a) | set(b)
    p_e = sum((a.count(l) / n) * (b.count(l) / n) for l in labels)
    return (p_o - p_e) / (1 - p_e) if p_e < 1 else 1.0


print(parse_verdict('Sure! {"winner": "B", "reason": "more precise"}'))
human = ["good", "bad", "good", "good", "bad", "good"]
judge = ["good", "bad", "good", "bad", "bad", "good"]
print(kappa(human, judge))
