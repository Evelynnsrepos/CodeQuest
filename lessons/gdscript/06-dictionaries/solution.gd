var bag := {}


func add_item(item: String, amount: int) -> void:
	bag[item] = bag.get(item, 0) + amount


func remove_item(item: String, amount: int) -> bool:
	if bag.get(item, 0) < amount:
		return false
	bag[item] -= amount
	if bag[item] == 0:
		bag.erase(item)
	return true


func run():
	add_item("wood", 3)
	print(bag)
