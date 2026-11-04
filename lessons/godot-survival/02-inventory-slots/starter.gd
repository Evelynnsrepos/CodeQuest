extends Node

var stack_size := 10
var slots := [null, null, null, null]


func add_item(item: String, amount: int) -> int:
	var remaining := amount
	# pass 1: top up stacks of the same item
	# pass 2: start new stacks in empty slots
	return remaining
