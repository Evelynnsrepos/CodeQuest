extends Node

var recipes := {
	"axe": {"wood": 3, "stone": 2},
	"campfire": {"wood": 5},
	"bandage": {"cloth": 2},
}
var items := {"wood": 4, "stone": 1}


func can_craft(thing: String) -> bool:
	if not recipes.has(thing):
		return false
	var recipe: Dictionary = recipes[thing]
	for ingredient in recipe:
		if items.get(ingredient, 0) < recipe[ingredient]:
			return false
	return true


func craft(thing: String) -> bool:
	if not can_craft(thing):
		return false
	var recipe: Dictionary = recipes[thing]
	for ingredient in recipe:
		items[ingredient] -= recipe[ingredient]
	items[thing] = items.get(thing, 0) + 1
	return true
