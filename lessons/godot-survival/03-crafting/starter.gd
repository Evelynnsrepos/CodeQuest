extends Node

var recipes := {
	"axe": {"wood": 3, "stone": 2},
	"campfire": {"wood": 5},
	"bandage": {"cloth": 2},
}
var items := {"wood": 4, "stone": 1}


func can_craft(thing: String) -> bool:
	return false


func craft(thing: String) -> bool:
	return false
