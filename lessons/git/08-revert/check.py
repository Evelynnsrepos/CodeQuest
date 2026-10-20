subjects = git("log", "--format=%s").splitlines()
assert len(subjects) == 4, "Make exactly one new commit with git revert (history shouldn't be rewritten)."
assert subjects[0] == 'Revert "Set speed to 9000"', "The newest commit should revert \"Set speed to 9000\". Which HEAD~ is it?"
assert read("game.txt").strip() == "speed = 5", "game.txt should say speed = 5 again."
assert read("player.txt").strip() == "lives = 3", "Keep the good commit: player.txt should still say lives = 3."
assert git("status", "--porcelain") == "", "Everything should be committed at the end."
