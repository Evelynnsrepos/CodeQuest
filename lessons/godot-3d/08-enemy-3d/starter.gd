extends CharacterBody3D

var speed := 3.0
var attack_range := 1.5
var attacks := 0
var target := Vector3.ZERO


func _physics_process(delta):
	hunt(target)


func attack() -> void:
	attacks += 1


func hunt(target: Vector3) -> void:
	move_and_slide()
