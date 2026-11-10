import math


def plan(minutes_per_day, lessons, minutes_per_lesson=20):
    total_minutes = lessons * minutes_per_lesson
    return math.ceil(total_minutes / minutes_per_day)


# Pick the course you'll do next (any of the PICK blocks is right):
PICK = "LLMs 1: How an LLM works"
print(plan(30, 14), "days;", "next:", PICK or "(not chosen yet)")
