echo "Remember to drink water" >> notes.txt
echo "Buy milk" >> todo.txt

git status
git diff

# Commit ONLY notes.txt with the message "Add notes"
git add notes.txt
git commit -m "Add notes"

git status
