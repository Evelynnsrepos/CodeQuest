ls
git status

# Write .gitignore here, one pattern per line
echo "secret.env" > .gitignore
echo "build/" >> .gitignore
echo "*.log" >> .gitignore

git add .
git commit -m "Add app"
git status
