import math


def batches(items, size):
    # groups = []
    # current = []
    # for item in items:
    #     current.append(item)
    #     if len(current) == size:
    #         groups.append(current)
    #         current = []
    # if len(current) > 0:
    #     groups.append(current)
    # return groups
    return [items]


def run_minutes(n_items, seconds_per_item, parallel):
    # return math.ceil(n_items / parallel) * seconds_per_item / 60
    return 0


print(batches(list(range(7)), 3))
print(run_minutes(600, 4, 2))
