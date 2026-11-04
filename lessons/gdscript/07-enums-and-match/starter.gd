enum State { IDLE, CHASE, ATTACK }

var state := State.IDLE


func next_state(distance: float) -> void:
	pass


func describe() -> String:
	return ""


func run():
	next_state(100)
	print(describe())
