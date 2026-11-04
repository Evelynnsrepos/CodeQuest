extends VBoxContainer

var score_label := Label.new()
var health_bar := ProgressBar.new()


func _ready():
	score_label.text = "Score: 0"
	add_child(score_label)
	add_child(health_bar)


func on_score_changed(score: int) -> void:
	score_label.text = "Score: %d" % score


func on_health_changed(health: int, max_health: int) -> void:
	health_bar.max_value = max_health
	health_bar.value = health
