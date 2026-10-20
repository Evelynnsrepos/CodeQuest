git init --bare ../server.git
git init
echo "# Shared project" > README.md
git add README.md
git commit -m "Initial commit"
echo "print('hi')" > main.py
git add main.py
git commit -m "Add main.py"
