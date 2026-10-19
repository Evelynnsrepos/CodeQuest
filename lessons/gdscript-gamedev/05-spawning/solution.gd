extends Node2D


func spawn_coins(count: int, spacing: float) -> void:
	for i in count:
		var coin := Node2D.new()
		coin.name = "Coin%d" % i
		coin.position = Vector2(i * spacing, 0)
		add_child(coin)
