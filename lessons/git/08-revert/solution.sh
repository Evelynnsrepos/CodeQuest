git log --oneline
cat game.txt player.txt

# Revert the "Set speed to 9000" commit
git revert --no-edit HEAD~1

cat game.txt
