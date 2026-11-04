extends CharacterBody2D

var gravity := 980.0
var speed := 200.0
var jump_velocity := -400.0
var coyote_time := 0.1
var buffer_time := 0.1
var coyote_timer := 0.0
var buffer_timer := 0.0


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	if is_on_floor():
		coyote_timer = coyote_time
	else:
		coyote_timer -= delta

	if Input.is_action_just_pressed("ui_accept"):
		buffer_timer = buffer_time
	else:
		buffer_timer -= delta

	if buffer_timer > 0 and coyote_timer > 0:
		velocity.y = jump_velocity
		buffer_timer = 0
		coyote_timer = 0

	velocity.x = Input.get_axis("ui_left", "ui_right") * speed
	move_and_slide()
