import json
import re


def parse_verdict(text):
    return None


def pairwise(judge, question, x, y):
    return "tie"


def kappa(a, b):
    return 0.0


print(parse_verdict('Sure! {"winner": "B", "reason": "more precise"}'))
human = ["good", "bad", "good", "good", "bad", "good"]
judge = ["good", "bad", "good", "bad", "bad", "good"]
print(kappa(human, judge))
