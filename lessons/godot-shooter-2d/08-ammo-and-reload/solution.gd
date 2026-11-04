extends Node

var magazine_size := 12
var magazine := 12
var reserve := 30


func fire() -> bool:
	if magazine == 0:
		return false
	magazine -= 1
	return true


func reload() -> void:
	var moved := mini(magazine_size - magazine, reserve)
	magazine += moved
	reserve -= moved
