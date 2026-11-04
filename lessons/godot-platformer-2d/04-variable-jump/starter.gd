extends CharacterBody2D

var gravity := 980.0
var jump_velocity := -450.0
var jump_cut := 0.5


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = jump_velocity

	# cut the jump short when the button is released early

	move_and_slide()
