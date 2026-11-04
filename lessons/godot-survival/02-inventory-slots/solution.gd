extends Node

var stack_size := 10
var slots := [null, null, null, null]


func add_item(item: String, amount: int) -> int:
	var remaining := amount
	for slot in slots:
		if remaining == 0:
			break
		if slot != null and slot.item == item and slot.count < stack_size:
			var put := mini(remaining, stack_size - slot.count)
			slot.count += put
			remaining -= put
	for i in slots.size():
		if remaining == 0:
			break
		if slots[i] == null:
			var put := mini(remaining, stack_size)
			slots[i] = {"item": item, "count": put}
			remaining -= put
	return remaining
