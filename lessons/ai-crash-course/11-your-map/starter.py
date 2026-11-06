import math


def plan(minutes_per_day, lessons, minutes_per_lesson=20):
    # total_minutes = lessons * minutes_per_lesson
    # return math.ceil(total_minutes / minutes_per_day)
    return 0


# Write the course you'll do next between the quotes:
PICK = ""
print(plan(30, 14), "days;", "next:", PICK or "(not chosen yet)")
