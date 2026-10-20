git init
echo "speed = 5" > game.txt
echo "lives = 1" > player.txt
git add game.txt player.txt
git commit -m "Add game settings"
echo "speed = 9000" > game.txt
git commit -am "Set speed to 9000"
echo "lives = 3" > player.txt
git commit -am "Give the player 3 lives"
