extends Node2D

var health := 100
var day := 1
var items := {}


func save_text() -> String:
	return JSON.stringify({
		"health": health,
		"day": day,
		"items": items,
		"position": {"x": position.x, "y": position.y},
	})


func load_text(text: String) -> void:
	var data = JSON.parse_string(text)
	health = int(data.health)
	day = int(data.day)
	items = data.items
	position = Vector2(data.position.x, data.position.y)
