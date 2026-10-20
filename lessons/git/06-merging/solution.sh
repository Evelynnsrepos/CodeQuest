git log --oneline --graph --all

# Merge login-page into main, then delete the branch
git switch main
git merge login-page
git branch -d login-page

git log --oneline
