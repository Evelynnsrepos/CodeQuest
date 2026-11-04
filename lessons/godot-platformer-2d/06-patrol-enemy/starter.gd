extends CharacterBody2D

var gravity := 980.0
var speed := 160.0
var direction := 1
var ledge_ray := RayCast2D.new()


func _ready():
	ledge_ray.position = Vector2(16, 0)
	ledge_ray.target_position = Vector2(0, 40)
	add_child(ledge_ray)


func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	# turn around at walls and ledges, then walk

	move_and_slide()
