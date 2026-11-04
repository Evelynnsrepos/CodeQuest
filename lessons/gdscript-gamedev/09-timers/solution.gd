extends Node

var spawn_every := 0.2
var spawned := 0


func _ready():
	var timer := Timer.new()
	timer.name = "SpawnTimer"
	timer.wait_time = spawn_every
	timer.timeout.connect(_on_spawn_timer_timeout)
	add_child(timer)
	timer.start()


func _on_spawn_timer_timeout():
	spawned += 1
