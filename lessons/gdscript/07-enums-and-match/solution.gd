enum State { IDLE, CHASE, ATTACK }

var state := State.IDLE


func next_state(distance: float) -> void:
	if distance <= 30:
		state = State.ATTACK
	elif distance <= 200:
		state = State.CHASE
	else:
		state = State.IDLE


func describe() -> String:
	match state:
		State.ATTACK:
			return "attack"
		State.CHASE:
			return "chase"
		_:
			return "idle"


func run():
	next_state(100)
	print(describe())
