git init
echo "Hello, world!" > greeting.txt
git add greeting.txt
git commit -m "Add greeting"
git switch -c friendly
echo "Hi there!" > greeting.txt
git commit -am "Make greeting friendlier"
git switch main
echo "Hello, everyone!" > greeting.txt
git commit -am "Greet everyone"
