def total_loot(chests):
    total = 0
    for gold in chests:
        total += gold
    return total


print(total_loot([3, 7, 2]))
