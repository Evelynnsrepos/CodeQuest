import math


def batches(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def run_minutes(n_items, seconds_per_item, parallel):
    return math.ceil(n_items / parallel) * seconds_per_item / 60


print(batches(list(range(7)), 3))
print(run_minutes(600, 4, 2))
