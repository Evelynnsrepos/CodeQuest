func count_big(coins: Array, at_least: int) -> int:
	var count := 0
	for c in coins:
		if c >= at_least:
			count += 1
	return count


func run():
	print(count_big([3, 7, 2, 10], 5))
