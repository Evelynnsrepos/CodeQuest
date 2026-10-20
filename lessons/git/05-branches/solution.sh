git branch

# 1. Create the dark-mode branch and switch to it
git switch -c dark-mode

# 2. Write theme.txt and commit it
echo "theme = dark" > theme.txt
git add theme.txt
git commit -m "Add dark mode"

# 3. Switch back to main
git switch main

git branch
ls
