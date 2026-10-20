# 1. Tell git who you are
git config --global user.name "Ada Lovelace"
git config --global user.email "ada@example.com"

# 2. Turn this folder into a repository
git init

echo "# My project" > README.md

# 3. Stage README.md and commit it with the message "First commit"
git add README.md
git commit -m "First commit"

git log --oneline
