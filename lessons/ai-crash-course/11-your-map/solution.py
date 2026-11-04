import math


def plan(minutes_per_day, lessons, minutes_per_lesson=20):
    return math.ceil(lessons * minutes_per_lesson / minutes_per_day)


PICK = "LLMs 1: How an LLM works"
print(plan(30, 14), "days;", "next:", PICK or "(not chosen yet)")
